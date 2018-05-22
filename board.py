import pygame
from settings import *

class board:
    def __init__(self):
        self.ver = []
        self.hor = []
        self.hor.append(((pac_size,pac_size),(board_width-pac_size,pac_size)))
        self.hor.append(((pac_size,board_height-pac_size),(board_width-pac_size,board_height - pac_size)))
        self.ver.append(((pac_size,pac_size),(pac_size,board_height - pac_size)))
        self.ver.append(((board_width-pac_size,pac_size),(board_width - pac_size,board_height - pac_size)))
    def draw(self):
        for vlines in self.ver:
            pygame.draw.line(screen,blue,vlines[0],vlines[1])
        for hlines in self.hor:
            pygame.draw.line(screen,blue,hlines[0],hlines[1])