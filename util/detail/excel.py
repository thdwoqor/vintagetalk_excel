import win32api
import win32con
import win32gui


def excel(x: int, y: int, name: str) -> None:
    hWnd = win32gui.FindWindow(None, name)

    lParam = win32api.MAKELONG(x, y)
    hWnd1 = win32gui.FindWindowEx(hWnd, None, None, None)
    win32gui.SendMessage(hWnd1, win32con.WM_LBUTTONDOWN, win32con.MK_LBUTTON, lParam)
    win32gui.SendMessage(hWnd1, win32con.WM_LBUTTONUP, None, lParam)
