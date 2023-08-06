import cv2 as cv
from time import sleep
import win32gui
from packages import ClickArea, Window
from config_data import *


def nightmare_exploration():
    active_window = Window(W_NAME, W_WIDTH, W_HEIGHT)
    win32gui.SetForegroundWindow(active_window.hwnd)

    threshold = 0.8

    while True:
        sleep(.1)
        use_button = ClickArea(USE_B, active_window, non_repudiation=False)
        if use_button.possibility >= threshold:
            use_button.Click()
            continue

        next_stage_button = ClickArea(NEXT_STAGE_B, active_window, non_repudiation=False)
        if next_stage_button.possibility >= threshold:
            next_stage_button.Click()
            print('Stage completed!')
            continue

        card_button = ClickArea(CARD_B, active_window, non_repudiation=False)
        if card_button.possibility >= threshold:
            card_button.Click()
            print('Card received.')
            continue

        fight_button = ClickArea(FIGHT_B, active_window, non_repudiation=False, moving_button=True)
        if fight_button.possibility >= threshold:
            fight_button.Click()

            skip_button = ClickArea(UPPERCASE_SKIP_B, active_window)
            skip_button.Click()

            exit_button = ClickArea(EXIT_B, active_window)
            exit_button.Click()
            print('Fight completed!')
            continue

        ok_button = ClickArea(OK_B, active_window, non_repudiation=False)
        if ok_button.possibility >= threshold:
            ok_button.Click()
            continue

        explore_button = ClickArea(EXPLORE_B, active_window, non_repudiation=False, moving_button=True)
        if explore_button.possibility >= threshold:
            explore_button.Click()


if __name__ == '__main__':
    nightmare_exploration()
