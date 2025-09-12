# Build-In Modules
import sys

# Copy to Clipboard
import pyperclip

# PyQt6 Modules
from PyQt6.QtCore import QTimer
from PyQt6.QtWidgets import QMessageBox


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
