from settings import *
from utilities import *
import pygame

blueimg = 'blue_a.png'
pinkimg = 'pink_a.png'
yellowimg = 'yellow_a.png'
redimg = 'red_a.png'

class ghosts:
    def __init__(self):
        pass
    def draw(self,img):
        self.image = pygame.image.load(img)
        self.rect = self.image.get_rect()
        self.rect.centerx = self.x
        self.rect.centery = self.y
        screen.blit(self.image, self.rect)
class reda(ghosts):
    def __init__(self):
        self.x = board_width-7*pac_size
        self.y = 4*pac_size
        self.dir = 'l'
        self.x_change=0
        self.y_change=0
    def draw(self):
        super().draw(redimg)
class pinka(ghosts):
    def __init__(self):
        self.x = 8*pac_size
        self.y = 4*pac_size
        self.dir = 'd'
        self.x_change=0
        self.y_change=0
    def draw(self):
        super().draw(pinkimg)
class bluea(ghosts):
    def __init__(self):
        self.x = board_width/2
        self.y = board_height/2-pac_size
        self.dir = 'u'
        self.x_change=0
        self.y_change=0
    def draw(self):
        super().draw(blueimg)
class yellowa(ghosts):
    def __init__(self):
        self.x = 6*pac_size
        self.y = board_height-5*pac_size
        self.dir = 'r'
        self.x_change=0
        self.y_change=0
    def draw(self):
        super().draw(yellowimg)