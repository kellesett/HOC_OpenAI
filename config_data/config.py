import cv2 as cv
import sys

path = r"C:\\Users\\gorpr\\PycharmProjects\\HOC_OpenAI\\images\\"

DEPTH_B = cv.imread(path + 'depthB.png')
FIGHT_WB_B = cv.imread(path + 'WB__depth_fightB.png')
NEXT_STAGE_B = cv.imread(path + 'next_stageB.png')
EXPLORE_B = cv.imread(path + 'exploreB.png')
FIGHT_B = cv.imread(path + 'general_figthB.png')
LOWERCASE_SKIP_B = cv.imread(path + 'skipB.png')
UPPERCASE_SKIP_B = cv.imread(path + 'skip2B.png')
EXIT_B = cv.imread(path + 'exitB.png')
CARD_B = cv.imread(path + 'cardB.png')
OK_B = cv.imread(path + 'okB.png')
USE_B = cv.imread(path + 'useB.png')

EMPTY = cv.imread(path + 'empty_window.png')

W_WIDTH = 1350
W_HEIGHT = 769
W_NAME = 'MEmu'
W_PATH = "C:\Microvirt\MEmu\MEmu.exe"

COMMANDS = (
    ('open', 'Open MEmu window and resize it'),
    ('explore', 'Explore new locations'),
    ('quit', 'Leave console')
)
