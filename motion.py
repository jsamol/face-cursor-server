import pyautogui


def click():
    pyautogui.click()


def move(d_x, d_y):
    pyautogui.moveRel(d_x, d_y)


def move_left(delta=5):
    move(-delta, 0)


def move_right(delta=5):
    move(delta, 0)


def move_up(delta=5):
    move(0, -delta)


def move_down(delta=5):
    move(0, delta)
