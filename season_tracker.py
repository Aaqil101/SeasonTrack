# Build-In Modules
import sys

# External Modules
import pyperclip

# PyQt6 Modules
from PyQt6.QtCore import QEvent, Qt, QTimer
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

# Helpers Modules
from helpers import Blur


class SeasonTracker(QWidget):
    PAGE_SIZE = 14
    KEY_ESC = "\x1b"

    def __init__(self) -> None:
        super().__init__()
        self.setWindowTitle("Season Tracker")
        self.setFixedSize(400, 400)

        self.current_page = 0
        self.total_pages = 1
        self.initUI()

    def initUI(self) -> None:
        self.layout = QVBoxLayout(self)

        # Season count selector
        season_layout = QHBoxLayout()
        season_layout.addWidget(QLabel("How many seasons?"))
        self.season_spin = QSpinBox()
        self.season_spin.setCursor(Qt.CursorShape.PointingHandCursor)
        self.season_spin.setButtonSymbols(QSpinBox.ButtonSymbols.NoButtons)
        self.season_spin.installEventFilter(self)
        self.season_spin.setStyleSheet(
            """
            QSpinBox {
                background-color: rgba(255, 255, 255, 0.04);
                color: rgba(255, 255, 255, 0.9);
                font-size: 14px;
                font-weight: 700;
                font-style: normal;
                font-family: 'Trebuchet MS', 'Lucida Sans Unicode', 'Lucida Grande', 'Lucida Sans', Arial, sans-serif;
                padding: 2px;
                border: none;
                border-radius: 2px;
                border: 2px solid transparent;
            }

            QSpinBox:focus {
                background-color: #222;
                border-bottom: 2px solid #0078d7;
                border-right: 2px solid #0078d7;
                font-style: unset;
            }

            QSpinBox:disabled {
                background-color: #444;
                color: #d3d3d3;
            }
            """
        )
        self.season_spin.setFixedWidth(40)
        self.season_spin.setRange(1, 100)
        self.season_spin.setValue(2)
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
        self.prev_button.setStyleSheet(
            """
            QPushButton {
                background-color: rgba(255, 255, 255, 0.04);
                font-size: 14px;
                font-weight: bold;
                font-family: system-ui, -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Oxygen, Ubuntu, Cantarell, 'Open Sans', 'Helvetica Neue', sans-serif;
                padding: 4px;
                border: none;
                border-radius: 4px;
                border: 2px solid transparent;
            }

            QPushButton:hover {
                background-color: rgba(255, 255, 255, 0.08);
                color: rgba(187, 253, 190, 0.80);
                border-bottom: 2px solid #0078d7;
            }

            QPushButton:pressed {
                background-color: rgba(255, 255, 255, 0.40);
                color: rgba(0, 255, 13, 0.80);
                border-bottom: 2px solid #2aad6c;
            }

            QPushButton:focus {
                background-color: #222;
                border-bottom: 2px solid #0078d7;
                border-right: 2px solid #0078d7;
                font-style: unset;
            }
            """
        )
        self.prev_button.clicked.connect(self.prev_page)

        self.next_button = QPushButton("Next")
        self.next_button.setCursor(Qt.CursorShape.PointingHandCursor)
        self.next_button.setFocusPolicy(Qt.FocusPolicy.NoFocus)
        self.next_button.setStyleSheet(
            """
            QPushButton {
                background-color: rgba(255, 255, 255, 0.04);
                font-size: 14px;
                font-weight: bold;
                font-family: system-ui, -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Oxygen, Ubuntu, Cantarell, 'Open Sans', 'Helvetica Neue', sans-serif;
                padding: 4px;
                border: none;
                border-radius: 4px;
                border: 2px solid transparent;
            }

            QPushButton:hover {
                background-color: rgba(255, 255, 255, 0.08);
                color: rgba(187, 253, 190, 0.80);
                border-bottom: 2px solid #0078d7;
            }

            QPushButton:pressed {
                background-color: rgba(255, 255, 255, 0.40);
                color: rgba(0, 255, 13, 0.80);
                border-bottom: 2px solid #2aad6c;
            }

            QPushButton:focus {
                background-color: #222;
                border-bottom: 2px solid #0078d7;
                border-right: 2px solid #0078d7;
                font-style: unset;
            }
            """
        )
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
        self.generate_button.setStyleSheet(
            """
            QPushButton {
                background-color: rgba(255, 255, 255, 0.04);
                font-size: 14px;
                font-weight: bold;
                font-family: system-ui, -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Oxygen, Ubuntu, Cantarell, 'Open Sans', 'Helvetica Neue', sans-serif;
                padding: 4px;
                border: none;
                border-radius: 4px;
                border: 2px solid transparent;
            }

            QPushButton:hover {
                background-color: rgba(255, 255, 255, 0.08);
                color: rgba(187, 253, 190, 0.80);
                border-bottom: 2px solid #0078d7;
            }

            QPushButton:pressed {
                background-color: rgba(255, 255, 255, 0.40);
                color: rgba(0, 255, 13, 0.80);
                border-bottom: 2px solid #2aad6c;
            }

            QPushButton:focus {
                background-color: #222;
                border-bottom: 2px solid #0078d7;
                border-right: 2px solid #0078d7;
                font-style: unset;
            }
            """
        )
        self.generate_button.setCursor(Qt.CursorShape.PointingHandCursor)
        self.generate_button.setFocusPolicy(Qt.FocusPolicy.NoFocus)
        self.generate_button.clicked.connect(self.generate_tracker)
        self.layout.addWidget(self.generate_button)

        # Output area
        self.output_area = QTextEdit()
        self.output_area.setReadOnly(True)
        self.output_area.setPlaceholderText("Your tracker will appear here...")
        self.output_area.setStyleSheet(
            """
            QTextEdit {
                background-color: rgba(255, 255, 255, 0.04);
                color: rgba(255, 255, 255, 0.9);
                font-size: 14px;
                font-weight: 700;
                font-style: normal;
                font-family: 'Trebuchet MS', 'Lucida Sans Unicode', 'Lucida Grande', 'Lucida Sans', Arial, sans-serif;
                padding: 4px;
                border: none;
                border-radius: 4px;
                border: 2px solid transparent;
            }

            QTextEdit:focus {
                background-color: #222;
                border-bottom: 2px solid #0078d7;
                border-right: 2px solid #0078d7;
                font-style: unset;
            }

            QTextEdit:disabled {
                background-color: #444;
                color: #d3d3d3;
            }
            """
        )
        self.output_area.setFocusPolicy(Qt.FocusPolicy.NoFocus)
        self.layout.addWidget(self.output_area)

        self.apply_window_style()
        self.center_on_screen()

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
                options: list[str] = ["▶️ To Watch", "⏸️ Watching", "🎯 Finished"]
                combo.addItems(options)
                combo.setCurrentText(options[0])  # "▶️ To Watch" set default
                combo.setStyleSheet(
                    """
                    QComboBox {
                        background-color: rgba(255, 255, 255, 0.04);
                        color: rgba(255, 255, 255, 0.9);
                        font-size: 14px;
                        font-weight: 700;
                        font-style: normal;
                        font-family: 'Trebuchet MS', 'Lucida Sans Unicode', 'Lucida Grande', 'Lucida Sans', Arial, sans-serif;
                        padding: 2px;
                        border: none;
                        border-radius: 2px;
                        border: 2px solid transparent;
                    }

                    QComboBox:focus {
                        background-color: #222;
                        border-bottom: 2px solid #0078d7;
                        border-right: 2px solid #0078d7;
                        font-style: unset;
                    }

                    QComboBox:disabled {
                        background-color: #444;
                        color: #d3d3d3;
                    }
                    """
                )
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
            "▶️ To Watch": "▶️",
            "⏸️ Watching": "⏸️",
            "🎯 Finished": "🎯",
        }

        output = []
        for i, combo in enumerate(self.all_status_selectors, start=1):
            text = combo.currentText()
            symbol: str = symbols.get(text, "▶️")
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
            self.setStyleSheet(
                """
                QLabel {
                    font-size: 14px;
                    font-weight: 700;
                    font-style: normal;
                }
                QWidget#options_container {
                    background-color: rgba(254, 255, 255, 0.02);
                    border-radius: 5px;
                    padding: -1px;
                    border: 0px solid rgba(0, 0, 0, 0.2);
                }
                """
            )
            Blur(self.winId())
        else:
            """
            QLabel {
                font-size: 14px;
                font-weight: 700;
                font-style: normal;
            }
            QWidget {
                background-color: rgb(31, 39, 56);
            }
            """

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

    def center_on_screen(self) -> None:
        """Centers the window on the current screen."""
        # Get the current screen where the window is
        app_instance = QApplication.instance()
        current_screen = (
            app_instance.screenAt(self.pos()) or app_instance.primaryScreen()
        )

        # Get the geometry of the screen
        screen_geometry = current_screen.availableGeometry()

        # Calculate the center position
        x = (screen_geometry.width() - self.width()) // 2 + screen_geometry.x()
        y = (screen_geometry.height() - self.height()) // 2 + screen_geometry.y()

        # Move the window
        self.move(x, y)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = SeasonTracker()
    window.show()
    sys.exit(app.exec())
