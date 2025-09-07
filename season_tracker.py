# In-Built Modules
import msvcrt
import sys
import time
from typing import List, Literal, LiteralString

# External Modules
import pyperclip
from colorama import Fore, init


def main() -> None:
    init(autoreset=True)  # Initialize colorama
    type_print("=== Season Tracker ===", 0.01)

    while True:
        num_seasons_input: str = type_input("How many seasons? ", 0.01, Fore.YELLOW)
        if num_seasons_input.isdigit() and int(num_seasons_input) > 0:
            num_seasons = int(num_seasons_input)
            break
        else:
            type_print("Please enter a valid positive number.", 0.01, Fore.RED)

    type_print(
        "\n👉 Tip: You can enter all statuses at once (e.g., 112 for 3 seasons)\n"
        "1 = Finished ✔️\n"
        "2 = To Watch ❌\n"
        "3 = Watching 🚫\n",
        0.005,
        Fore.MAGENTA,
    )

    # Get multiple numeric choices at once
    choices: List[str] = get_multiple_numeric_input(
        f"Enter statuses (length {num_seasons}): "
    )

    symbols: dict[str, str] = {
        "1": "✔️",  # Finished
        "2": "❌",  # To Watch
        "3": "🚫",  # Watching
    }

    output = []
    for i in range(1, num_seasons + 1):
        if i - 1 < len(choices):
            # Use pre-entered choice (command line or all-at-once input)
            choice: str = choices[i - 1]
            if choice not in symbols:
                choice = "2"  # default to To Watch ❌ if invalid
        else:
            # Fallback to interactive numeric-only input
            choice: str = get_numeric_input(f"Season {i:02} -> ")

        symbol: str = symbols.get(choice, "❌")
        output.append(f"S{i:02}{symbol}")

    final_output: LiteralString = " ".join(output)

    # Print and copy to clipboard
    pyperclip.copy(final_output)
    type_print("✅ Copied to clipboard!", 0.01, Fore.GREEN)


def get_numeric_input(prompt: str, valid_choices=("1", "2", "3")) -> str:
    print(Fore.YELLOW + prompt + Fore.RESET, end="", flush=True)
    choice: Literal[""] = ""

    while True:
        key: str = msvcrt.getwch()

        if key in valid_choices:
            print(Fore.CYAN + key + Fore.RESET, end="", flush=True)
            choice = key
            break
        elif key == "\x08":  # Backspace
            if choice:
                choice = ""
                print("\b \b", end="", flush=True)  # erase the key from screen
        elif key == "\r":  # Enter key with no input, ignore
            continue
        else:
            # ignore any other keypress
            continue

    print()  # move to next line
    return choice


def get_multiple_numeric_input(
    prompt: str, valid_choices=("1", "2", "3"), color=Fore.YELLOW
) -> List[str]:
    print(color + prompt + Fore.RESET, end="", flush=True)
    choices: List[str] = []

    while True:
        key: str = msvcrt.getwch()
        if key in valid_choices:
            print(
                Fore.CYAN + key + Fore.RESET, end="", flush=True
            )  # typed keys in cyan
            choices.append(key)
        elif key == "\r":  # Enter key finishes input
            break
        elif key == "\x08":  # Backspace
            if choices:
                choices.pop()
                # Move cursor back, overwrite with space, move back again
                print("\b \b", end="", flush=True)
        else:
            # ignore any other key
            continue
    print()  # move to next line
    return choices


def type_print(text: str, delay: float = 0.05, color=Fore.CYAN) -> None:
    for char in text:
        sys.stdout.write(color + char)
        sys.stdout.flush()
        time.sleep(delay)
    print()  # for newline


def type_input(prompt: str, delay: float = 0.05, color=Fore.CYAN) -> str:
    for char in prompt:
        sys.stdout.write(color + char)
        sys.stdout.flush()
        time.sleep(delay)
    return input()  # Wait for user input after animation


if __name__ == "__main__":
    main()
