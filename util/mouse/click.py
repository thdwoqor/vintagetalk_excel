import time

import pyautogui
import win32api
import win32con
import win32gui
from pynput import mouse
from util.detail.get_window import getWindowList
from util.detail.size import size


def click(x, y, button, pressed, f9_image_state):
    if button == mouse.Button.left:
        if pressed == True:
            window = getWindowList("입력")
            if window == "입력":
                try:
                    size_x1, size_y1, top, left = size("입력", "ThunderDFrame")

                    title = getWindowList("꿀뷰")
                    if title != None:
                        hwndMain = win32gui.FindWindowEx(0, 0, 0, title)
                        if (
                            y >= top + 31 + size_y1 * 0.0074183976261128
                            and y <= top + 31 + size_y1 * 0.1454005934718101
                        ):
                            if x >= left + size_x1 * 0.9000657462195924 and x <= left + size_x1 * 0.9349112426035503:
                                if f9_image_state.get() == 1:
                                    print("f9")
                                    pyautogui.press("f9")
                                    time.sleep(0.1)
                                    pyautogui.press("f9")
                            elif x >= left + size_x1 * 0.8625904010519395 and x <= left + size_x1 * 0.8974358974358974:
                                win32api.PostMessage(hwndMain, win32con.WM_KEYDOWN, win32con.VK_NEXT, 0)
                                win32api.PostMessage(hwndMain, win32con.WM_KEYUP, win32con.VK_NEXT, 0)
                            elif x >= left + size_x1 * 0.8145956607495069 and x <= left + size_x1 * 0.8599605522682446:
                                win32api.PostMessage(hwndMain, win32con.WM_KEYDOWN, win32con.VK_PRIOR, 0)
                                win32api.PostMessage(hwndMain, win32con.WM_KEYUP, win32con.VK_PRIOR, 0)
                except:
                    pass
            elif window == "입력2":
                try:
                    size_x1, size_y1, top, left = size("입력2", "ThunderDFrame")

                    title = getWindowList("꿀뷰")
                    if title != None:
                        hwndMain = win32gui.FindWindowEx(0, 0, 0, title)
                        if y >= top + size_y1 * 0.0449826989619377 and y <= top + size_y1 * 0.1995386389850058:
                            if x >= left + size_x1 * 0.875 and x <= left + size_x1 * 0.9256578947368421:
                                if f9_image_state.get() == 1:
                                    print("f9")
                                    pyautogui.press("f9")
                                    time.sleep(0.1)
                                    pyautogui.press("f9")
                            elif x >= left + size_x1 * 0.8217105263157895 and x <= left + size_x1 * 0.8723684210526316:
                                win32api.PostMessage(hwndMain, win32con.WM_KEYDOWN, win32con.VK_NEXT, 0)
                                win32api.PostMessage(hwndMain, win32con.WM_KEYUP, win32con.VK_NEXT, 0)
                            elif x >= left + size_x1 * 0.7532894736842105 and x <= left + size_x1 * 0.8190789473684211:
                                win32api.PostMessage(hwndMain, win32con.WM_KEYDOWN, win32con.VK_PRIOR, 0)
                                win32api.PostMessage(hwndMain, win32con.WM_KEYUP, win32con.VK_PRIOR, 0)
                except:
                    pass


# Window , Window
