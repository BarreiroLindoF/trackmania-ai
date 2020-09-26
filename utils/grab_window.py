import win32gui
import pyautogui

hwnd = None


def screenshot(window_title=None):
    global hwnd
    if not hwnd:
        hwnd = win32gui.FindWindow(None, window_title)

    if not hwnd:
        raise Exception('Could not find the correct window.')

    win32gui.SetForegroundWindow(hwnd)
    x, y, x1, y1 = win32gui.GetClientRect(hwnd)
    x, y = win32gui.ClientToScreen(hwnd, (x, y))
    x1, y1 = win32gui.ClientToScreen(hwnd, (x1 - x, y1 - y))
    im = pyautogui.screenshot(region=(x, y, x1, y1))
    return im
