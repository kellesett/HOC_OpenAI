import os
import cv2 as cv
from packages import Window
from config_data import *


def open_window(window_path: str, window_name: str, width: int, height: int) -> None:
    os.startfile(window_path)

    opened_w = Window(window_name)
    img = opened_w.get_screenshot()
    cv.imshow('Test', img)


if __name__ == '__main__':
    open_window(W_PATH, W_NAME, W_WIDTH, W_HEIGHT)
