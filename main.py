import pygame 
from settings import *
from player import *
pygame.init()

pygame.display.update()
clock = pygame.time.Clock()

pacman = player()

start_time = pygame.time.get_ticks()

while True:
    
    x_change = 0
    y_change=0

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
    pacman.x+=x_change
    pacman.y+=y_change
    qseconds = (int)((pygame.time.get_ticks()-start_time)/200)
    gameDisplay.fill(black)
    if qseconds%2 == 0:
        pacman.drawclosed()
    else:
        pacman.drawopen()
    pygame.display.update()
    clock.tick(60) 