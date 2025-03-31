from PySide6.QtCore import QSize
from PySide6.QtGui import QFont
from PySide6.QtWidgets import QMainWindow, QPushButton


class MainWindow(QMainWindow):

    def __init__(self, title: str, scaled_size: QSize):
        super().__init__()
        self.setWindowTitle(title)
        self.setFixedSize(scaled_size)
        self.scaled_size = scaled_size

        button_width: int = scaled_size.width() // 8
        button_height: int = scaled_size.height() // 8

        button = QPushButton('Press Me!', self)
        button.setFixedSize(button_width, button_height)
        button.setStyleSheet(self.get_button_color_style())

        font_family: str = self.font().family()
        print(f'{font_family=}')
        font_size: int = self.font().pointSize()
        print(f'{font_size=}')
        button.setFont(QFont(font_family, font_size * 2))

        button.show()
        self.button = button
        self.window_font = self.font()

        self.setCentralWidget(button)


    def get_button_color_style(self) -> str:
        normal_background = 'red'
        hover_background = 'blue'
        pressed_background = 'green'
        font_size = self.font().pointSize() * 8
        return f"""
            QPushButton {{
                background-color: {normal_background}; color: white; border: 2px solid black; 
        border-radius: 5px;      
            }}
            QPushButton:hover {{
                background-color: {hover_background}; color: white; border: 2px solid red;  
        border-radius: 5px;      
            }}
            QPushButton:pressed {{
                background-color: {pressed_background}; color: yellow; border: 2px solid blue;
            }}
        """


    def resizeEvent(self, event):
        super().resizeEvent(event)
        # Reposition the button at (150, 100) when the window resizes
        window_rect = self.geometry()
        print(f'Window rect: {window_rect}')

        # Calculate the position to center the button
        button_width: int = self.scaled_size.width() // 10
        button_height: int = self.scaled_size.height() // 10
        x = (window_rect.width() - button_width) // 2
        y = (window_rect.height() - button_height) // 2
        print(f'X: {x}, Y: {y}')
        self.button.move(x, y)
