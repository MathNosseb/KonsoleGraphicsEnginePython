import os
import time
from abc import ABC, abstractmethod
from KonsoleEngine import *
import Keyboard


window = Grid([40,80])
window.clearScreen()

carre = Square(3, 1,"a", window)  # on passe l'instance
carre.summon(window)

window.draw()

interval = 1.0  # une seconde

start = time.time()

while True:

    #keyboard
    char = Keyboard.GetKey()
    if char:
        if char.lower() == 'q' :
            if carre.x != 1:
                window.screen_buffer[carre.x + carre.y * window.size[0]] = None
                carre.x -= 2
                window.screen_buffer[carre.x + carre.y * window.size[0]] = carre
        if char.lower() == 'd' :
            if carre.x < (window.size[0] - 2): # -2 car il y a deux character pour un carré
                window.screen_buffer[carre.x + carre.y * window.size[0]] = None
                carre.x += 2
                window.screen_buffer[carre.x + carre.y * window.size[0]] = carre
        if char == " ":
            break



    if time.time() - start >= interval:
        window.clearScreen()
        window.draw()
        window.fall()
        start = time.time()
        


    
"""#clear the screen
for i in range(1080):
    print("\033["+str(0)+";"+str(i)+"H"+"a")
"""