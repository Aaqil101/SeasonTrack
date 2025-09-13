import sys

from PyQt6.QtCore import Qt
from PyQt6.QtWidgets import QApplication, QDockWidget, QMainWindow, QTextEdit

app = QApplication(sys.argv)

window = QMainWindow()
window.setWindowTitle("Dockable Panels Example")
window.resize(800, 600)

# Central widget
central = QTextEdit("Main Workspace")
window.setCentralWidget(central)

# Left Dock
dock_left = QDockWidget("Project Panel", window)
dock_left.setWidget(QTextEdit("Projects..."))
dock_left.setAllowedAreas(
    Qt.DockWidgetArea.LeftDockWidgetArea | Qt.DockWidgetArea.RightDockWidgetArea
)
window.addDockWidget(Qt.DockWidgetArea.LeftDockWidgetArea, dock_left)

# Right Dock
dock_right = QDockWidget("Properties Panel", window)
dock_right.setWidget(QTextEdit("Properties..."))
dock_right.setAllowedAreas(
    Qt.DockWidgetArea.LeftDockWidgetArea | Qt.DockWidgetArea.RightDockWidgetArea
)
window.addDockWidget(Qt.DockWidgetArea.RightDockWidgetArea, dock_right)

window.show()
sys.exit(app.exec())
