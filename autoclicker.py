import mouse
from time import sleep as slp

counter = 0
slp(5)
while True:
    slp(0.1)
    mouse.click()
    print('clicked.')

    if counter == 10_000:
        break
    else:
        counter += 1

print('CLICKING FINISHED')