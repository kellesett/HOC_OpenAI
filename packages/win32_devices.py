import win32con
import win32api
from time import sleep
from abc import ABC
import cv2 as cv
from packages.window_capturing import Window


MOUSEEVENT_SCALE = 65535.0
W = 1920
H = 1080


class Mouse(ABC):
    @classmethod
    def LeftClick(cls, x, y):
        cls.MoveMouse(x, y)
        win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN, 0, 0)
        sleep(.1)
        win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP, 0, 0)
        # print('Left Click')

    @classmethod
    def RightClick(cls, x, y):
        cls.MoveMouse(x, y)
        win32api.mouse_event(win32con.MOUSEEVENTF_RIGHTDOWN, 0, 0)
        sleep(.1)
        win32api.mouse_event(win32con.MOUSEEVENTF_RIGHTUP, 0, 0)
        # print('Left Click')

    @classmethod
    def MoveMouse(cls, x, y):
        # win32api.SetCursorPos((x, y))
        win32api.mouse_event(
            win32con.MOUSEEVENTF_MOVE | win32con.MOUSEEVENTF_ABSOLUTE,
            int(x / W * MOUSEEVENT_SCALE), int(y / H * MOUSEEVENT_SCALE)
        )

    @classmethod
    def GetCursorPos(cls):
        print(', '.join(map(str, win32api.GetCursorPos())))
        exit(0)


class Keyboard(ABC):
    pass


class ClickArea:
    x_cord = 0
    y_cord = 0
    possibility = 0

    def __init__(self, area_img, window: Window, non_repudiation=False, test_mode=False, moving_button=False):
        threshold = 0.9
        screen_img = window.get_screenshot()

        check_result = cv.matchTemplate(screen_img, area_img, cv.TM_CCOEFF_NORMED)
        sleep(.1)
        screen_img = window.get_screenshot()
        result = cv.matchTemplate(screen_img, area_img, cv.TM_CCOEFF_NORMED)

        ch_min_val, ch_max_val, ch_min_loc, ch_max_loc = cv.minMaxLoc(check_result)
        min_val, max_val, min_loc, max_loc = cv.minMaxLoc(result)

        while (non_repudiation and max_val < threshold) or (moving_button and max_loc != ch_max_loc):
            sleep(.1)
            screen_img = window.get_screenshot()
            result = cv.matchTemplate(screen_img, area_img, cv.TM_CCOEFF_NORMED)
            ch_max_loc = max_loc
            min_val, max_val, min_loc, max_loc = cv.minMaxLoc(result)
        self.possibility = max_val

        width = area_img.shape[0]
        height = area_img.shape[1]

        x = max_loc[0] + height // 2
        y = max_loc[1] + width // 2
        self.x = x
        self.y = y

        if test_mode:
            marked_img = cv.drawMarker(
                screen_img, (x, y), color=(0, 0, 255), markerType=cv.MARKER_CROSS, markerSize=40, thickness=2
            )
            cv.imshow('Test Window', marked_img)
            cv.waitKey()

    def Click(self):
        Mouse.LeftClick(self.x, self.y)
