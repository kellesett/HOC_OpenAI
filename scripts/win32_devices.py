import win32gui
import win32con
import win32api
from time import sleep
from abc import ABC


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
        print('Left Click')

    @classmethod
    def RightClick(cls, x, y):
        cls.MoveMouse(x, y)
        win32api.mouse_event(win32con.MOUSEEVENTF_RIGHTDOWN, 0, 0)
        sleep(.1)
        win32api.mouse_event(win32con.MOUSEEVENTF_RIGHTUP, 0, 0)
        print('Left Click')

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


if __name__ == '__main__':
    # Mouse.GetCursorPos()
    Mouse.LeftClick(545, 1066)
