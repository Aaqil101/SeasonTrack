# Build-In Modules
import random
import sys

# PyQt6 Modules
from PyQt6.QtCore import Qt

# WinMica for Windows 11 Mica Effect
from winmica import ApplyMica, MicaType

# Helpers Modules
from helpers.styles import Styles


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
