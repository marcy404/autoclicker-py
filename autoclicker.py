from time import sleep
import mouse
import keyboard

class Stopper:
    def __init__(self):
        self.a = 0
    
    def addA(self):
        self.a += 1
        return self.a


a = Stopper()

keyboard.add_hotkey('ctrl+alt+shift+s', a.addA)
sleep(2)

while a.a == 0:
    mouse.click()
    
print('break')