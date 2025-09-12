# Build-In Modules
import os
import sys
from pathlib import Path

# PyQt6 Modules
from PyQt6.QtCore import QEvent, QSettings, Qt
from PyQt6.QtGui import QIcon
from PyQt6.QtWidgets import (
    QApplication,
    QComboBox,
    QGridLayout,
    QHBoxLayout,
    QLabel,
    QLayoutItem,
    QPushButton,
    QSpinBox,
    QTextEdit,
    QVBoxLayout,
    QWidget,
)

# Helpers Modules
from helpers import Styles, apply_window_style, center_on_screen, generate_tracker
from settings import SettingsDialog


# https://stackoverflow.com/questions/31836104/pyinstaller-and-onefile-how-to-include-an-image-in-the-exe-file#:~:text=def%20resource_path(relative_path)%3A%0A%20%20%20%20%22%22%22%20Get,return%20os.path.join(base_path%2C%20relative_path)
def resource_path(relative_path) -> str:
    """Get absolute path to resource, works for dev and for PyInstaller"""
    try:
        # PyInstaller creates a temp folder and stores path in _MEIPASS
        base_path = sys._MEIPASS
    except Exception:
        base_path: str = os.path.abspath(".")

    return os.path.join(base_path, relative_path)


class SeasonTracker(QWidget):
    def __init__(self) -> None:
        super().__init__()
        self.setWindowTitle("Season Tracker")
        self.setFixedSize(400, 400)

        # Path for .ini file inside AppData\Roaming\
        appdata = os.getenv("APPDATA")  # usually C:\Users\<User>\AppData\Roaming
        settings_dir = os.path.join(appdata, "SeasonTracker")
        os.makedirs(settings_dir, exist_ok=True)

        settings_path: str = os.path.join(settings_dir, "settings.ini")
        self.settings = QSettings(settings_path, QSettings.Format.IniFormat)

        # Window Icon Path
        self.default_icon = str(
            resource_path(Path(__file__).parent / "assets" / "WindowIcon.ico")
        )
        if not self.settings.contains("window_icon"):
            self.settings.setValue("window_icon", self.default_icon)

        # Apply window icon
        self.apply_window_icon()

        self.page_size = self.settings.value("page_size", 12, type=int)
        self.current_page = 0
        self.total_pages = 1
        self.initUI()

    def initUI(self) -> None:
        self.layout = QVBoxLayout(self)

        # Season count selector
        season_layout = QHBoxLayout()
        season_layout.addWidget(QLabel("How many seasons?"))
        # Season spin box
        self.season_spin = QSpinBox()
        self.season_spin.setCursor(Qt.CursorShape.PointingHandCursor)
        self.season_spin.setButtonSymbols(QSpinBox.ButtonSymbols.NoButtons)
        self.season_spin.installEventFilter(self)
        self.season_spin.setStyleSheet(Styles.SEASON_SPIN)
        self.season_spin.setFixedWidth(40)
        self.season_spin.setRange(1, 100)

        default_seasons = self.settings.value("default_season_count", 1, type=int)
        self.season_spin.setValue(default_seasons)

        self.season_spin.valueChanged.connect(self.on_season_spin_changed)
        season_layout.addWidget(self.season_spin)
        self.layout.addLayout(season_layout)

        # Season status selectors
        self.status_layout = QGridLayout()
        self.layout.addLayout(self.status_layout)
        self.status_layout.setHorizontalSpacing(4)
        self.status_layout.setVerticalSpacing(4)
        self.status_layout.setContentsMargins(0, 0, 0, 0)
        self.status_selectors = []

        # Paging controls
        nav_layout = QHBoxLayout()
        nav_layout.setContentsMargins(0, 0, 0, 0)
        nav_layout.setSpacing(8)

        self.prev_button = QPushButton("Previous")
        self.prev_button.setCursor(Qt.CursorShape.PointingHandCursor)
        self.prev_button.setFocusPolicy(Qt.FocusPolicy.NoFocus)
        self.prev_button.setStyleSheet(Styles.PREV_BUTTON)
        self.prev_button.clicked.connect(self.prev_page)

        self.next_button = QPushButton("Next")
        self.next_button.setCursor(Qt.CursorShape.PointingHandCursor)
        self.next_button.setFocusPolicy(Qt.FocusPolicy.NoFocus)
        self.next_button.setStyleSheet(Styles.NEXT_BUTTON)
        self.next_button.clicked.connect(self.next_page)

        self.page_label = QLabel()
        self.page_label.setAlignment(Qt.AlignmentFlag.AlignCenter)

        nav_layout.addWidget(self.prev_button)
        nav_layout.addWidget(self.page_label)
        nav_layout.addWidget(self.next_button)
        self.layout.addLayout(nav_layout)

        self.update_season_inputs()

        # Settings & Generate buttons
        controls_layout = QHBoxLayout()
        controls_layout.setContentsMargins(0, 0, 0, 0)

        self.generate_button = QPushButton("Generate Tracker")
        self.generate_button.setStyleSheet(Styles.GENERATE_BUTTON)
        self.generate_button.setCursor(Qt.CursorShape.PointingHandCursor)
        self.generate_button.setFocusPolicy(Qt.FocusPolicy.NoFocus)

        self.settings_button = QPushButton("🛠️")
        self.settings_button.setFixedSize(32, 32)  # Keep it compact
        self.settings_button.setStyleSheet(Styles.SETTINGS_BUTTON)
        self.settings_button.setCursor(Qt.CursorShape.PointingHandCursor)
        self.generate_button.setFocusPolicy(Qt.FocusPolicy.NoFocus)

        controls_layout.addWidget(self.generate_button)
        controls_layout.addWidget(self.settings_button)
        self.layout.addLayout(controls_layout)

        # Output area
        self.output_area = QTextEdit()
        self.output_area.setReadOnly(True)
        self.output_area.setPlaceholderText("Your tracker will appear here...")
        self.output_area.setStyleSheet(Styles.OUTPUT_AREA)
        self.output_area.setFocusPolicy(Qt.FocusPolicy.NoFocus)
        self.layout.addWidget(self.output_area)

        self.generate_button.clicked.connect(lambda: generate_tracker(self))
        self.settings_button.clicked.connect(self.open_settings)

        apply_window_style(self)
        center_on_screen(self)

    def open_settings(self) -> None:
        dialog = SettingsDialog(self.settings, self)
        if dialog.exec():
            # Reload default season value
            default_value = self.settings.value("default_season_count", 1, type=int)
            self.season_spin.setValue(default_value)

            # Reload page size
            self.page_size = self.settings.value("page_size", 12, type=int)
            self.update_season_inputs()

            # Reload window icon with fallback
            self.apply_window_icon()

    def apply_window_icon(self) -> None:
        icon_path = str(self.settings.value("window_icon", self.default_icon))
        if not Path(icon_path).exists():
            icon_path: str = self.default_icon
        self.setWindowIcon(QIcon(icon_path))

    def on_season_spin_changed(self) -> None:
        self.current_page = 0
        self.update_season_inputs()

    def update_season_inputs(self) -> None:
        # Clear old widgets/layouts from the grid, but do NOT delete QComboBox widgets in all_status_selectors
        while self.status_layout.count():
            child: QLayoutItem | None = self.status_layout.takeAt(0)
            if child.widget():
                # Only remove from layout, do not delete
                child.widget().setParent(None)
            elif child.layout():
                while child.layout().count():
                    sub_child: QLayoutItem | None = child.layout().takeAt(0)
                    if sub_child.widget():
                        sub_child.widget().setParent(None)
                # Remove the layout itself
                child.layout().setParent(None)

        num_seasons: int = self.season_spin.value()
        self.total_pages: int = (num_seasons - 1) // self.page_size + 1
        self.page_label.setText(f"Page {self.current_page + 1} / {self.total_pages}")
        self.prev_button.setEnabled(self.current_page > 0)
        self.next_button.setEnabled(self.current_page < self.total_pages - 1)

        # Only create selectors once, keep their state
        if (
            not hasattr(self, "all_status_selectors")
            or len(getattr(self, "all_status_selectors", [])) != num_seasons
        ):
            self.all_status_selectors = []
            for i in range(1, num_seasons + 1):
                combo = QComboBox()
                combo.setMinimumWidth(120)
                combo.setCursor(Qt.CursorShape.PointingHandCursor)
                options: list[str] = self.settings.value(
                    "status_options",
                    ["📕 To Watch", "📖 Watching", "📗 Finished"],
                    type=list,
                )
                combo.addItems(options)
                combo.setCurrentText(options[0])  # "📕 To Watch" set default
                combo.setStyleSheet(Styles.COMBO)
                self.all_status_selectors.append(combo)

        self.status_selectors = []
        start: int = self.current_page * self.page_size
        end: int = min(start + self.page_size, num_seasons)
        for idx, i in enumerate(range(start + 1, end + 1)):
            row, col = divmod(idx, 2)  # 2 selectors per row
            season_row = QHBoxLayout()
            season_row.setContentsMargins(0, 0, 0, 0)
            season_row.setSpacing(4)

            label = QLabel(f"S{i:02}")
            label.setAlignment(
                Qt.AlignmentFlag.AlignVCenter | Qt.AlignmentFlag.AlignRight
            )
            label.setContentsMargins(0, 0, 0, 0)

            arrow = QLabel("➜")
            arrow.setAlignment(Qt.AlignmentFlag.AlignCenter)
            arrow.setContentsMargins(0, 0, 0, 0)

            combo = self.all_status_selectors[i - 1]
            season_row.addWidget(label)
            season_row.addWidget(arrow)
            season_row.addWidget(combo)

            self.status_layout.addLayout(season_row, row, col)
            self.status_selectors.append(combo)

    def prev_page(self) -> None:
        if self.current_page > 0:
            self.current_page -= 1
            self.update_season_inputs()

    def next_page(self) -> None:
        if self.current_page < self.total_pages - 1:
            self.current_page += 1
            self.update_season_inputs()

    def keyPressEvent(self, event) -> None:
        Key_Esc = "\x1b"
        # Neovim style: 'h' for prev, 'l' for next
        text = event.text()
        if text == "l":
            if self.current_page < self.total_pages - 1:
                self.next_page()
        elif text == "h":
            if self.current_page > 0:
                self.prev_page()
        elif event.key() in (Qt.Key.Key_Return, Qt.Key.Key_Enter):
            generate_tracker(self)
        elif text == Key_Esc:
            self.close()
        elif event.key() == Qt.Key.Key_Home:
            self.open_settings()
        else:
            super().keyPressEvent(event)

    def eventFilter(self, obj, event) -> bool:
        if obj == self.season_spin and event.type() == QEvent.Type.KeyPress:
            text = event.text()
            if text == "l":
                if self.current_page < self.total_pages - 1:
                    self.next_page()
                return True
            elif text == "h":
                if self.current_page > 0:
                    self.prev_page()
                return True
            elif event.key() in (Qt.Key.Key_Return, Qt.Key.Key_Enter):
                generate_tracker(self)
                return True
            elif event.key() == Qt.Key.Key_Home:
                self.open_settings()
                return True
        return super().eventFilter(obj, event)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = SeasonTracker()
    window.show()
    sys.exit(app.exec())
