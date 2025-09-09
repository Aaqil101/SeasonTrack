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
    PREV_BUTTON = """
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
            color: rgba(187, 253, 190, 0.80);
            border-bottom: 2px solid #0078d7;
        }

        QPushButton:pressed {
            background-color: rgba(255, 255, 255, 0.40);
            color: rgba(0, 255, 13, 0.80);
            border-bottom: 2px solid #2aad6c;
        }

        QPushButton:focus {
            background-color: #222;
            border-bottom: 2px solid #0078d7;
            border-right: 2px solid #0078d7;
            font-style: unset;
        }
    """
    NEXT_BUTTON = """
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
            color: rgba(187, 253, 190, 0.80);
            border-bottom: 2px solid #0078d7;
        }

        QPushButton:pressed {
            background-color: rgba(255, 255, 255, 0.40);
            color: rgba(0, 255, 13, 0.80);
            border-bottom: 2px solid #2aad6c;
        }

        QPushButton:focus {
            background-color: #222;
            border-bottom: 2px solid #0078d7;
            border-right: 2px solid #0078d7;
            font-style: unset;
        }
    """
    GENERATE_BUTTON = """
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
            color: rgba(187, 253, 190, 0.80);
            border-bottom: 2px solid #0078d7;
        }

        QPushButton:pressed {
            background-color: rgba(255, 255, 255, 0.40);
            color: rgba(0, 255, 13, 0.80);
            border-bottom: 2px solid #2aad6c;
        }

        QPushButton:focus {
            background-color: #222;
            border-bottom: 2px solid #0078d7;
            border-right: 2px solid #0078d7;
            font-style: unset;
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
            font-size: 14px;
            font-weight: 700;
            font-style: normal;
        }
        QWidget {
            background-color: rgb(31, 39, 56);
        }
    """
