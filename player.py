from settings import *
from utilities import *
import pygame

mopen = 'open.png'
mclosed = 'closed.png'

class player:
    def __init__(self):
        self.x = board_height/2
        self.y = board_height/2
        self.dir = 'r'
    def drawopen(self):
        self.image = pygame.image.load(mopen)
        self.rect = self.image.get_rect()
        self.rect.centerx = self.x
        self.rect.centery = self.y
        if self.dir == 'l':
            self.image = rot_center(self.image,180)
        elif self.dir == 'u':
            self.image = rot_center(self.image,90)
        elif self.dir == 'd':
            self.image = rot_center(self.image,-90)
        gameDisplay.blit(self.image, self.rect)
    def drawclosed(self):
        self.image = pygame.image.load(mclosed)
        self.rect = self.image.get_rect()
        self.rect.centerx = self.x
        self.rect.centery = self.y
        gameDisplay.blit(self.image, self.rect)