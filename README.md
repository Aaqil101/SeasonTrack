# 🎬 Season Tracker

[![License: GPL-3.0](https://img.shields.io/badge/License-GPL-orange.svg)](LICENSE)
[![Core README](https://img.shields.io/badge/Core-README-blue)](https://github.com/Aaqil101/SeasonTrack/blob/master/README.md)
[![Python](https://img.shields.io/badge/Python-3.13%2B-yellow)](https://www.python.org/)
[![GitHub stars](https://img.shields.io/github/stars/Aaqil101/WiFi-Center.svg)](https://github.com/Aaqil101/SeasonTrack/stargazers)

A lightweight **[PyQt6](https://doc.qt.io/qtforpython-6/) desktop app** for tracking TV show seasons with a clean interface, customizable statuses, and clipboard integration.
Easily mark seasons as **📕 To Watch**, **📖 Watching**, or **📗 Finished** — and generate a compact progress string in one click.

![App Screenshot Placeholder](assets/screenshot.png) <!-- Replace with real screenshot -->

> **Note:** If you want the command-line version of this software click here: [Season Tracker CLI](https://github.com/Aaqil101/SeasonTrack/tree/master/cli)

## ✨ Features

-   📺 **Track TV Show Seasons** — Manage up to 100 seasons at once.
-   🔄 **Paging Support** — Display seasons in customizable page sizes.
-   ⚙️ **Settings Dialog** —
    -   Default number of seasons
    -   Seasons per page
    -   Custom status options (emojis + text)
    -   Custom window icon
-   🪟 **Windows 10/11 Styling** — Mica effect on Windows 11, dark themed styles on Windows 10.
-   ⌨️ **Keyboard Shortcuts**
    | Window | Keyboard Shortcuts / Actions |
    |-----------------|----------------------------------------------------------------------------------------------------------------------------------|
    | Main Window | Esc → Close window<br>Alt+P → Previous page<br>Alt+N → Next page<br>Enter or Alt+G → Generate Tracker<br>F1 or Alt+H → Open Help<br>F2 or Alt+S → Open Settings |
    | Settings Window | Esc or Alt+C → Close window<br>Alt+S → Save Settings<br>Alt+B → Browse Icon |
    | Help Window | Alt+R → Open ReadMe<br>Esc or Alt+C → Close window |
-   📋 **Clipboard Integration** — One-click generate copies tracker output to clipboard.
-   ✅ **Quick Feedback** — Temporary toast-like popup confirms when tracker is copied.

## 🚀 Getting Started

### 1. Clone the repository

```bash
git clone https://github.com/Aaqil101/SeasonTrack.git
cd SeasonTrack
```

### 2. Install dependencies

```bash
pip install -r requirements.txt
```

### 3. Run the app

```bash
python main.py
```

## ⚙️ Settings Overview

-   **Default Number of Seasons** — Preload a chosen count on startup.
-   **Seasons Per Page** — Controls how many selectors show per page.
-   **Status Options** — Customize labels and emojis for tracking (e.g. 🎯, ⏳, ✅).
-   **Window Icon** — Choose a custom `.ico` or `.png` file.
-   **Choose Mica Mode** — Set window background style:
    -   🎲 **Random** (default) — Pick randomly on startup.
    -   🌌 **Mica** — Use the standard Mica effect.
    -   🌓 **Mica Alt** — Use the alternative Mica effect.
-   **Keyboard Shortcuts** — Quickly navigate with Alt keys or custom hotkeys (see Help ❓).

All settings are stored in:

```
%APPDATA%\SeasonTrack\settings.ini
```

## 🖼️ Example Output

If you tracked **5 seasons** as follows:

-   S01 📗 Finished
-   S02 📖 Watching
-   S03 📕 To Watch
-   S04 📖 Watching
-   S05 📗 Finished

The generated output will be:

```
S01📗 S02📖 S03📕 S04📖 S05📗
```

✔️ Copied directly to your clipboard!

## 📷 Screenshots

<table>
  <tr>
    <td align="center" style="padding:10px;">
      <div style="border-radius:12px; box-shadow:0 4px 10px rgba(0,0,0,0.3); padding:8px; background:#1e1e1e; color:white; width:410px;">
        <img src="https://github.com/Aaqil101/SeasonTrack/blob/master/screenshots/main_window.png" width="600" style="border-radius:8px;"/><br/>
        <b>Main Window</b><br/>
        <!-- <a href="https://example.com" style="color:#61dafb; text-decoration:none;">🔗 Link</a> -->
      </div>
    </td>
    <td align="center" style="padding:10px;">
      <div style="border-radius:12px; box-shadow:0 4px 10px rgba(0,0,0,0.3); padding:8px; background:#1e1e1e; color:white; width:410px;">
        <img src="https://github.com/Aaqil101/SeasonTrack/blob/master/screenshots/settings_window.png" width="600" style="border-radius:8px;"/><br/>
        <b>Settings Window</b><br/>
      </div>
    </td>
  </tr>
  <tr>
    <td align="center" style="padding:10px;">
      <div style="border-radius:12px; box-shadow:0 4px 10px rgba(0,0,0,0.3); padding:8px; background:#1e1e1e; color:white; width:410px;">
        <img src="https://github.com/Aaqil101/SeasonTrack/blob/master/screenshots/output_window.png" width="600" style="border-radius:8px;"/><br/>
        <b>Output Window</b><br/>
      </div>
    </td>
    <td align="center" style="padding:10px;">
      <div style="border-radius:12px; box-shadow:0 4px 10px rgba(0,0,0,0.3); padding:8px; background:#1e1e1e; color:white; width:410px;">
        <img src="https://github.com/Aaqil101/SeasonTrack/blob/master/screenshots/help_window.png" width="600" style="border-radius:8px;"/><br/>
        <b>Help Window</b><br/>
      </div>
    </td>
  </tr>
</table>

## Build Executable

To build the SeasonTrack [one file](https://pyinstaller.org/en/stable/usage.html#cmdoption-F) executable, use:

```ps1
.\compilers\onefile_build.ps1
```

To build the SeasonTrack [one directory](https://pyinstaller.org/en/stable/usage.html#cmdoption-D) executable, use:

```ps1
.\compilers\onedir_build.ps1
```

> **Note:** You must be in the SeasonTrack directory for this to work; **please do not** enter the compilers directory.

## Icon Attribution

<a href="https://www.freepik.com/icon/video_15485046#fromView=search&page=1&position=5&uuid=6535ecfa-42af-498c-8283-cf1116c637f7">App Icon by pocike</a>

<a href="https://www.freepik.com/icon/check_5253725#fromView=image_search_similar&page=1&position=3&uuid=5f4c3af7-c745-4ec1-abfd-842ccf406f01">Window Icon by Rizki Ahmad Fauzi</a>

[Windows Installer Icon by MindsEyeTHPS](https://logos.fandom.com/wiki/Windows_Installer?file=Windows_Installer_icon_%28Windows_11%29.png)

## 📜 License

This project is licensed under the GPL-3.0 License — see the [LICENSE](https://github.com/Aaqil101/SeasonTrack/blob/master/LICENSE) file for details.
