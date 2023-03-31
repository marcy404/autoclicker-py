import pyautogui
from keyboard import is_pressed
from time import sleep as timesleep


timesleep(2)
pyautogui.PAUSE = 0.0001
while True:
    pyautogui.click()
    if is_pressed('z'): break