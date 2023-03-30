import pyautogui
from keyboard import is_pressed

pyautogui.PAUSE = 0.0001
while True:
    pyautogui.click()
    if is_pressed('z'):
        break

print('LOOP BROKEN')