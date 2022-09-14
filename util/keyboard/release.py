import win32api
import win32con
import win32gui
from pynput import keyboard
from pynput.keyboard import KeyCode
from util.detail.get_window import getWindowList


def release(key, var, speed, merge_queue, press):
    if key == keyboard.Key.enter:
        title = getWindowList("꿀뷰")
        if title != None:
            hwndMain = win32gui.FindWindowEx(0, 0, 0, title)

            win32api.PostMessage(hwndMain, win32con.WM_KEYUP, win32con.VK_NEXT, 0)
    elif key == KeyCode.from_char("`"):
        press[0] = False
