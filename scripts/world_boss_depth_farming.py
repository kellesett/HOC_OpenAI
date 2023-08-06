import cv2 as cv
from time import sleep
import win32gui
from packages.window_capturing import Window
from packages.win32_devices import ClickArea
from config_data.config import *


def world_boss_depth_farming(cnt: int = 10):
    boss_cntr = 0

    while True:
        test_button = ClickArea(FIGHT_WB_B, active_window, False)
        depth_button = ClickArea(DEPTH_B, active_window, moving_button=True)

        # open depth mode
        if test_button.possibility < 0.9:
            depth_button.Click()
            test_button = ClickArea(FIGHT_WB_B, active_window)

        test_button.Click()

        # now - fight
        fight_button = ClickArea(FIGHT_B, active_window, moving_button=True)
        fight_button.Click()

        skip_button = ClickArea(LOWERCASE_SKIP_B, active_window)
        skip_button.Click()

        exit_button = ClickArea(EXIT_B, active_window)
        exit_button.Click()
        boss_cntr += 1
        print('Bosses killed:', boss_cntr)
        if boss_cntr == cnt:
            print('Farm have ended!')
            exit(0)


if __name__ == '__main__':
    active_window = Window('MEmu', 1350, 769)
    win32gui.SetForegroundWindow(active_window.hwnd)
    sleep(1)

    world_boss_depth_farming()
