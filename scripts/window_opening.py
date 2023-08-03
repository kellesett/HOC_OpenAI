import win32api
import win32con
import win32gui
from window_capturing import Window
from os import startfile
from time import sleep
import cv2 as cv


def open_window(window_name, path):
    check_hwnd = win32gui.FindWindow(None, window_name)
    if check_hwnd:
        return

    startfile(path)
    sleep(5)
    open_window(window_name, path)


if __name__ == '__main__':
    open_window('MEmu', 'C:\Microvirt\MEmu\MEmu')

    current_window = Window('MEmu', 1350, 769)
    hwnd = current_window.hwnd
    win32gui.SetWindowPos(hwnd, win32con.HWND_TOP, 0, 0, 1350, 769, win32con.SWP_SHOWWINDOW)

    screen = current_window.get_screenshot()
    template = cv.imread('../images/HOC_icon.png')

    min_val, max_val, min_loc, max_loc = 0, 0, (0, 0), (0, 0)
    while max_val < 0.9:
        result = cv.matchTemplate(screen, template, cv.TM_CCOEFF_NORMED)
        min_val, max_val, min_loc, max_loc = cv.minMaxLoc(result)
        sleep(.1)

    width = template.shape[0]
    height = template.shape[1]

    cv.rectangle(screen, max_loc, (max_loc[0] + width, max_loc[1] + height), color=(0, 255, 0))
    cv.imshow('2', screen)
    cv.waitKey()
