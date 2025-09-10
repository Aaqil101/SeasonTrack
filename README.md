# SeasonTrack

[![License: GPL-3.0](https://img.shields.io/badge/License-GPL-orange.svg)](LICENSE)
[![Core README](https://img.shields.io/badge/Core-README-blue)](https://github.com/Aaqil101/SeasonTrack/blob/master/README.md)
[![Python](https://img.shields.io/badge/Python-3.13%2B-yellow)](https://www.python.org/)
[![GitHub stars](https://img.shields.io/github/stars/Aaqil101/WiFi-Center.svg)](https://github.com/Aaqil101/SeasonTrack/stargazers)

🎬 A simple [Python](https://www.python.org/) software to track TV show seasons with status markers:

-   📕 To Watch
-   📖 Watching
-   📗 Finished

> **Note:** If you want the command-line version of this software click here: [Season Tracker CLI](https://github.com/Aaqil101/SeasonTrack/tree/master/cli)

## Build Executable (with Icon)

To build the SeasonTrack executable with the app icon, use:

```ps1
pyinstaller --clean -n SeasonTracker \
    -F --windowed \
    --icon=assets/AppIcon.ico \
    --add-data "assets;assets" \
    --add-data "helpers;helpers" \
    season_tracker.py
```

## Icon Attribution

<a href="https://www.freepik.com/icon/video_15485046#fromView=search&page=1&position=5&uuid=6535ecfa-42af-498c-8283-cf1116c637f7">App Icon by pocike</a>

<a href="https://www.freepik.com/icon/check_5253725#fromView=image_search_similar&page=1&position=3&uuid=5f4c3af7-c745-4ec1-abfd-842ccf406f01">Window Icon by Rizki Ahmad Fauzi</a>

[Windows Installer Icon by MindsEyeTHPS](https://logos.fandom.com/wiki/Windows_Installer?file=Windows_Installer_icon_%28Windows_11%29.png)
