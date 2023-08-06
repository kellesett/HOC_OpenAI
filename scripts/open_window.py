import os
import cv2 as cv
import numpy as np
from time import sleep
from win32gui import SetForegroundWindow, SetWindowPos, GetWindowRect
from win32con import HWND_TOP, SWP_SHOWWINDOW
from packages.window_capturing import Window
from packages.console_design import system_message
from config_data.config import *


def open_window(window_path: str, window_name: str, width: int, height: int) -> None:
    opened_w = Window(window_name, width, height, mode='O')
    if opened_w.hwnd is None:
        os.startfile(window_path)

    system_message('Opening in process...')
    while opened_w.hwnd is None:
        sleep(.1)
        opened_w = Window(window_name, width, height, mode='O')

    img = opened_w.get_screenshot()
    while np.array_equal(EMPTY, img):
        sleep(1)
        img = opened_w.get_screenshot()

    SetForegroundWindow(opened_w.hwnd)
    while GetWindowRect(opened_w.hwnd) != (0, 0, W_WIDTH, W_HEIGHT):
        sleep(1)
        SetWindowPos(opened_w.hwnd, HWND_TOP, 0, 0, W_WIDTH, W_HEIGHT, SWP_SHOWWINDOW)
    system_message('Opening completed.')


if __name__ == '__main__':
    open_window(W_PATH, W_NAME, W_WIDTH, W_HEIGHT)
