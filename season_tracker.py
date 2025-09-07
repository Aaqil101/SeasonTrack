# Build-In Modules
import sys

# External Modules
import pyperclip

# PyQt6 Modules
from PyQt6.QtCore import Qt, QTimer
from PyQt6.QtWidgets import (
    QApplication,
    QComboBox,
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
    def __init__(self) -> None:
        super().__init__()
        self.setWindowTitle("Season Tracker")
        self.setFixedSize(400, 400)

        self.initUI()

    def initUI(self) -> None:
        self.layout = QVBoxLayout(self)

        # Season count selector
        season_layout = QHBoxLayout()
        season_layout.addWidget(QLabel("How many seasons?"))
        self.season_spin = QSpinBox()
        self.season_spin.setCursor(Qt.CursorShape.PointingHandCursor)
        self.season_spin.setButtonSymbols(QSpinBox.ButtonSymbols.NoButtons)
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
        self.season_spin.setFixedWidth(30)
        self.season_spin.setRange(1, 100)
        self.season_spin.setValue(1)
        self.season_spin.valueChanged.connect(self.update_season_inputs)
        season_layout.addWidget(self.season_spin)
        self.layout.addLayout(season_layout)

        # Season status selectors
        self.status_layout = QVBoxLayout()
        self.layout.addLayout(self.status_layout)
        self.status_selectors = []
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

    def update_season_inputs(self) -> None:
        # Clear old widgets
        while self.status_layout.count():
            child: QLayoutItem | None = self.status_layout.takeAt(0)
            if child.widget():
                child.widget().deleteLater()
            elif child.layout():
                while child.layout().count():
                    sub_child: QLayoutItem | None = child.layout().takeAt(0)
                    if sub_child.widget():
                        sub_child.widget().deleteLater()
                child.layout().deleteLater()

        self.status_selectors.clear()
        num_seasons: int = self.season_spin.value()

        # Add selectors for each season
        for i in range(1, num_seasons + 1):
            row = QHBoxLayout()
            row.addWidget(QLabel(f"S{i:02}"))
            combo = QComboBox()
            combo.setFixedWidth(110)
            combo.setCursor(Qt.CursorShape.PointingHandCursor)
            combo.setStyleSheet(
                """
                QComboBox {
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
            combo.addItems(["✔️ Finished", "❌ To Watch", "🚫 Watching"])
            combo.setCurrentText("❌ To Watch")  # set default
            row.addWidget(combo)
            self.status_layout.addLayout(row)
            self.status_selectors.append(combo)

    def generate_tracker(self) -> None:
        symbols: dict[str, str] = {
            "✔️ Finished": "✔️",
            "❌ To Watch": "❌",
            "🚫 Watching": "🚫",
        }

        output = []
        for i, combo in enumerate(self.status_selectors, start=1):
            text = combo.currentText()
            symbol: str = symbols.get(text, "❌")
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
