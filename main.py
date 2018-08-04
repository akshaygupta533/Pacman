import pygame 
from settings import *
from player import *
from board import *
from ghost import *
import random
pygame.init()

pygame.display.update()
clock = pygame.time.Clock()

pacman = player()
brd = board()
ghosts=[]
ghosts.append(reda())
ghosts.append(yellowa())
ghosts.append(bluea())
ghosts.append(pinka())

total=len(brd.rect)
score=0

start_time = pygame.time.get_ticks()

while True:
    
    x_change = 0
    y_change=0

    screen.fill(black)
    brd.draw()
    draw_text("Score",pac_size,pac_size,30)
    draw_text(str(score),3*pac_size+20,pac_size,30)
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
    
    for g in ghosts:
        if pacman.x<g.x+pac_size and pacman.x>g.x-pac_size:
            if pacman.y<g.y+pac_size and pacman.y>g.y-pac_size:
                pacman.destroy()
        
        g.x_change=0
        g.y_change=0
        if g.dir=='l':
            g.x_change= -ghost_speed
        elif g.dir=='r':
            g.x_change= +ghost_speed
        elif g.dir=='u':
            g.y_change= -ghost_speed
        elif g.dir=='d':
            g.y_change= +ghost_speed

        for hlines in brd.hor:
            if g.x<hlines[1][0]+25/2 and g.x>hlines[0][0]-25/2:
                if g.y+g.y_change<hlines[0][1]+(25+line_thickness)/2 and g.y+g.y_change>hlines[0][1]-(25+line_thickness)/2:
                    g.y_change=0
    
            if g.y<hlines[0][1]+(line_thickness+25)/2 and g.y>hlines[0][1]-(line_thickness+25)/2:
                if g.x+g.x_change<hlines[1][0]+25/2 and g.x+g.x_change>hlines[0][0]-25/2:
                    g.x_change=0
    
        for vlines in brd.ver:
            if g.y<vlines[1][1]+25/2 and g.y>vlines[0][1]-25/2:
                if g.x+g.x_change<vlines[0][0]+(25+line_thickness)/2 and g.x+g.x_change>vlines[0][0]-(25+line_thickness)/2:
                    g.x_change=0

            if g.x<vlines[0][0]+(line_thickness+25)/2 and g.x>vlines[0][0]-(25+line_thickness)/2:
                if g.y+g.y_change<vlines[1][1]+25/2 and g.y+g.y_change>vlines[0][1]-25/2:
                    g.y_change=0
        if g.x_change==0 and g.y_change==0:
            rand = random.randint(1,4)
            if rand==1:
                g.dir='l'
            elif rand==2:
                g.dir='r'
            elif rand==3:
                g.dir='u'
            elif rand==4:
                g.dir='d'
        g.x+=g.x_change
        g.y+=g.y_change
        g.draw()
             



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



    for rect in brd.rect:
        if pacman.y>=rect[1]-pac_size/2 and pacman.y<=rect[1]+pac_size/2+5 and pacman.x>=rect[0]-pac_size/2 and pacman.x<=rect[0]+pac_size/2+5 and rect[2]!=0:
            rect[2]=0
            score+=1

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


    for life in range (1,pacman.lives+1):
        image = pygame.image.load(mopen)
        rect = image.get_rect()
        rect.centerx = 5*pac_size + life*1.5*pac_size
        rect.centery = 1.5*pac_size
        screen.blit(image, rect)

    if pacman.lives<0 or score==total:
        screen.fill(black)
        draw_text("Game Over",board_width/3,board_height/2.5,100)

    pygame.display.update()
    clock.tick(60) 