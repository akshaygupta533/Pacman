import pygame
import pygame.gfxdraw
from settings import *

def rot_center(image, rect, angle):
        """rotate an image while keeping its center"""
        rot_image = pygame.transform.rotate(image, angle)
        rot_rect = rot_image.get_rect(center=rect.center)
        return rot_image,rot_rect

def draw_text(text,x,y,size):
        pygame.font.init()
        myfont = pygame.font.SysFont('Comic Sans MS',size)
        textsurface = myfont.render(text,True,white)
        screen.blit(textsurface,(x,y))
