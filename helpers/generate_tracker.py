# Build-In Modules
import sys

# Copy to Clipboard
import pyperclip

# PyQt6 Modules
from PyQt6.QtCore import QTimer
from PyQt6.QtWidgets import QMessageBox


def generate_tracker(self) -> None:
    # Get status options from settings (e.g., ["📕 To Watch", "📖 Watching", "📗 Finished"])
    options: list[str] = self.settings.value(
        "status_options",
        ["📕 To Watch", "📖 Watching", "📗 Finished"],
        type=list,
    )
    # Extract emojis from each option (first character)
    emojis = [opt.strip()[0] if opt.strip() else "❓" for opt in options]

    output = []
    for i, combo in enumerate(self.all_status_selectors, start=1):
        text = combo.currentText()
        # Find the emoji for the selected status option
        symbol = "❓"
        for idx, opt in enumerate(options):
            if text == opt:
                symbol = emojis[idx]
                break
        # Add episode number if status is '📖 Watching' and property is set
        episode = combo.property("current_episode")
        if text == options[1] and episode:
            output.append(f"S{i:02}{symbol}E{int(episode):02}")
        else:
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
