import win32api
import win32gui

import win32con


def click():
    x, y = win32gui.GetCursorPos()
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN, x, y, 0, 0)
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP, x, y, 0, 0)


def move(d_x, d_y):
    x, y = win32gui.GetCursorPos()

    win32api.SetCursorPos((x + d_x, y + d_y))


def move_left(delta=5):
    move(-delta, 0)


def move_right(delta=5):
    move(delta, 0)


def move_up(delta=5):
    move(0, -delta)


def move_down(delta=5):
    move(0, delta)
