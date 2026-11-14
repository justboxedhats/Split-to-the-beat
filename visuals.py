import pygame 
import random 
import time
screen.pygame.

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

class pannel_press (pannel):
    def __init__ (self):
        super().__init__()
        
    def check_click (self):
        if self.rect.collidepoint(pygame.mouse.get_pos()) and pygame.mouse.get_just_pressed()[0] :
            return True
        else:
            return False

    def outline_render(self): #this may have some problems because pygame does not have a direct function 
        pygame.draw.rect(screen, self)

    def render (self):
        pygame






class text ():
    def __init__ (x,y,text, color, font="arial",size=20):
        self.x=x
        self.y=y
        self.text=text
        self.color=color
        self.font=font 
        self.size=size 

    def render (self):
        if self.font == "df":
            font="arial"
        else: 
            font=self.font        
        # calls pygame function to render 


class particles ():
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

class menus():
    def __init__():
        self.
