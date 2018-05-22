import pygame 
from settings import *
from player import *
from board import *
pygame.init()

pygame.display.update()
clock = pygame.time.Clock()

pacman = player()
brd = board()

start_time = pygame.time.get_ticks()

while True:
    
    x_change = 0
    y_change=0

    screen.fill(black)
    brd.draw()
    keys = pygame.key.get_pressed()  #checking pressed keys
    if keys[pygame.K_UP]:
        pacman.dir='u'
        y_change = -mvmt_speed
    elif keys[pygame.K_DOWN]:
        pacman.dir='d'
        y_change = mvmt_speed
    elif keys[pygame.K_LEFT]:
        pacman.dir='l'
        x_change = -mvmt_speed
    elif keys[pygame.K_RIGHT]:
        pacman.dir='r'
        x_change = mvmt_speed

    for event in pygame.event.get():

        if event.type == pygame.QUIT:
            pygame.quit()
    
    for hlines in brd.hor:
        if pacman.x<hlines[1][0]+pac_size/2 and pacman.x>hlines[0][0]-pac_size/2:
            if pacman.y+y_change<hlines[0][1]+(pac_size+line_thickness)/2 and pacman.y+y_change>hlines[0][1]-(pac_size+line_thickness)/2:
                y_change=0
    
        if pacman.y<hlines[0][1]+(line_thickness+pac_size)/2 and pacman.y>hlines[0][1]-(line_thickness+pac_size)/2:
            if pacman.x+x_change<hlines[1][0]+pac_size/2 and pacman.x+x_change>hlines[0][0]-pac_size/2:
                x_change=0
    
    for vlines in brd.ver:
        if pacman.y<vlines[1][1]+pac_size/2 and pacman.y>vlines[0][1]-pac_size/2:
            if pacman.x+x_change<vlines[0][0]+(pac_size+line_thickness)/2 and pacman.x+x_change>vlines[0][0]-(pac_size+line_thickness)/2:
                x_change=0
        if pacman.x<vlines[0][0]+(line_thickness+pac_size)/2 and pacman.x>vlines[0][0]-(pac_size+line_thickness)/2:
            if pacman.y+y_change<vlines[1][1]+pac_size/2 and pacman.y+y_change>vlines[0][1]-pac_size/2:
                y_change=0
    
    

    pacman.x+=x_change
    pacman.y+=y_change
    if pacman.x > board_width+pac_size:
        pacman.x = -pac_size
    if pacman.y > board_height+pac_size:
        pacman.y = -pac_size
    if pacman.x < -pac_size:
        pacman.x = board_width+pac_size
    if pacman.y < -pac_size:
        pacman.y = board_height+pac_size
    
    qseconds = (int)((pygame.time.get_ticks()-start_time)/200)
    if qseconds%2 == 0:
        pacman.drawclosed()
    else:
        pacman.drawopen()
    pygame.display.update()
    clock.tick(60) 