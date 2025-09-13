class Styles:
    SEASON_SPIN = """
        QSpinBox {
            background-color: rgba(255, 255, 255, 0.04);
            color: rgba(255, 255, 255, 0.9);
            font-size: 14px;
            font-weight: 700;
            font-style: normal;
            font-family: 'Trebuchet MS', 'Lucida Sans Unicode', 'Lucida Grande', 'Lucida Sans', Arial, sans-serif;
            padding: 2px;
            border: none;
            border-radius: 2px;
            border: 2px solid transparent;
        }

        QSpinBox:focus {
            background-color: #222;
            border-bottom: 2px solid #0078d7;
            border-right: 2px solid #0078d7;
            font-style: unset;
        }

        QSpinBox:disabled {
            background-color: #444;
            color: #d3d3d3;
        }
    """
    SETTINGS_BUTTON = """
        QPushButton {
            background-color: rgba(255, 255, 255, 0.04);
            font-size: 14px;
            font-weight: bold;
            font-family: system-ui, -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Oxygen, Ubuntu, Cantarell, 'Open Sans', 'Helvetica Neue', sans-serif;
            padding: 4px;
            border: none;
            border-radius: 4px;
            border: 2px solid transparent;
        }

        QPushButton:hover {
            background-color: rgba(255, 255, 255, 0.08);
            color: rgba(238, 229, 177, 0.9);
            border-bottom: 2px solid #0078d7;
        }

        QPushButton:pressed {
            background-color: rgba(255, 255, 255, 0.40);
            color: rgba(238, 229, 177, 0.80);
            border-bottom: 2px solid #2aad6c;
        }
    """
    SAVE_BUTTON = """
        QPushButton {
            background-color: rgba(255, 255, 255, 0.04);
            font-size: 14px;
            font-weight: bold;
            font-family: system-ui, -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Oxygen, Ubuntu, Cantarell, 'Open Sans', 'Helvetica Neue', sans-serif;
            padding: 4px;
            border: none;
            border-radius: 4px;
            border: 2px solid transparent;
        }

        QPushButton:hover {
            background-color: rgba(255, 255, 255, 0.08);
            color: rgba(114, 255, 122, 0.90);
            border-bottom: 2px solid #12d700;
        }

        QPushButton:pressed {
            background-color: rgba(255, 255, 255, 0.40);
            color: rgba(0, 255, 13, 0.90);
            border-bottom: 2px solid #2aad6c;
        }
    """
    CANCEL_BUTTON = """
        QPushButton {
            background-color: rgba(255, 255, 255, 0.04);
            font-size: 14px;
            font-weight: bold;
            font-family: system-ui, -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Oxygen, Ubuntu, Cantarell, 'Open Sans', 'Helvetica Neue', sans-serif;
            padding: 4px;
            border: none;
            border-radius: 4px;
            border: 2px solid transparent;
        }

        QPushButton:hover {
            background-color: rgba(255, 255, 255, 0.08);
            color: rgba(255, 109, 109, 0.90);
            border-bottom: 2px solid #d70000;
        }

        QPushButton:pressed {
            background-color: rgba(255, 255, 255, 0.40);
            color: rgba(255, 0, 0, 0.90);
            border-bottom: 2px solid #ad2a2a;
        }
    """
    HELP_BUTTON = """
        QPushButton {
            background-color: rgba(255, 255, 255, 0.04);
            font-size: 14px;
            font-weight: bold;
            font-family: system-ui, -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Oxygen, Ubuntu, Cantarell, 'Open Sans', 'Helvetica Neue', sans-serif;
            padding: 4px;
            border: none;
            border-radius: 4px;
            border: 2px solid transparent;
        }

        QPushButton:hover {
            background-color: rgba(255, 255, 255, 0.08);
            color: rgba(104, 164, 255, 0.90);
            border-bottom: 2px solid #0078d7;
        }

        QPushButton:pressed {
            background-color: rgba(255, 255, 255, 0.40);
            color: rgba(0, 102, 255, 0.90);
            border-bottom: 2px solid #0032d7;
        }
    """
    GROUP_BOX = """
        QGroupBox {
            font-family: 'Trebuchet MS', 'Lucida Sans Unicode', 'Lucida Grande', 'Lucida Sans', Arial, sans-serif;
            font-size: 12qpx;
            font-weight: 700;
            font-style: italic;
        }
    """
    OUTPUT_AREA = """
        QTextEdit {
            background-color: rgba(255, 255, 255, 0.04);
            color: rgba(255, 255, 255, 0.9);
            font-size: 14px;
            font-weight: 700;
            font-style: normal;
            font-family: 'Trebuchet MS', 'Lucida Sans Unicode', 'Lucida Grande', 'Lucida Sans', Arial, sans-serif;
            padding: 4px;
            border: none;
            border-radius: 4px;
            border: 2px solid transparent;
        }

        QTextEdit:focus {
            background-color: #222;
            border-bottom: 2px solid #0078d7;
            border-right: 2px solid #0078d7;
            font-style: unset;
        }

        QTextEdit:disabled {
            background-color: #444;
            color: #d3d3d3;
        }
    """
    COMBO = """
        QComboBox {
            background-color: rgba(255, 255, 255, 0.04);
            color: rgba(255, 255, 255, 0.9);
            font-size: 14px;
            font-weight: 700;
            font-style: normal;
            font-family: 'Trebuchet MS', 'Lucida Sans Unicode', 'Lucida Grande', 'Lucida Sans', Arial, sans-serif;
            padding: 2px;
            border: none;
            border-radius: 2px;
            border: 2px solid transparent;
        }

        QComboBox:focus {
            background-color: #222;
            border-bottom: 2px solid #0078d7;
            border-right: 2px solid #0078d7;
            font-style: unset;
        }

        QComboBox:disabled {
            background-color: #444;
            color: #d3d3d3;
        }
    """
    LINE_EDIT = """
        QLineEdit {
            background-color: rgba(255, 255, 255, 0.04);
            color: rgba(255, 255, 255, 0.9);
            font-size: 14px;
            font-weight: 700;
            font-style: normal;
            font-family: 'Trebuchet MS', 'Lucida Sans Unicode', 'Lucida Grande', 'Lucida Sans', Arial, sans-serif;
            padding: 4px;
            border: none;
            border-radius: 4px;
            border: 2px solid transparent;
        }

        QLineEdit:focus {
            background-color: #222;
            border-bottom: 2px solid #0078d7;
            border-right: 2px solid #0078d7;
            font-style: unset;
        }

        QLineEdit:disabled {
            background-color: #444;
            color: #d3d3d3;
        }
    """
    WIN11 = """
        QLabel {
            font-size: 14px;
            font-weight: 700;
            font-style: normal;
        }
        QWidget#options_container {
            background-color: rgb(254, 255, 255);
            border-radius: 5px;
            padding: -1px;
            border: 0px solid rgba(0, 0, 0, 0.2);
        }
    """
    WIN10 = """
        QLabel {
            color: #ffffff;
            font-size: 14px;
            font-weight: 700;
            font-style: normal;
        }
        QWidget {
            background-color: rgb(31, 39, 56);
        }
    """
