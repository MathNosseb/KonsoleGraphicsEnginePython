import os
import time
from abc import ABC, abstractmethod
class Grid(ABC):
    def __init__(self, size):
        self.size = size
        self.x, self.y = 0, 0
        self.screen_buffer = [None for _ in range(size*size)]  # attribut d'instance

    def clearScreen(self):

        print("\033[2J\033[H", end="")


    def draw(self):
        for y in range(self.size):
            for x in range(self.size):
                item = self.screen_buffer[x + y * self.size]
                if item:
                    item.draw()
    def fall(self):
        for y in range(self.size):
            for x in range(self.size):
                item = self.screen_buffer[x + y * self.size]
                if item:
                    item.y=+1
                    self.screen_buffer[x+y*self.size] == 


class Square(Grid):
    def __init__(self, x, y, window):
        self.x = x
        self.y = y
        window.screen_buffer[x + y * window.size] = self  # modifie l'instance
    def draw(self):
        print("\033["+str(self.y)+";"+str(self.x)+"H"+"aa")
        print("\033["+str(self.y+1)+";"+str(self.x)+"H"+"aa")


window = Grid(6)
window.clearScreen()

carre = Square(1, 1, window)  # on passe l'instance
window.draw()

for z in range(100):
    window.draw()
    time.sleep(1)
    window.clearScreen()
    



"""#clear the screen
for i in range(1080):
    print("\033["+str(0)+";"+str(i)+"H"+"a")
"""