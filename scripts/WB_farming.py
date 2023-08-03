from win32_devices import ClickArea
from window_capturing import Window
import cv2 as cv
from time import sleep
import win32gui

if __name__ == '__main__':
    active_window = Window('MEmu', 1350, 769)
    win32gui.SetForegroundWindow(active_window.hwnd)
    sleep(1)

    FIGHT_WB_img = cv.imread('../images/WB__depth_fightB.png')
    FIGHT_img = cv.imread('../images/general_figthB.png')
    SKIP_img = cv.imread('../images/skipB.png')
    EXIT_img = cv.imread('../images/exitB.png')
    DEPTH_img = cv.imread('../images/depthB.png')

    boss_cntr = 0
    while True:
        test_button = ClickArea(FIGHT_WB_img, active_window, False)
        depth_button = ClickArea(DEPTH_img, active_window, moving_button=True)

        # open depth mode
        if test_button.possibility < 0.9:
            depth_button.Click()
            sleep(.1)
            test_button = ClickArea(FIGHT_WB_img, active_window)

        test_button.Click()

        # now - fight
        fight_button = ClickArea(FIGHT_img, active_window, moving_button=True)
        fight_button.Click()

        skip_button = ClickArea(SKIP_img, active_window)
        skip_button.Click()

        exit_button = ClickArea(EXIT_img, active_window)
        exit_button.Click()
        boss_cntr += 1
        print('Bosses killed:', boss_cntr)
        if boss_cntr == 20:
            print('Farm have ended!')
            exit(0)
