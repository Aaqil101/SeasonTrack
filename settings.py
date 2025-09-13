# Build-In Modules
from pathlib import Path

# PyQt6 Modules
from PyQt6.QtCore import Qt
from PyQt6.QtWidgets import (
    QComboBox,
    QDialog,
    QFileDialog,
    QGridLayout,
    QGroupBox,
    QHBoxLayout,
    QLabel,
    QLineEdit,
    QPushButton,
    QSpinBox,
    QVBoxLayout,
)

# Helpers Modules
from helpers import Styles, apply_window_style, center_on_screen


class SettingsDialog(QDialog):
    def __init__(self, settings, parent=None) -> None:
        super().__init__(parent)
        self.setWindowTitle("Settings")
        self.settings = settings
        self.setFixedSize(400, 400)

        main_layout = QVBoxLayout(self)
        main_layout.setSpacing(15)
        main_layout.setContentsMargins(20, 20, 20, 20)

        # --- General Section ---
        general_group = QGroupBox("General")
        general_group.setStyleSheet(Styles.GROUP_BOX)
        general_layout = QGridLayout()
        general_group.setLayout(general_layout)

        general_layout.addWidget(QLabel("Default number of seasons:"), 0, 0)

        self.default_spin = QSpinBox()
        self.default_spin.setRange(1, 100)
        self.default_spin.setStyleSheet(Styles.SEASON_SPIN)
        self.default_spin.setButtonSymbols(QSpinBox.ButtonSymbols.NoButtons)
        saved_default = self.settings.value("default_season_count", 1, type=int)
        self.default_spin.setValue(saved_default)
        general_layout.addWidget(self.default_spin, 0, 1)

        # --- Page Size ---
        general_layout.addWidget(QLabel("Seasons per page:"))

        self.page_spin = QSpinBox()
        self.page_spin.setRange(1, 100)
        saved_page_size = self.settings.value("page_size", 12, type=int)
        self.page_spin.setValue(saved_page_size)
        self.page_spin.setStyleSheet(Styles.SEASON_SPIN)
        self.page_spin.setButtonSymbols(QSpinBox.ButtonSymbols.NoButtons)
        general_layout.addWidget(self.page_spin)

        main_layout.addWidget(general_group)

        # --- Mica Effect ---
        general_layout.addWidget(QLabel("Choose Mica Mode:"))

        self.mica_combo = QComboBox()
        options: list[str] = ["🎲 Random", "🌌 Mica", "🌓 Mica Alt"]
        self.mica_combo.addItems(options)
        self.mica_combo.setCurrentText(options[0])  # "🎲 Random" set default
        self.mica_combo.setStyleSheet(Styles.COMBO)
        self.mica_combo.setCursor(Qt.CursorShape.PointingHandCursor)
        saved_mode = self.settings.value("mica_mode", "🎲 Random")
        index: int = self.mica_combo.findText(saved_mode)
        if index >= 0:
            self.mica_combo.setCurrentIndex(index)

        general_layout.addWidget(self.mica_combo)

        # --- Window Icon Section ---
        default_icon = str(Path(__file__).parent / "assets" / "WindowIcon.ico")

        saved_icon = self.settings.value("window_icon", default_icon)
        self.icon_edit = QLineEdit()
        self.icon_edit.setText(saved_icon)
        self.icon_edit.setStyleSheet(Styles.LINE_EDIT)

        browse_button = QPushButton("📁")
        browse_button.setToolTip("Browse for Icon")
        browse_button.setShortcut("Alt+B")
        browse_button.setStyleSheet(Styles.HELP_BUTTON)
        browse_button.setCursor(Qt.CursorShape.PointingHandCursor)
        browse_button.clicked.connect(self.browse_icon)

        general_layout.addWidget(self.icon_edit)
        general_layout.addWidget(browse_button)

        # --- Status Options Section ---
        status_group = QGroupBox("Status Options")
        status_group.setStyleSheet(Styles.GROUP_BOX)
        status_layout = QGridLayout()
        status_group.setLayout(status_layout)

        default_options: list[str] = [
            "📕 To Watch",
            "📖 Watching",
            "📗 Finished",
        ]
        saved_options = self.settings.value(
            "status_options", default_options, type=list
        )

        self.option_edits = []
        labels: list[str] = ["First Option:", "Second Option:", "Third Option:"]

        for i, label in enumerate(labels):
            status_layout.addWidget(QLabel(label), i, 0)
            edit = QLineEdit()
            edit.setText(saved_options[i] if i < len(saved_options) else "")
            edit.setStyleSheet(Styles.LINE_EDIT)
            status_layout.addWidget(edit, i, 1)
            self.option_edits.append(edit)

        main_layout.addWidget(status_group)

        # --- Buttons ---
        button_layout = QHBoxLayout()
        button_layout.addStretch()

        save_button = QPushButton("&Save")
        save_button.setCursor(Qt.CursorShape.PointingHandCursor)
        save_button.setFocusPolicy(Qt.FocusPolicy.NoFocus)
        save_button.setStyleSheet(Styles.SAVE_BUTTON)

        cancel_button = QPushButton("&Cancel")
        cancel_button.setCursor(Qt.CursorShape.PointingHandCursor)
        cancel_button.setFocusPolicy(Qt.FocusPolicy.NoFocus)
        cancel_button.setStyleSheet(Styles.CANCEL_BUTTON)

        button_layout.addWidget(save_button)
        button_layout.addWidget(cancel_button)
        button_layout.setSpacing(4)

        main_layout.addLayout(button_layout)

        # Connect buttons
        save_button.clicked.connect(self.save_settings)
        cancel_button.clicked.connect(self.reject)

        apply_window_style(self)
        center_on_screen(self)

    def save_settings(self) -> None:
        self.settings.setValue("default_season_count", self.default_spin.value())

        options = [
            edit.text().strip() for edit in self.option_edits if edit.text().strip()
        ]
        self.settings.setValue("status_options", options)

        self.settings.setValue("window_icon", self.icon_edit.text().strip())

        self.settings.setValue("page_size", self.page_spin.value())

        self.settings.setValue("mica_mode", self.mica_combo.currentText())

        self.accept()

    def browse_icon(self) -> None:
        file, _ = QFileDialog.getOpenFileName(
            self, "Choose Icon", "", "Icon Files (*.ico *.png)"
        )
        if file:
            self.icon_edit.setText(file)
