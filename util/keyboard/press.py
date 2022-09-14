import time

import pyautogui
import win32api
import win32con
import win32gui
from pynput import keyboard
from pynput.keyboard import KeyCode
from util.detail.excel import excel
from util.detail.get_window import getWindowList, getWindowLists
from util.detail.process import process
from util.detail.size import size


def press(key, var, speed, press, f9_state):
    if key == keyboard.Key.enter:
        if any(valid_url in process() for valid_url in ["입력", "입력2", "꿀뷰", "Excel"]):
            w = win32gui
            window = str(w.GetWindowText(w.GetForegroundWindow()))

            if window == "입력":
                size_x, size_y, top, left = size("입력", "ThunderDFrame")
                print(size_x, size_y, top, left)
                excel(int(size_x * 0.8714661406969099), int(size_y * 0.0764094955489614), "입력")
            elif window == "입력2":
                size_x, size_y, top, left = size("입력2", "ThunderDFrame")
                print(size_x, size_y, top, left)
                excel(int(size_x * 0.8473684210526316), int(size_y * 0.1291810841983852), "입력2")
            elif "꿀뷰" in window:
                while True:
                    try:
                        title = getWindowLists()
                        if "입력" in title:
                            size_x, size_y, top, left = size("입력", "ThunderDFrame")

                            excel(int(size_x * 0.8714661406969099), int(size_y * 0.0764094955489614), "입력")
                        elif "입력2" in title:
                            size_x, size_y, top, left = size("입력2", "ThunderDFrame")

                            excel(int(size_x * 0.8473684210526316), int(size_y * 0.1291810841983852), "입력2")
                        elif "Excel" in title:
                            hwndMain = win32gui.FindWindowEx(0, 0, 0, title)

                            win32api.PostMessage(hwndMain, win32con.WM_KEYDOWN, win32con.VK_DOWN, 0)
                            win32api.PostMessage(hwndMain, win32con.WM_KEYUP, win32con.VK_DOWN, 0)
                        break
                    except:
                        pass

            title = getWindowList("꿀뷰")
            if title != None:
                hwndMain = win32gui.FindWindowEx(0, 0, 0, title)

                win32api.PostMessage(hwndMain, win32con.WM_KEYDOWN, win32con.VK_NEXT, 0)

            if f9_state.get() == 1:
                print("f9")
                pyautogui.press("f9")
                time.sleep(0.1)
                pyautogui.press("f9")

    elif key == KeyCode.from_char("`"):
        print("input `")
        speed[0] = int(var.get())
        if not press[0]:
            press[0] = True
    elif key == keyboard.Key.tab:
        title = getWindowList("꿀뷰")
        if title != None:
            hwndMain = win32gui.FindWindowEx(0, 0, 0, title)

            win32api.PostMessage(hwndMain, win32con.WM_KEYDOWN, win32con.VK_TAB, 0)
            win32api.PostMessage(hwndMain, win32con.WM_KEYUP, win32con.VK_TAB, 0)


# https://stackoverflow.com/questions/69922080/different-behaviours-encountered-when-posting-a-mouse-scroll-message-to-differen
