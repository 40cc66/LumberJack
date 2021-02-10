"""
Author: Stanislav Akimov
"""
import sys
from itertools import product

import pyautogui

pyautogui.click(400, 400)  # Move to the game window.
interval = float(sys.argv[-1]) if len(sys.argv) == 2 else 0.07
branch_colors = [
    (161, 116, 56),
    (136, 99, 50),
]  # Branch colors found out with `python -m pyautogui`.

LEFT = 'left'
RIGHT = 'right'

branch_ys = (645, 545, 445, 345, 245, 145)
left_branch_x = 430
right_branch_x = 530

pyautogui.press('left')
pyautogui.press('left')

while True:
    pyautogui.sleep(interval)
    chops = []
    for y, x in product(branch_ys, (left_branch_x, right_branch_x)):
        pixel = pyautogui.pixel(x, y)
        if pixel in branch_colors:
            chop_side = RIGHT if x == left_branch_x else LEFT
            chops.append(chop_side)
    for chop_side in chops:
        pyautogui.press(chop_side)
        pyautogui.press(chop_side)
