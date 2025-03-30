from typing import ClassVar
import pyautogui
# import pygame as pg


class GuiSettings:
    ONE_TIME_COUNT: ClassVar[int] = 0  # helps with one-time actions

    def __init__(self, pct: float = 0.5):
        """Initialize the game's settings."""
        # Screen settings

        # calculate game size as a percentage of device screen size
        device_width, device_height = pyautogui.size()
        self.screenPct: float = float(pct)

        # ratio to original hard-coded values of 1280 (w) x 720 (h) in the original code
        ratio_height: float = device_height / 720.0
        ratio_width: float = device_width / 1280.0
        if GuiSettings.ONE_TIME_COUNT == 0:
            print(f'ratios: height: {ratio_height:.2f}, width: {ratio_width:.2f}')

        # round scaled width and height to multiple of 100
        scaled_width: int = int((device_width * self.screenPct // 100) * 100)
        scaled_height: int = int((device_height * self.screenPct // 100) * 100)
        if GuiSettings.ONE_TIME_COUNT == 0:
            print(f'scaled width: {scaled_width}, height: {scaled_height}')

        self.screen_width = scaled_width
        self.screen_height = scaled_height

        # self.SCREEN_RECTANGLE = pg.Rect(0, 0, self.screen_width, self.screen_height)

        GuiSettings.ONE_TIME_COUNT += 1
