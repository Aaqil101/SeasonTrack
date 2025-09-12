# Build-In Modules
import os
import random
import sys
from pathlib import Path

# PyQt6 Modules
from PyQt6.QtCore import Qt
from PyQt6.QtWidgets import (
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

# WinMica for Windows 11 Mica Effect
from winmica import ApplyMica, MicaType

# Helpers Modules
from helpers import Styles, center_on_screen


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

        # --- Page Size ---)
        general_layout.addWidget(QLabel("Seasons per page:"))

        self.page_spin = QSpinBox()
        self.page_spin.setRange(1, 100)
        saved_page_size = self.settings.value("page_size", 12, type=int)
        self.page_spin.setValue(saved_page_size)
        self.page_spin.setStyleSheet(Styles.SEASON_SPIN)
        self.page_spin.setButtonSymbols(QSpinBox.ButtonSymbols.NoButtons)
        general_layout.addWidget(self.page_spin)

        main_layout.addWidget(general_group)

        # --- Window Icon Section ---
        default_icon = str(Path(__file__).parent / "assets" / "WindowIcon.ico")

        saved_icon = self.settings.value("window_icon", default_icon)
        self.icon_edit = QLineEdit()
        self.icon_edit.setText(saved_icon)
        self.icon_edit.setStyleSheet(Styles.LINE_EDIT)

        browse_btn = QPushButton("📁")
        browse_btn.setStyleSheet(Styles.GENERATE_BUTTON)
        browse_btn.setCursor(Qt.CursorShape.PointingHandCursor)
        browse_btn.clicked.connect(self.browse_icon)

        general_layout.addWidget(self.icon_edit)
        general_layout.addWidget(browse_btn)

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
        btn_layout = QHBoxLayout()
        btn_layout.addStretch()

        save_btn = QPushButton("Save")
        save_btn.setStyleSheet(Styles.GENERATE_BUTTON)

        cancel_btn = QPushButton("Cancel")
        cancel_btn.setStyleSheet(Styles.SETTINGS_BUTTON)

        btn_layout.addWidget(save_btn)
        btn_layout.addWidget(cancel_btn)

        main_layout.addLayout(btn_layout)

        # Connect buttons
        save_btn.clicked.connect(self.save_settings)
        cancel_btn.clicked.connect(self.reject)

        self.apply_window_style()
        center_on_screen(self)

    def apply_window_style(self) -> None:
        """
        Applies the appropriate window style based on the Windows version.
        """
        windows_build: int = sys.getwindowsversion().build
        is_windows_11: bool = windows_build >= 22000

        if is_windows_11:
            self.setAttribute(Qt.WidgetAttribute.WA_TranslucentBackground)
            hwnd = int(self.winId())
            # Alternate between MICA and MICA_ALT each launch
            mica_type: MicaType = random.choice([MicaType.MICA, MicaType.MICA_ALT])
            ApplyMica(hwnd, mica_type)
            self.setStyleSheet(Styles.WIN11)
        else:
            self.setStyleSheet(Styles.WIN10)

    def save_settings(self) -> None:
        self.settings.setValue("default_season_count", self.default_spin.value())

        options = [
            edit.text().strip() for edit in self.option_edits if edit.text().strip()
        ]
        self.settings.setValue("status_options", options)

        self.settings.setValue("window_icon", self.icon_edit.text().strip())

        self.settings.setValue("page_size", self.page_spin.value())

        self.accept()

    def browse_icon(self) -> None:
        file, _ = QFileDialog.getOpenFileName(
            self, "Choose Icon", "", "Icon Files (*.ico *.png)"
        )
        if file:
            self.icon_edit.setText(file)
