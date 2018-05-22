import pygame
from settings import *

class board:
    def __init__(self):
        self.ver = []
        self.hor = []
        self.hor.append(((pac_size,3*pac_size),(board_width-pac_size,3*pac_size)))
        self.hor.append(((pac_size,board_height-pac_size),(board_width-pac_size,board_height - pac_size)))
        self.ver.append(((pac_size,3*pac_size),(pac_size,board_height - pac_size)))
        self.ver.append(((board_width-pac_size,3*pac_size),(board_width - pac_size,board_height - pac_size)))
        self.hor.append(((board_width/2 - 2.5*pac_size,board_height/2),(board_width/2 + 2.5*pac_size,board_height/2)))
        self.hor.append(((board_width/2 - 2.5*pac_size,board_height/2+2*pac_size),(board_width/2 + 2.5*pac_size,board_height/2+2*pac_size)))
        self.ver.append(((board_width/2 - 2.5*pac_size,board_height/2-line_thickness/2+1),(board_width/2 - 2.5*pac_size,board_height/2+2*pac_size+line_thickness/2)))
        self.ver.append(((board_width/2 + 2.5*pac_size,board_height/2-line_thickness/2+1),(board_width/2 + 2.5*pac_size,board_height/2+2*pac_size+line_thickness/2)))

    def draw(self):
        for vlines in self.ver:
            pygame.draw.line(screen,blue,vlines[0],vlines[1],line_thickness)
        for hlines in self.hor:
            pygame.draw.line(screen,blue,hlines[0],hlines[1],line_thickness)