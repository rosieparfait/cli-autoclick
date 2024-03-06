#TO RUN THE AUTOCLICKER, PRESS 'P'

import mouse
import keyboard
import time

loopActive = False
run = True
did = False

cps = 15# 15

print("Currect CPS: " + str(cps))

while run:
    if(keyboard.is_pressed('o')): run = False
    if(keyboard.is_pressed('+')):
        cps += 1
        print("Currect CPS: " + str(cps))
    if(keyboard.is_pressed('-')):
        cps -= 1
        print("Currect CPS: " + str(cps))
    if(keyboard.is_pressed('p') and not did):
        loopActive = not loopActive
        print("\n\nAutoclicker Active: " + str(loopActive))
        did = True
    if(not keyboard.is_pressed('p') and did):
        did = False
    if(loopActive): mouse.click('left')
    time.sleep(1/cps)
    
