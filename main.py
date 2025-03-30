import sys

import PySide6.QtCore
import pyautogui as pg
from PyQt6.QtCore import QSize
from PySide6.QtWidgets import QApplication, QWidget

from gui_settings import GuiSettings

settings = GuiSettings(pct=0.45, multiple_of=10)

def get_python_version() -> str:
    return f'{sys.version_info.major}.{sys.version_info.minor}.{sys.version_info.micro}'


def create_simple_window(title: str) -> None:
    # You need one (and only one) QApplication instance per application.
    # Pass in sys.argv to allow command line arguments for your app.
    # If you know you won't use command line arguments QApplication([]) works too.
    app = QApplication(sys.argv)

    # Create a Qt widget, which will be our window.
    window = QWidget()
    window.setWindowTitle(f'{title}  ({settings.screen_width} x {settings.screen_height})')
    window.setFixedSize(settings.screen_width, settings.screen_height)
    window.show()  # IMPORTANT!!!!! Windows are hidden by default.

    # Start the event loop.
    app.exec()

    # Your application won't reach here until you exit and the event
    # loop has stopped.


def main():
    create_simple_window('Simple Window')

if __name__ == '__main__':
    msg = f'Python version: {get_python_version()}'
    print(msg)
    print(f'PySide6 version: {PySide6.__version__}')
    print(f'Qt version: {PySide6.QtCore.__version__}')
    print(f'PyAutoGUI version: {pg.__version__}')
    main()