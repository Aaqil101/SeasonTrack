# Build-In Modules
import sys
from pathlib import Path

# Copy to Clipboard
import pyperclip

# PyQt6 Modules
from PyQt6.QtCore import QEvent, Qt, QTimer
from PyQt6.QtGui import QIcon
from PyQt6.QtWidgets import (
    QApplication,
    QComboBox,
    QGridLayout,
    QHBoxLayout,
    QLabel,
    QLayoutItem,
    QMessageBox,
    QPushButton,
    QSpinBox,
    QTextEdit,
    QVBoxLayout,
    QWidget,
)

# WinMica for Windows 11 Mica Effect
from winmica import ApplyMica, MicaType, is_mica_supported

# Helpers Modules
from helpers import Blur, Styles, center_on_screen


# https://stackoverflow.com/questions/31836104/pyinstaller-and-onefile-how-to-include-an-image-in-the-exe-file#:~:text=def%20resource_path(relative_path)%3A%0A%20%20%20%20%22%22%22%20Get,return%20os.path.join(base_path%2C%20relative_path)
def resource_path(relative_path: str) -> str:
    """Get absolute path to resource, works for dev and for PyInstaller."""
    try:
        # PyInstaller >= 4 uses _MEIPASS, older versions used _MEIPASS2
        base_path = getattr(sys, "_MEIPASS", getattr(sys, "_MEIPASS2", None))
        if base_path:
            base_path = Path(base_path)
        else:
            base_path: Path = Path.cwd()
    except Exception:
        base_path = Path.cwd()

    return str(base_path / relative_path)


class SeasonTracker(QWidget):
    PAGE_SIZE = 14
    KEY_ESC = "\x1b"

    def __init__(self) -> None:
        super().__init__()
        self.setWindowTitle("Season Tracker")
        self.setFixedSize(400, 400)
        self.setAttribute(Qt.WidgetAttribute.WA_TranslucentBackground, True)
        self.setStyleSheet(
            """
            QLabel {
                font-size: 14px;
                font-weight: 700;
                font-style: normal;
            }
            """
        )
        if is_mica_supported():
            hwnd = int(self.winId())
            ApplyMica(hwnd, MicaType.MICA)

        # Window Icon Path
        IconPath: Path = Path(__file__).parent / "asset" / "AppIcon.ico"
        # icon_path: str = resource_path(str(IconPath))
        # self.setWindowIcon(QIcon(icon_path))
        self.setWindowIcon(QIcon(str(IconPath)))

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
        self.season_spin.setValue(1)
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

        # Generate button
        self.generate_button = QPushButton("Generate Tracker")
        self.generate_button.setStyleSheet(Styles.GENERATE_BUTTON)
        self.generate_button.setCursor(Qt.CursorShape.PointingHandCursor)
        self.generate_button.setFocusPolicy(Qt.FocusPolicy.NoFocus)
        self.generate_button.clicked.connect(self.generate_tracker)
        self.layout.addWidget(self.generate_button)

        # Output area
        self.output_area = QTextEdit()
        self.output_area.setReadOnly(True)
        self.output_area.setPlaceholderText("Your tracker will appear here...")
        self.output_area.setStyleSheet(Styles.OUTPUT_AREA)
        self.output_area.setFocusPolicy(Qt.FocusPolicy.NoFocus)
        self.layout.addWidget(self.output_area)

        # self.apply_window_style()
        center_on_screen(self)

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
        self.total_pages = (num_seasons - 1) // self.PAGE_SIZE + 1
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
                options: list[str] = ["📕 To Watch", "📖 Watching", "📗 Finished"]
                combo.addItems(options)
                combo.setCurrentText(options[0])  # "📕 To Watch" set default
                combo.setStyleSheet(Styles.COMBO)
                self.all_status_selectors.append(combo)

        self.status_selectors = []
        start = self.current_page * self.PAGE_SIZE
        end = min(start + self.PAGE_SIZE, num_seasons)
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

    def generate_tracker(self) -> None:
        symbols: dict[str, str] = {
            "📕 To Watch": "📕",
            "📖 Watching": "📖",
            "📗 Finished": "📗",
        }

        output = []
        for i, combo in enumerate(self.all_status_selectors, start=1):
            text = combo.currentText()
            symbol: str = symbols.get(text, "❓")
            output.append(f"S{i:02}{symbol}")

        final_output: sys.LiteralString = " ".join(output)
        self.output_area.setPlainText(final_output)
        pyperclip.copy(final_output)

        # Create the message box
        msg = QMessageBox(self)
        msg.setIcon(QMessageBox.Icon.Information)
        msg.setWindowTitle("Copied")
        msg.setText("✅ Tracker copied to clipboard!")

        # Show the message box
        msg.show()

        # Set a timer to close it after 1 seconds
        QTimer.singleShot(1000, msg.close)

        # Clear the output area after 1 second
        QTimer.singleShot(1000, lambda: self.output_area.clear())

    def apply_window_style(self) -> None:
        """
        Applies the appropriate window style based on the Windows version.
        """
        windows_build: int = sys.getwindowsversion().build
        is_windows_11: bool = windows_build >= 22000

        if is_windows_11:
            self.setAttribute(Qt.WidgetAttribute.WA_TranslucentBackground)
            self.setStyleSheet(Styles.WIN11)
            Blur(self.winId())
        else:
            Styles.WIN10

    def keyPressEvent(self, event) -> None:
        # Neovim style: 'h' for prev, 'l' for next
        text = event.text()
        if text == "l":
            if self.current_page < self.total_pages - 1:
                self.next_page()
        elif text == "h":
            if self.current_page > 0:
                self.prev_page()
        elif event.key() in (Qt.Key.Key_Return, Qt.Key.Key_Enter):
            self.generate_tracker()
        elif text == self.KEY_ESC:
            self.close()
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
                self.generate_tracker()
                return True
        return super().eventFilter(obj, event)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = SeasonTracker()
    window.show()
    sys.exit(app.exec())
