import pygame
board_width = 1200
board_height = 600
size = (board_width,board_height)
red = (255, 0, 0)
green = (0, 255, 0)
blue = (0, 0, 255)
white = (255, 255, 255)
black = (0,0,0)
screen = pygame.display.set_mode((board_width, board_height))
mvmt_speed = 2
pac_size = 25
line_thickness = 10
gap = 1.5*pac_size+line_thickness-1
rad = (int)(pac_size/2)