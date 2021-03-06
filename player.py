from settings import *
from utilities import *
import pygame

mopen = 'open.png'
mclosed = 'closed.png'

'''The configuratons for the player'''

class player:
    def __init__(self):
        self.x = board_width/2
        self.y = board_height-2*pac_size
        self.dir = 'r'
        self.lives = 3
    def drawopen(self):
        self.image = pygame.image.load(mopen)
        self.rect = self.image.get_rect()
        self.rect.centerx = self.x
        self.rect.centery = self.y
        if self.dir == 'l':
            self.image,self.rect = rot_center(self.image,self.rect,180)
        elif self.dir == 'u':
            self.image,self.rect = rot_center(self.image,self.rect,90)
        elif self.dir == 'd':
            self.image,self.rect = rot_center(self.image,self.rect,-90)
        screen.blit(self.image, self.rect)
    def drawclosed(self):
        self.image = pygame.image.load(mclosed)
        self.rect = self.image.get_rect()
        self.rect.centerx = self.x
        self.rect.centery = self.y
        screen.blit(self.image, self.rect)
    def destroy(self):
        self.x = board_width/2
        self.y = board_height-2*pac_size
        self.lives-=1
        