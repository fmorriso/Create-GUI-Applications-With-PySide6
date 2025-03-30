import sys

import PySide6.QtCore
import pyautogui as pg
from PySide6.QtCore import QSize
from PySide6.QtWidgets import QApplication, QWidget

from SimpleWindow import SimpleWindow
from gui_settings import GuiSettings

scaled_settings = GuiSettings(pct = 0.45, multiple_of = 10)
scaled_size = QSize(scaled_settings.screen_width, scaled_settings.screen_height)


def get_python_version() -> str:
    return f'{sys.version_info.major}.{sys.version_info.minor}.{sys.version_info.micro}'


def create_simple_window(title: str, qsz = None) -> None:
    # You need one (and only one) QApplication instance per application.
    # Pass in sys.argv to allow command line arguments for your app.
    # If you know you won't use command line arguments QApplication([]) works too.
    app = QApplication(sys.argv)

    # Create a Qt widget, which will be our window.
    window = SimpleWindow(title, scaled_size)
    window.show()  # IMPORTANT!!!!! Windows are hidden by default.

    # Start the event loop.
    sys.exit(app.exec())

    # Your application won't reach here until you exit and the event
    # loop has stopped.


def main():
    title: str = f'Simple Window using python {get_python_version()}'
    create_simple_window(title)


if __name__ == '__main__':
    msg = f'Python version: {get_python_version()}'
    print(msg)
    print(f'PySide6 version: {PySide6.__version__}')
    print(f'Qt version: {PySide6.QtCore.__version__}')
    print(f'PyAutoGUI version: {pg.__version__}')
    main()
