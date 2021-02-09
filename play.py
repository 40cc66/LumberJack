import pyautogui

pyautogui.click(400, 400)  # Move to the game window.
interval = 0.08
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
            pyautogui.press('right', interval=0)
            chop_left = False
        else:
            pixel = pyautogui.pixel(535, 645)
            if pixel in branch_colors:
                pyautogui.press('left', interval=0)

    else:
        pyautogui.press('right', interval=interval)
        pixel = pyautogui.pixel(535, 645)
        if pixel in branch_colors:
            pyautogui.press('left', interval=0)
            chop_left = True
        else:
            pixel = pyautogui.pixel(425, 645)
            if pixel in branch_colors:
                pyautogui.press('right', interval=0)
