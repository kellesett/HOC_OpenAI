import cv2 as cv
import win32gui
from packages import ClickArea, Window
from time import sleep
from config_data import *


if __name__ == "__main__":
    print('Your personal bot console ready for farming!')

    while True:
        command = input('User: ')
        print('Your command:', command)
