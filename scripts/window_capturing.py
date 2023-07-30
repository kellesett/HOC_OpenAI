import win32gui
import win32ui
import win32con
import numpy as np
import cv2


def get_screenshot(window_name):
    # define your window size
    w, h = 2600, 1080

    # get hwnd
    hwnd = win32gui.FindWindow(None, window_name)

    # get the window image data
    wdc = win32gui.GetWindowDC(hwnd)
    dc_obj = win32ui.CreateDCFromHandle(wdc)
    cdc = dc_obj.CreateCompatibleDC()
    data_bit_map = win32ui.CreateBitmap()
    data_bit_map.CreateCompatibleBitmap(dc_obj, w, h)
    cdc.SelectObject(data_bit_map)
    cdc.BitBlt((0, 0), (w, h), dc_obj, (0, 0), win32con.SRCCOPY)

    # save the image as a bitmap file
    data_bit_map.SaveBitmapFile(cdc, 'debug.bmp')

    # convert the raw data into a format opencv can read
    signed_ints_array = data_bit_map.GetBitmapBits(True)
    img = np.frombuffer(signed_ints_array, dtype='uint8')
    img.shape = (h, w, 4)

    # free resources
    dc_obj.DeleteDC()
    cdc.DeleteDC()
    win32gui.ReleaseDC(hwnd, wdc)
    win32gui.DeleteObject(data_bit_map.GetHandle())

    # drop the alpha channel to work with cv.matchTemplate()
    img = img[..., :3]

    # make image C_CONTIGUOUS to avoid errors with cv.rectangle()
    img = np.ascontiguousarray(img)

    return img


def enum_handler(hwnd, lparam):
    with open('windows_list.txt', 'a', encoding='utf-8') as file:
        if not win32gui.IsWindowVisible(hwnd):
            return
        window_name = win32gui.GetWindowText(hwnd)
        if window_name:
            print(hwnd, window_name, file=file)


def show_windows():
    win32gui.EnumWindows(enum_handler, None)


if __name__ == '__main__':
    show_windows()
    name = 'HOC_OpenAI – window_capturing.py'

    image = get_screenshot(name)
    cv2.imshow('test', image)
    cv2.waitKey()
