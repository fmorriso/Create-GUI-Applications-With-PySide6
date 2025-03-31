from PySide6.QtCore import QSize
from PySide6.QtWidgets import QWidget


class SimpleWindow(QWidget):
    def __init__(self, title: str, scaled_size: QSize):
        super().__init__()
        self.setWindowTitle(title)
        self.setFixedSize(scaled_size)
