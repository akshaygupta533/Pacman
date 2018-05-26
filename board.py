import pygame
from settings import *

gap = 1.5*pac_size+line_thickness-1

class board:
    def __init__(self):
        self.ver = []
        self.hor = []
       
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
        self.ver.append(((board_width-(6.5*pac_size+line_thickness/2),board_height/2-2.75*pac_size-line_thickness/2),(board_width-(6.5*pac_size+line_thickness/2),board_height-pac_size)))

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

    def draw(self):
        for vlines in self.ver:
            pygame.draw.line(screen,blue,vlines[0],vlines[1],line_thickness)
        for hlines in self.hor:
            pygame.draw.line(screen,blue,hlines[0],hlines[1],line_thickness)