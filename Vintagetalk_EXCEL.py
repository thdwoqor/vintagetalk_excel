import multiprocessing
import sys
import time
from multiprocessing import Process, Queue, freeze_support

import keyboard as kb
import win32api
import win32con
import win32gui
from pynput import keyboard, mouse

from util.auth import auth2
from util.button.setting import setting
from util.detail.get_window import getWindowList
from util.keyboard.press import press
from util.keyboard.release import release
from util.mouse.click import click
from view.gui import f9_image_state, f9_state, root, var


def closing():
    global speed
    root.destroy()
    speed[0] = -1


def queue_reset(speed, press):
    while True:
        if speed[0] == -1:
            sys.exit(0)
        if speed[0] != 5:
            time.sleep(0.01 / speed[0])
        if press[0]:
            title = getWindowList("꿀뷰")
            if title != None:
                hwndMain = win32gui.FindWindowEx(0, 0, 0, title)

                # wparam = win32api.MAKELONG(0, -win32con.WHEEL_DELTA)
                # lParam = win32api.MAKELONG(500, 500)

                # win32gui.SendMessage(hwndMain, win32con.WM_MOUSEWHEEL, wparam, lParam)
                # win32gui.SendMessage(hwndMain, win32con.WM_MOUSEMOVE, 0, lParam)
                win32api.PostMessage(hwndMain, win32con.WM_KEYDOWN, win32con.VK_SPACE, 0)
                win32api.PostMessage(hwndMain, win32con.WM_KEYUP, win32con.VK_SPACE, 0)


def main():
    kb.block_key("`")
    kb.block_key("tab")

    if not auth2(2022, 9, 30):
        sys.exit(0)

    global is_double_press, merge_queue, speed
    is_double_press = Queue()
    merge_queue = Queue()

    manager = multiprocessing.Manager()
    keyboard_press = manager.list()
    keyboard_press.append(False)

    manager1 = multiprocessing.Manager()
    speed = manager1.list()
    speed.append(var.get())

    with keyboard.Listener(
        on_press=lambda event: press(event, var=var, speed=speed, press=keyboard_press, f9_state=f9_state),
        on_release=lambda event: release(
            event,
            var=var,
            speed=speed,
            merge_queue=merge_queue,
            press=keyboard_press,
        ),
    ) as listener:
        with mouse.Listener(on_click=lambda *event: click(*event, f9_image_state=f9_image_state)) as listener:
            func = Process(
                target=queue_reset,
                args=(speed, keyboard_press),
            )
            func.start()

            root.protocol("WM_DELETE_WINDOW", closing)
            root.mainloop()

            is_double_press.close()
            is_double_press.join_thread()
            listener.stop()
            listener.join()
            func.join()


if __name__ == "__main__":
    freeze_support()
    setting()
    main()

# pyinstaller -w --exclude pandas, --exclude numpy run.py

# https://soma0sd.tistory.com/123
# https://www.codegrepper.com/code-examples/python/python+get+list+of+all+open+windows
# https://github.com/boppreh/keyboard#keyboard.block_key
# https://stackoverflow.com/questions/62985579/restrict-block-key-presses-for-input-in-python-and-prevent-keyboard-key-press-ap
# https://mebadong.tistory.com/80

# win32api.keybd_event(win32con.VK_F1, 0, 0,  -3943346)  # key down
# time.sleep(1)
# win32api.keybd_event(win32con.VK_F1, 0, win32con.KEYEVENTF_KEYUP,  -3943346)  # key up

# pyinstaller -w --icon=icon.ico --exclude pandas Vintagetalk_EXCEL.py
