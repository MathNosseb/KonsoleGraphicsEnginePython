import os
import time
from abc import ABC, abstractmethod
from KonsoleEngine import *


window = Grid([40,80])
window.clearScreen()

carre = Square(1, 1,"a", window)  # on passe l'instance
carre2 = Square(3,1,"b",window)

carre.summon(window)

window.draw()

while True:
    window.draw()
    time.sleep(1)
    window.clearScreen()
    window.fall()

    



"""#clear the screen
for i in range(1080):
    print("\033["+str(0)+";"+str(i)+"H"+"a")
"""