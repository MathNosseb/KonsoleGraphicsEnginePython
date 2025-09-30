import os
import time
from abc import ABC, abstractmethod
class Grid(ABC):
    def __init__(self, size):
        self.size = size
        self.x, self.y = 0, 0
        self.screen_buffer = [None for _ in range(size[0]*size[1])]  # attribut d'instance

    def clearScreen(self):

        print("\033[2J\033[H", end="")
        for screen in range(self.size[1]):
            print("\033["+str(screen)+";"+str(self.size[0])+"H"+f"#")


    def draw(self):
        for y in range(self.size[1]):
            for x in range(self.size[0]):
                item = self.screen_buffer[x + y * self.size[0]]
                if item:
                    item.draw()
    def fall(self):
        for y in range(self.size[1] - 1, -1, -1):  # du bas vers le haut
            for x in range(self.size[0]):
                item = self.screen_buffer[x + y * self.size[0]]
                if item:
                    new_y = item.y + 1
                    if new_y < self.size[1]:  # si on est pas en bas
                        # libérer l’ancienne case
                        self.screen_buffer[x + y * self.size[0]] = None
                        # déplacer
                        item.y = new_y
                        self.screen_buffer[item.x + item.y * self.size[0]] = item



class Square:
    def __init__(self, x, y,character, window):
        self.x = x
        self.y = y
        self.character = character
    def summon(self,windows):
        windows.screen_buffer[self.x + self.y * windows.size[0]] = self  # modifie l'instance
    def draw(self):
        print("\033["+str(self.y)+";"+str(self.x)+"H"+f"{self.character*2}")
        print("\033["+str(self.y+1)+";"+str(self.x)+"H"+f"{self.character*2}")
    def changeXCoord(self,changeX):
        self.x = changeX
        