import pygame 
import random 

class circles ():
    def __init__(pos):
        self.pos=pos


class pannel ():
    def __init__ (x,y,width,height,color ):
        self.pos=(x,y)
        self.x=x
        self.y=y
        self.width=width
        self.height=height
        self.color=color
    def outline_render (self):
        pygame.draw(screen, (100,100,100), self.rect, -3)

    def render (self):
        self.rect=pygame.rect.Rect()



class parrticles ():
    def __init__ (x,y,pos ):
        self.x=x
        self.y=y
        self.pos=pos
        self.surface=surface
        self.behavior=behavior 
        self.volosity=None
        self.direction=None

    def render (self):
        if self.volosity == None :

            if self.behavior == "burst":

            elif self.behavior == "slow_fall":


            elif self.behavior == "slow_rise":


            else: 
                print(f"error  { self.behavior} not reconized")


