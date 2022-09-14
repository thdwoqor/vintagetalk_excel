import datetime
import threading
from tkinter import messagebox

# lock = threading.Lock()


def sum(files, save_path, index, start, lock):
    import os

    from util.detail.merge import merge
    from view.gui import (
        blank_size,
        line_color,
        merge_progress,
        merge_progressbar,
        merge_state,
    )

    global state, count, max

    while len(index) > 0:
        lock.acquire()
        i = index.pop(0)
        file = files[i]
        lock.release()
        print(i)
        merge(file, save_path, blank_size.get(), line_color.cget("bg"))

        if merge_state.get() < i * 100 / max:
            merge_progress.configure(text=f"{i+1}/{max}")
            merge_state.set(i * 100 / max)
            merge_progressbar.update()
    if i == len(files) - 1:
        messagebox.showinfo(title="", message="작업 소요 시간 : " + str(datetime.datetime.now() - start))


def merge_all(event):
    import os
    from glob import glob

    from util.button.path import product_path as pp
    from util.detail.merge import merge
    from view.gui import merge_folder_name, merge_progress, merge_state

    global state, count, max

    product_path = str(pp())

    if product_path == "None":
        # wx.MessageDialog(None, "경로를 설정해 주세요", "에러", wx.OK | wx.ICON_ERROR, pos=(200, 200)).ShowModal()
        return

    temp = "\\".join(product_path.split("\\")[:-1])

    files = glob(product_path + "\\*")

    save_path = os.path.join(temp, "web", merge_folder_name.get())

    state = 0
    count = 1
    max = len(files)
    index = [i for i in range(max)]

    merge_state.set(0)
    merge_progress.configure(text=f"0/{max}")

    start = datetime.datetime.now()
    lock = threading.Lock()
    t = threading.Thread(target=sum, args=(files, save_path, index, start, lock))
    t.start()
    t2 = threading.Thread(target=sum, args=(files, save_path, index, start, lock))
    t2.start()
    t3 = threading.Thread(target=sum, args=(files, save_path, index, start, lock))
    t3.start()

    # end = datetime.datetime.now()
    # messagebox.showinfo(title="", message="작업 소요 시간 : " + str(end - start))
