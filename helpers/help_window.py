# PyQt6 Modules
from PyQt6.QtCore import Qt, QUrl
from PyQt6.QtGui import QDesktopServices
from PyQt6.QtWidgets import QDialog, QHBoxLayout, QLabel, QPushButton, QVBoxLayout

# Helpers Modules
from helpers.apply_window_style import apply_window_style
from helpers.center import center_on_screen
from helpers.styles import Styles


class HelpDialog(QDialog):
    def __init__(self, settings, parent=None) -> None:
        super().__init__(parent)
        self.setWindowTitle("Help & Shortcuts")
        self.setFixedSize(400, 300)
        self.settings = settings

        layout = QVBoxLayout(self)

        # Shortcuts section as dark-themed HTML table
        shortcuts_table = """
            <table style="border-collapse: collapse; width: 100%; font-family: Arial, sans-serif; color: #ffffff;">
            <tr>
                <th style="background-color: #2c2c2c; padding: 6px; text-align: left;">Window</th>
                <th style="background-color: #3d3d3d; padding: 6px; text-align: left;">Keyboard Shortcuts / Actions</th>
            </tr>
            <tr>
                <td style="background-color: #1e1e1e; padding: 4px;">Main Window</td>
                <td style="background-color: #252525; padding: 4px;">
                    Esc → Close window<br>
                    Alt+P → Previous page<br>
                    Alt+N → Next page<br>
                    Enter or Alt+G → Generate Tracker<br>
                    F1 or Alt+H → Open Help<br>
                    F2 or Alt+S → Open Settings
                </td>
            </tr>
            <tr>
                <td style="background-color: #1e1e1e; padding: 4px;">Settings Window</td>
                <td style="background-color: #252525; padding: 4px;">
                    Esc or Alt+C → Close window<br>
                    Alt+S → Save Settings<br>
                    Alt+B → Browse Icon
                </td>
            </tr>
            <tr>
                <td style="background-color: #1e1e1e; padding: 4px;">Help Window</td>
                <td style="background-color: #252525; padding: 4px;">
                    Alt+R → Open ReadMe<br>
                    Esc or Alt+C → Close window
                </td>
            </tr>
            </table>
        """

        shortcuts_label = QLabel(shortcuts_table)
        shortcuts_label.setTextFormat(Qt.TextFormat.RichText)
        shortcuts_label.setWordWrap(True)
        layout.addWidget(shortcuts_label)

        button_layout = QHBoxLayout()

        # README link
        readme_button = QPushButton("📖 &ReadMe")
        readme_button.setCursor(Qt.CursorShape.PointingHandCursor)
        readme_button.setFocusPolicy(Qt.FocusPolicy.NoFocus)
        readme_button.setStyleSheet(Styles.HELP_BUTTON)
        readme_button.clicked.connect(self.open_readme)
        layout.addWidget(readme_button)

        # Close button
        close_button = QPushButton("❌ &Close")
        close_button.setCursor(Qt.CursorShape.PointingHandCursor)
        close_button.setFocusPolicy(Qt.FocusPolicy.NoFocus)
        close_button.setStyleSheet(Styles.CANCEL_BUTTON)
        close_button.clicked.connect(self.close)

        button_layout.addWidget(readme_button)
        button_layout.addWidget(close_button)
        button_layout.setSpacing(4)

        layout.addLayout(button_layout)

        apply_window_style(self)
        center_on_screen(self)

    def open_readme(self) -> None:
        # Adjust if README is hosted on GitHub
        url = QUrl(
            "https://github.com/Aaqil101/SeasonTrack?tab=readme-ov-file#-season-tracker"
        )
        QDesktopServices.openUrl(url)
