import pygame 
import random 
import time
import math
screen=pygame.display.set_mode((500,500))

class circles :
    def __init__(self,x,y,size,color):
        self.x=x
        self.y=y
        self.pos=(x,y)
        self.size=size
        self.color=color
        self.radius= size/2

    def draw_base (self):
        global screen
        pygame.draw.circle(screen,self.color,self.pos,self.radius)

    def half_circle(self,st_angle=0.0,ed_angle=0.5):
        global screen
        pygame.draw.arc(screen,self.color,(self.x,self.y,self.size,self.size),st_angle,ed_angle)

class pannel :
    def __init__ (self,x,y,width,height,color ):
        self.pos=(x,y)
        self.x=x
        self.y=y
        self.width=width
        self.height=height
        self.color=color
        self.rect=pygame.rect.Rect(x,y,width,height)
    def outline_render (self):
        pygame.draw(screen, (100,100,100), self.rect, -3)

    def render (self):
        pygame.draw.rect(screen, self.color,self.rect)

class pannel_press (pannel):
    def __init__ (self,x,y,width,height,color):
        super().__init__(x,y,width,height,color)
        
    def check_click (self):
        if self.rect.collidepoint(pygame.mouse.get_pos()) and pygame.mouse.get_just_pressed()[0] :
            return True
        else:
            return False

    def outline_render(self): #this may have some problems because pygame does not have a direct function 
        pygame.draw.rect(screen, self)

    def render (self):
        pygame.draw.rect(screen,self.color,self.rect)


class text ():
    def __init__ (self,x,y,text, color=(10,10,10), font="arial",size=20):
        self.x=x
        self.y=y
        self.pos=(x,y)
        self.text=text
        self.color=color
        self.font=font 
        self.size=size 

    def render (self):
        if self.font == "df":
            font="arial"
        else: 
            font=self.font      
        text=pygame.font.SysFont(font,self.size,True,False)
        text_surf=text.render(self.text,True,self.color)
        screen.blit(text_surf,(self.x,self.y))
        


class particles ():
    def __init__ (self,x,y,pos,surface,behavior ):
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
                pass

            elif self.behavior == "slow_fall":
                pass


            elif self.behavior == "slow_rise":
                pass


            else: 
                print(f"error  { self.behavior} not reconized")

"""class menus():
    def __init__():
        self."""
