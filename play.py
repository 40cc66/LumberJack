import sys
import pyautogui

pyautogui.click(400, 400)  # Move to the game window.
interval = float(sys.argv[-1]) if len(sys.argv) == 2 else 0.07
branch_colors = [
    (161, 116, 56),
    (136, 99, 50),
]  # Branch colors found out with `python -m pyautogui`.
chop_left = True  # Start chopping from left.
while True:
    if chop_left:
        pyautogui.press('left', interval=interval)
        pixel = pyautogui.pixel(425, 645)
        if pixel in branch_colors:
            chop_left = False

    else:
        pyautogui.press('right', interval=interval)
        pixel = pyautogui.pixel(535, 645)
        if pixel in branch_colors:
            chop_left = True
