import pygame
from settings import *
from utilities import *

'''The configurtions for the board'''

class board:
    def __init__(self):
        self.ver = []
        self.hor = []
        self.rect = []
        #board frame
        self.hor.append(((pac_size,3*pac_size),(board_width-pac_size,3*pac_size)))
        self.hor.append(((pac_size,board_height-pac_size),(board_width-pac_size,board_height - pac_size)))
       
        self.ver.append(((pac_size,3*pac_size-line_thickness/2+1),(pac_size,board_height/2-0.75*pac_size)))
        self.ver.append(((pac_size,board_height/2+0.75*pac_size),(pac_size,board_height - pac_size+line_thickness/2)))
        
        self.ver.append(((board_width-pac_size,3*pac_size-line_thickness/2+1),(board_width - pac_size,board_height/2-0.75*pac_size)))
        self.ver.append(((board_width-pac_size,board_height/2+0.75*pac_size),(board_width - pac_size,board_height - pac_size+line_thickness/2)))
       
        self.hor.append(((pac_size,board_height/2-0.75*pac_size-line_thickness/2),(5*pac_size,board_height/2-0.75*pac_size-line_thickness/2)))
        self.hor.append(((pac_size,board_height/2+0.75*pac_size+line_thickness/2-1),(5*pac_size,board_height/2+0.75*pac_size+line_thickness/2-1)))

        self.hor.append(((board_width-5*pac_size,board_height/2-0.75*pac_size-line_thickness/2),(board_width-pac_size,board_height/2-0.75*pac_size-line_thickness/2)))
        self.hor.append(((board_width-5*pac_size,board_height/2+0.75*pac_size+line_thickness/2-1),(board_width-pac_size,board_height/2+0.75*pac_size+line_thickness/2-1)))
       
        #center box for aliens
        self.hor.append(((board_width/2 - 2.5*pac_size,board_height/2),(board_width/2 + 2.5*pac_size,board_height/2)))
        self.hor.append(((board_width/2 - 2.5*pac_size,board_height/2+2*pac_size),(board_width/2 + 2.5*pac_size,board_height/2+2*pac_size)))
        self.ver.append(((board_width/2 - 2.5*pac_size,board_height/2-line_thickness/2+1),(board_width/2 - 2.5*pac_size,board_height/2+2*pac_size+line_thickness/2)))
        self.ver.append(((board_width/2 + 2.5*pac_size,board_height/2-line_thickness/2+1),(board_width/2 + 2.5*pac_size,board_height/2+2*pac_size+line_thickness/2)))
        
        #other lines
        self.ver.append(((0.667*board_width,board_height-4*pac_size),(0.667*board_width,board_height - pac_size)))
        self.ver.append(((0.333*board_width,board_height-4*pac_size),(0.333*board_width,board_height - pac_size)))
        
        self.ver.append(((0.667*board_width,3*pac_size-line_thickness/2+1),(0.667*board_width,6*pac_size-line_thickness/2+1)))
        self.ver.append(((0.333*board_width,3*pac_size-line_thickness/2+1),(0.333*board_width,6*pac_size-line_thickness/2+1)))

        self.hor.append(((0.333*board_width+gap,3*pac_size+gap),(0.667*board_width-gap,3*pac_size+gap)))
        self.hor.append(((0.333*board_width+gap,board_height-pac_size-gap),(0.667*board_width-gap,board_height - pac_size-gap)))

        self.ver.append(((0.333*board_width,6*pac_size-line_thickness/2+1+gap),(0.333*board_width,9*pac_size-line_thickness/2+1+gap)))
        self.ver.append(((0.667*board_width,6*pac_size-line_thickness/2+1+gap),(0.667*board_width,9*pac_size-line_thickness/2+1+gap)))

        self.ver.append(((0.333*board_width,board_height-7*pac_size-gap),(0.333*board_width,board_height-4*pac_size-gap)))
        self.ver.append(((0.667*board_width,board_height-7*pac_size-gap),(0.667*board_width,board_height-4*pac_size-gap)))

        self.ver.append(((0.333*board_width+gap+line_thickness/2-1,board_height-4*pac_size-line_thickness+1),(0.333*board_width+gap+line_thickness/2-1,board_height-pac_size-gap)))
        self.ver.append(((0.667*board_width-gap-line_thickness/2,board_height-4*pac_size-line_thickness+1),(0.667*board_width-gap-line_thickness/2,board_height-pac_size-gap)))
        self.hor.append(((0.333*board_width+gap+line_thickness/2-1,board_height-4*pac_size-line_thickness/2),(0.667*board_width-gap-line_thickness/2,board_height-4*pac_size-line_thickness/2)))


        self.hor.append(((0.333*board_width-4*pac_size,9*pac_size-line_thickness+1+gap),(0.333*board_width,9*pac_size-line_thickness+1+gap)))
        self.hor.append(((0.333*board_width-4*pac_size,board_height-7*pac_size-gap+line_thickness/2-1),(0.333*board_width,board_height-7*pac_size-gap+line_thickness/2-1)))

        self.ver.append(((0.333*board_width-1-4*pac_size+line_thickness/2,9*pac_size-line_thickness+1+gap),(0.333*board_width-1-4*pac_size+line_thickness/2,board_height-7*pac_size-gap+line_thickness/2-1)))

        self.ver.append(((0.333*board_width-4*pac_size+gap,9*pac_size-line_thickness+1+2*gap),(0.333*board_width-4*pac_size+gap,board_height-7*pac_size-gap+line_thickness/2-1)))
        self.ver.append(((0.333*board_width,9*pac_size-line_thickness+1+gap),(0.333*board_width,board_height-7*pac_size-2*gap+line_thickness/2-1)))

        self.hor.append(((0.667*board_width-line_thickness/2+1,9*pac_size-line_thickness/2+1+gap),(0.667*board_width+4*pac_size,9*pac_size-line_thickness/2+1+gap)))
        self.hor.append(((0.667*board_width-line_thickness/2+1,board_height-7*pac_size-gap),(0.667*board_width+4*pac_size,board_height-7*pac_size-gap)))
        self.ver.append(((0.667*board_width+4*pac_size-line_thickness/2,9*pac_size-line_thickness/2+1+gap),(0.667*board_width+4*pac_size-line_thickness/2,board_height-7*pac_size-gap)))

        self.ver.append(((0.667*board_width+4*pac_size-line_thickness/2-gap,9*pac_size-line_thickness/2+1+2*gap),(0.667*board_width+4*pac_size-line_thickness/2-gap,board_height-7*pac_size-gap)))
        self.ver.append(((0.667*board_width,9*pac_size-line_thickness/2+1+gap),(0.667*board_width,board_height-7*pac_size-2*gap)))

        self.hor.append(((0.333*board_width,board_height-4*pac_size-gap-line_thickness/2),(0.667*board_width-gap,board_height-4*pac_size-gap-line_thickness/2)))     

        self.ver.append(((6.5*pac_size+line_thickness/2,3*pac_size),(6.5*pac_size+line_thickness/2,board_height/2+2.75*pac_size+line_thickness/2)))
        self.ver.append(((board_width-(6.5*pac_size+line_thickness/2),3*pac_size+gap),(board_width-(6.5*pac_size+line_thickness/2),board_height-pac_size)))

        self.hor.append(((pac_size+gap,board_height/2-0.75*pac_size-line_thickness/2-gap),(6.5*pac_size+line_thickness/2,board_height/2-0.75*pac_size-line_thickness/2-gap)))
        self.hor.append(((pac_size,board_height/2-0.75*pac_size-line_thickness/2-2*gap),(6.5*pac_size+line_thickness/2-gap,board_height/2-0.75*pac_size-line_thickness/2-2*gap)))
        self.hor.append(((pac_size+gap,board_height/2-0.75*pac_size-line_thickness/2-3*gap),(6.5*pac_size+line_thickness/2,board_height/2-0.75*pac_size-line_thickness/2-3*gap)))

        self.hor.append(((board_width-(6.5*pac_size+line_thickness/2),board_height/2+0.75*pac_size+line_thickness/2-1+gap),(board_width-pac_size-gap,board_height/2+0.75*pac_size+line_thickness/2-1+gap)))
        self.hor.append(((board_width-(6.5*pac_size+line_thickness/2)+gap,board_height/2+0.75*pac_size+line_thickness/2-1+2*gap),(board_width-pac_size,board_height/2+0.75*pac_size+line_thickness/2-1+2*gap)))        
        self.hor.append(((board_width-(6.5*pac_size+line_thickness/2),board_height/2+0.75*pac_size+line_thickness/2-1+3*gap),(board_width-pac_size-gap,board_height/2+0.75*pac_size+line_thickness/2-1+3*gap)))
        self.hor.append(((board_width-(6.5*pac_size+line_thickness/2)+gap,board_height/2+0.75*pac_size+line_thickness/2-1+4*gap),(board_width-pac_size,board_height/2+0.75*pac_size+line_thickness/2-1+4*gap)))
        self.ver.append(((board_width-(6.5*pac_size+line_thickness/2)+gap,board_height/2+0.75*pac_size+4*gap),(board_width-(6.5*pac_size+line_thickness/2)+gap,board_height-pac_size)))

        self.ver.append(((5*pac_size,board_height/2+0.75*pac_size+line_thickness/2-1+gap),(5*pac_size,board_height-pac_size)))
        self.ver.append(((5*pac_size-gap,board_height/2+0.75*pac_size+line_thickness/2-1),(5*pac_size-gap,board_height-pac_size-gap)))

        self.ver.append(((board_width-5*pac_size,3*pac_size),(board_width-5*pac_size,board_height/2-0.75*pac_size-line_thickness/2-gap)))
        self.ver.append(((board_width-5*pac_size+gap,3*pac_size+gap),(board_width-5*pac_size+gap,board_height/2-0.75*pac_size-line_thickness/2)))
                
        self.ver.append(((0.5*board_width,board_height/2+2*pac_size),(0.5*board_width,board_height-4*pac_size-2*gap-line_thickness/2)))
        self.hor.append(((0.333*board_width,board_height-4*pac_size-2*gap-line_thickness/2),(0.5*board_width-gap,board_height-4*pac_size-2*gap-line_thickness/2)))
        self.hor.append(((0.5*board_width-line_thickness/2+1,board_height-4*pac_size-2*gap-line_thickness/2),(0.667*board_width,board_height-4*pac_size-2*gap-line_thickness/2)))

        self.ver.append(((0.333*board_width+gap,3*pac_size+gap+1-line_thickness/2),(0.333*board_width+gap,board_height-4*pac_size-2*gap-line_thickness/2-gap)))
        self.ver.append(((0.667*board_width-gap,3*pac_size+gap+1-line_thickness/2),(0.667*board_width-gap,board_height-4*pac_size-2*gap-line_thickness/2-gap)))
        self.hor.append(((board_width/2+2.5*pac_size,board_height-4*pac_size-2*gap-line_thickness-gap),(0.667*board_width-2*gap,board_height-4*pac_size-2*gap-line_thickness-gap)))
        self.ver.append(((board_width/2-2.5*pac_size-gap-line_thickness/2,3*pac_size+2*gap),(board_width/2-2.5*pac_size-gap-line_thickness/2,board_height-4*pac_size-2*gap-line_thickness/2-gap)))
        self.hor.append(((board_width/2-2.5*pac_size-line_thickness/2,3*pac_size+2*gap),(0.667*board_width-gap,3*pac_size+2*gap)))
        self.hor.append(((board_width/2-2.5*pac_size-line_thickness/2-gap,3*pac_size+3*gap),(0.667*board_width-2*gap,3*pac_size+3*gap)))
        self.hor.append(((board_width/2-2.5*pac_size-line_thickness/2,3*pac_size+4*gap-line_thickness+4),(0.667*board_width-gap,3*pac_size+4*gap-line_thickness+4)))
        self.ver.append(((0.667*board_width-2*gap,3*pac_size+5*gap-line_thickness+4),(0.667*board_width-2*gap,board_height-4*pac_size-2*gap-line_thickness/2-gap)))

        self.hor.append(((pac_size+2*gap+line_thickness/2,board_height-4*pac_size),(0.333*board_width+line_thickness/2,board_height-4*pac_size)))
        self.hor.append(((0.667*board_width-line_thickness/2+1,board_height-4*pac_size),(board_width-3.5*gap,board_height-4*pac_size)))

        self.hor.append(((pac_size+2*gap+line_thickness/2,board_height-4*pac_size-gap),(0.333*board_width+line_thickness/2-gap,board_height-4*pac_size-gap)))
        self.hor.append(((0.667*board_width-line_thickness/2+1+gap,board_height-4*pac_size-gap),(board_width-3.5*gap,board_height-4*pac_size-gap)))

        self.ver.append(((0.333*board_width+line_thickness/2-2*gap,board_height-7*pac_size+line_thickness/2-1),(0.333*board_width+line_thickness/2-2*gap,board_height-4*pac_size-gap)))
        self.ver.append(((pac_size+4*gap+line_thickness/2,3*pac_size+gap),(pac_size+4*gap+line_thickness/2,board_height-4*pac_size-gap)))
        self.ver.append(((pac_size+5*gap+line_thickness/2-2,3*pac_size),(pac_size+5*gap+line_thickness/2-2,board_height-4*pac_size-2*gap)))
        self.ver.append(((pac_size+6*gap+line_thickness/2-2,3*pac_size),(pac_size+6*gap+line_thickness/2-2,9*pac_size-line_thickness+1)))
        self.ver.append(((pac_size+7*gap+line_thickness/2-2,3*pac_size+gap),(pac_size+7*gap+line_thickness/2-2,9*pac_size-line_thickness+1+gap)))

        self.ver.append(((board_width-4.5*gap,3*pac_size),(board_width-4.5*gap,board_height-4*pac_size-2*gap)))
        self.ver.append(((board_width-5.5*gap,3*pac_size+gap),(board_width-5.5*gap,board_height-4*pac_size-gap)))
        self.ver.append(((board_width-6.5*gap,3*pac_size),(board_width-6.5*gap,9*pac_size-line_thickness+1)))
        self.ver.append(((board_width-7.5*gap,3*pac_size+gap),(board_width-7.5*gap,9*pac_size-line_thickness+1+gap)))
        self.ver.append(((0.667*board_width-line_thickness/2+1+2*gap,board_height-7*pac_size+line_thickness/2-1),(0.667*board_width-line_thickness/2+1+2*gap,board_height-4*pac_size-gap)))

        x = pac_size
        index = 0
        while(x<board_width-pac_size):
            x += 30
            index += 1
            if index==38:
                break
            if index==2 or index==3:
                self.rect.append([x,4*pac_size+60,1])
                self.rect.append([x,4*pac_size+60+gap,1])
                self.rect.append([x,4*pac_size+60+2*gap,1])
            if( not(index==5 or index==8 or index==9 or index==12 or index==26 or index==29  or index==32 or index==35 or index>=38)):
                self.rect.append([x,4*pac_size,1])
            if index<=37 and index>=4:
                if (index>=4 and index<=13) or index>=25:  
                    self.rect.append([x,4*pac_size+330+gap,1])
                else:
                    self.rect.append([x,4*pac_size+370,1])
            if index>=13 and index<=25:
                self.rect.append([x,4*pac_size+320,1])
                self.rect.append([x,board_height-2*pac_size,1])
            if index>=14 and index<=24 :
                if index<=23 and index>14:
                    self.rect.append([x+10,4*pac_size+40,1])
                if index>15 and index<=23:
                    self.rect.append([x,4*pac_size+40+gap,1])
                    self.rect.append([x,4*pac_size+40+2*gap,1])
                    self.rect.append([x,4*pac_size+40+3*gap,1])
                if index!=19:
                    self.rect.append([x,4*pac_size+320-gap,1])
            if index>=35:
                self.rect.append([x,4*pac_size+8*30,1])
                self.rect.append([x,4*pac_size+8*30+gap,1])
                self.rect.append([x,4*pac_size+8*30+2*gap,1])

        self.rect.append([pac_size+16*30,4*pac_size+40+3*gap+60,1])
        self.rect.append([pac_size+16*30,4*pac_size+40+3*gap+30,1])
        self.rect.append([pac_size+23.5*30,4*pac_size+40+3*gap+60,1])
        self.rect.append([pac_size+23.5*30,4*pac_size+40+3*gap+30,1])
        self.rect.append([pac_size+23.5*30-gap,4*pac_size+40+3*gap+45,1])
        self.rect.append([pac_size+13*30,board_height-2*pac_size-40,1])
        self.rect.append([pac_size+25*30,board_height-2*pac_size-40,1])

        self.rect.append([pac_size+9.5*30,4*pac_size+10*30,1])
        self.rect.append([pac_size+10.5*30,4*pac_size+10*30,1])
        self.rect.append([pac_size+11.5*30,4*pac_size+10*30,1])
        self.rect.append([pac_size+11.5*30,4*pac_size+11*30,1])

        self.rect.append([0.667*board_width+30,4*pac_size+10*30,1])
        self.rect.append([0.667*board_width+60,4*pac_size+10*30,1])
        self.rect.append([0.667*board_width+90,4*pac_size+10*30,1])
        self.rect.append([0.667*board_width+30,4*pac_size+11*30,1])

        for y in range(4*pac_size+30,4*pac_size+360,30):
            self.rect.append([pac_size+7*30-gap,y,1])
            self.rect.append([pac_size+7*30,y,1])
             
            if y>=4*pac_size+60 and y!=4*pac_size+4*30:
                self.rect.append([pac_size+7*30-2*gap,y,1])
            if y<=4*pac_size+150:
                self.rect.append([board_width-2*gap-10,y,1])
                self.rect.append([board_width-gap-10,y,1])
                if y!=4*pac_size+90:
                    self.rect.append([50,y,1])
            if y<=4*pac_size+270:    
                self.rect.append([board_width-9*gap-10,y,1])
                self.rect.append([pac_size+7*30+4*gap,y,1])
                if y!=4*pac_size+270:
                    if y>=4*pac_size+180:
                        self.rect.append([board_width-8*gap-5,y+10,1])
                        self.rect.append([board_width-7*gap-5,y+10,1])
                        self.rect.append([pac_size+295,y+10,1])
                        self.rect.append([pac_size+295+gap,y+10,1])
                    else:
                        self.rect.append([board_width-8*gap-5,y-10,1])
                    self.rect.append([pac_size+14.5*30,y+10,1])

            if y<=4*pac_size+120:
                self.rect.append([board_width-7*gap-5,y,1])
                self.rect.append([pac_size+7*30+2*gap,y,1])
                self.rect.append([pac_size+7*30+3*gap,y,1])
            
            if y<=4*pac_size+8*30:
                self.rect.append([board_width-3*gap-10,y,1])
            self.rect.append([board_width-4*gap-10+3,y,1])
            self.rect.append([board_width-5*gap-10+5,y,1])
            self.rect.append([board_width-6*gap-10+5,y,1]) 

        for y in range(4*pac_size+8*30,4*pac_size+16*30,30):    
            self.rect.append([2*pac_size,y,1])
            self.rect.append([2*pac_size+gap,y,1])
            if y!=4*pac_size+8*30 and y!=4*pac_size+9*30 and y!=4*pac_size+12*30 and y!=4*pac_size+13*30:
                self.rect.append([board_width-3*gap-10,y,1])


        for y in range(4*pac_size,4*pac_size+360,30):
            self.rect.append([pac_size+7*30+gap,y,1])

        self.rect.append([board_width-4*gap-30,4*pac_size+330,1])
        self.rect.append([pac_size+7*30+gap/2,4*pac_size+330,1])        



    def draw(self):
        for vlines in self.ver:
            pygame.draw.line(screen,blue,vlines[0],vlines[1],line_thickness)
        for hlines in self.hor:
            pygame.draw.line(screen,blue,hlines[0],hlines[1],line_thickness)


        for rect in self.rect:
            if rect[2]==1:
                pygame.draw.rect(screen,white,(rect[0],rect[1],10,10),0)

    
