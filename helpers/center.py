# PyQt6 Modules
from PyQt6.QtWidgets import QApplication


def center_on_screen(self) -> None:
    """Centers the window on the current screen."""
    # Get the current screen where the window is
    app_instance = QApplication.instance()
    current_screen = app_instance.screenAt(self.pos()) or app_instance.primaryScreen()

    # Get the geometry of the screen
    screen_geometry = current_screen.availableGeometry()

    # Calculate the center position
    x = (screen_geometry.width() - self.width()) // 2 + screen_geometry.x()
    y = (screen_geometry.height() - self.height()) // 2 + screen_geometry.y()

    # Move the window
    self.move(x, y)
