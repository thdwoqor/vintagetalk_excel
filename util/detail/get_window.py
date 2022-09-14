import win32gui


def getWindowList(name: str) -> str:
    def callback(hwnd, hwnd_list: list):
        title = win32gui.GetWindowText(hwnd)
        if win32gui.IsWindowEnabled(hwnd) and win32gui.IsWindowVisible(hwnd) and title:
            hwnd_list.append((title, hwnd))
        return True

    output = []
    win32gui.EnumWindows(callback, output)

    for title, pid in output:
        if name in title:
            return title


def getWindowLists() -> str:
    def callback(hwnd, hwnd_list: list):
        title = win32gui.GetWindowText(hwnd)
        if win32gui.IsWindowEnabled(hwnd) and win32gui.IsWindowVisible(hwnd) and title:
            hwnd_list.append((title, hwnd))
        return True

    output = []
    win32gui.EnumWindows(callback, output)

    for title, pid in output:
        for name in ["입력", "입력2", "Excel"]:
            if name in title:
                return title
