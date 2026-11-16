import pygame 
import visuals 
import sound 
import time 
from levels import tutorial_lev 
pygame.init()
screen=pygame.display.set_mode((500,500),pygame.RESIZABLE)
# settinsg varables 
flags=[]
running=True
pause=False
level="home"
level_song=None
level_bpm=None
health=None
score=0
bg_color=(200,200,200)
beat_time_offset=2# time it takes of a beat reach the guide
circle_display_distance=20# under to place the postion of the guide circles 
level_beats={}
input_beats={"up":{},"down":{},"right":{},"left":{}}
render_beats={}

def per2pix (part,whole="s_w") :
    m_whole=whole
    if whole == "s_h":
        m_whole= screen.get_height()
    elif whole == "s_w":
        m_whole= screen.get_width()
    #print(f"perpix  {m_whole/part}")
    return int((part/100)*m_whole)

def load_level ():
    # the conditions may problamatic (the giant if chains)
    # so I might work on it later :(
    # so I can get a prototype as soon as 
    # possable 
    imported_level=tutorial_lev
    level_song=imported_level["song"]
    del imported_level["song"]
    level_bpm=imported_level["bpm"]
    del imported_level["bpm"]
    level_beats=imported_level

    # make the beat list 

    for beat in level_beats.keys():
        # the bpm may be used to deren the amount of time for trh player to see the beats 
        # renders 2 seconds early 
        input_distance= circle_display_distance# may not be nesscary 
        #speed= distance/time
        beat_speed=input_distance/beat_time_offset
        render_beats[beat-beat_time_offset]=level_beats[beat]
        #input_beats: direction>time>type
        if "1" in level_beats[beat] and "o" in level_beats[beat]:   
            input_beats["up"][beat]= "o"
        if "1" in level_beats[beat] and "O" in level_beats[beat]:
            input_beats["up"][beat]= "O"
        if "1" in level_beats[beat] and "c" in level_beats[beat]:
            input_beats["up"][beat]= "c"
        if "1" in level_beats[beat] and "C" in level_beats[beat]:
            input_beats["up"][beat]= "C"
        if "1" in level_beats[beat] and "g" in level_beats[beat]:
            input_beats["up"][beat]= "g"
        if "2" in level_beats[beat] and "o" in level_beats[beat]:
            input_beats["up"][beat]= "o"
        if "2" in level_beats[beat] and "O" in level_beats[beat]:
            input_beats["up"][beat]= "O"
        if "2" in level_beats[beat] and "c" in level_beats[beat]:
            input_beats["up"][beat]= "c"
        if "2" in level_beats[beat] and "C" in level_beats[beat]:
            input_beats["up"][beat]= "C"
        if "2" in level_beats[beat] and "g" in level_beats[beat]:
            input_beats["up"][beat]= "g"
        if "3" in level_beats[beat] and "o" in level_beats[beat]:
            input_beats["up"][beat]= "o"
        if "3" in level_beats[beat] and "O" in level_beats[beat]:
            input_beats["up"][beat]= "O"
        if "3" in level_beats[beat] and "c" in level_beats[beat]:
            input_beats["up"][beat]= "c"
        if "3" in level_beats[beat] and "C" in level_beats[beat]:
            input_beats["up"][beat]= "C"
        if "3" in level_beats[beat] and "g" in level_beats[beat]:
            input_beats["up"][beat]= "g"
        if "4" in level_beats[beat] and "o" in level_beats[beat]:
            input_beats["up"][beat]= "o"
        if "4" in level_beats[beat] and "O" in level_beats[beat]:
            input_beats["up"][beat]= "O"
        if "4" in level_beats[beat] and "c" in level_beats[beat]:
            input_beats["up"][beat]= "c"
        if "4" in level_beats[beat] and "C" in level_beats[beat]:
            input_beats["up"][beat]= "C"
        if "4" in level_beats[beat] and "g" in level_beats[beat]:
            input_beats["up"][beat]= "g"                    

        #print(f" input; {input_beats} render {render_beats}")
        # coutculates the amount it takes for a beat from the 
        # top or sides to reach the circle guides 
        # then generates the time for the player to make a input 
        # and then another list that is set earlyer based off of the 

def start_level(level_num):
    global bg_color,level,pause
    bg_color=(20,20,20)
    level=str(level_num)
    pause=True

def player_circle():

    # renders guide

    top_guide_circle=visuals.circles(per2pix(50),per2pix(20),per2pix(3),(100,100,100))
    bottom_guide_circle=visuals.circles(per2pix(50),per2pix(80),per2pix(3),(100,100,100))
    right_guide_circle=visuals.circles(per2pix(20),per2pix(50),per2pix(3),(100,100,100))
    left_guide_circle=visuals.circles(per2pix(80),per2pix(50),per2pix(3),(100,100,100))

        #renders guides

    top_guide_circle.draw_base()
    bottom_guide_circle.draw_base()
    right_guide_circle.draw_base()
    left_guide_circle.draw_base()


    # checks user imputs 
    #                    print(input_beats)
    if "w" in input_beats or "up" in input_beats :
        r_half_cirle=visuals.circles(per2pix(50),per2pix(circle_display_distance,"s_h"),per2pix(7),(250,250,250))
        r_half_cirle.half_circle(-1.5,1.5)
        l_half_circle=visuals.circles(per2pix(50),per2pix(100-circle_display_distance,"s_h"),per2pix(7),(250,250,250))
        l_half_circle.half_circle(1.5,-1.5)
        # right up
    elif "s" in input_beats or "down" in input_beats :
        r_half_cirle=visuals.circles(per2pix(50),per2pix(100-circle_display_distance,"s_h"),per2pix(7),(250,250,250))
        r_half_cirle.half_circle(-1.5,1.5)
        l_half_circle=visuals.circles(per2pix(50),per2pix(circle_display_distance,"s_h"),per2pix(7),(250,250,250))
        l_half_circle.half_circle(1.5,-1.5)
        #right down      
    elif "d" in input_beats or "left" in input_beats:
        r_half_cirle=visuals.circles(per2pix(100-circle_display_distance),per2pix(50,"s_h"),per2pix(7),(250,250,250))
        r_half_cirle.half_circle(3,0)
        l_half_circle=visuals.circles(per2pix(circle_display_distance),per2pix(50,"s_h"),per2pix(7),(250,250,250))
        l_half_circle.half_circle(0,3)
        # up left            
    elif "a" in input_beats or "right" in input_beats :
        r_half_cirle=visuals.circles(per2pix(circle_display_distance),per2pix(50,"s_h"),per2pix(7),(250,250,250))
        r_half_cirle.half_circle(3,0)
        l_half_circle=visuals.circles(per2pix(100-circle_display_distance),per2pix(50,"s_h"),per2pix(7),(250,250,250))
        l_half_circle.half_circle(0,3)
        # up right

    else:
        main_circle=visuals.circles(per2pix(50),per2pix(50,"s_h"),per2pix(7),(250,250,250))
        main_circle.draw_base()

        #load regular cirlcle at the center of the screen





    
def check_acreacy (beat):
        global score , health
        # intended to use time.time.current()
        if  abs(beat-(pygame.time.get_ticks()/1000))<0.15: # perfect 
            print("perfect")
            score+=100
            del input_beats["up"][beat]#hmm
            # delets teh beat from other menus 
            # renders particles and circle 
        elif abs(beat-(pygame.time.get_ticks()/1000))>0.15 and abs(beat-(pygame.time.get_ticks()/1000))<0.35:# great 
            print("great")
        elif abs(beat-(pygame.time.get_ticks()/1000))>0.35 and abs(beat-(pygame.time.get_ticks()/1000))<0.65:# good 
            print("good")
        elif abs(beat-(pygame.time.get_ticks()/1000))>0.65 and abs(beat-(pygame.time.get_ticks()/1000))<0.9:# ok
            print("ok")
        elif abs(beat-(pygame.time.get_ticks()/1000))<0.9 and abs(beat-(pygame.time.get_ticks()/1000))> 1.1 :# miss
            # miss sound 
            print("input miss")
            health-=1
    
        elif beat-(pygame.time.get_ticks()/1000) < -1.5:#miss :(
            print("automatic miss")
            health-=1 


        # loads sounds
        # it determens the  acreacy of the input and ranks it(miss,good, great, perrfcet)
        # changes varables (points, health, beats list )    


while running :

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running=False
            print("attempted to quit") 
        if event.type == pygame.KEYDOWN:
            if event.type == pygame.K_ESCAPE:
                # I'm not sure if a list of inputs would be best :( 
                # but it will have to due for now  
                #add to input 
                input_beats.append("escape")
            else:
                if "escape" in input_beats:
                    input_beats.remove("escape")
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_a:  
                input_beats.append("a")
            else:
                if "a" in input_beats:
                    input_beats.remove("a")
            if event.key == pygame.K_LEFT:
                input_beats.append("left")
                print("left")
            else:
                if "left" in input_beats:
                    input_beats.remove("left")
            if event.key == pygame.K_d:
                    input_beats.append("d")
            else:
                if "d" in input_beats:
                    input_beats.remove("d")
            if event.key == pygame.K_RIGHT:
                input_beats.append("right")
                print("right")
            else:
                if "right" in input_beats:
                    input_beats.remove("right")
            if event.key == pygame.K_w:
                input_beats.append("w")
            else:
                if "w" in input_beats:
                    input_beats.remove("w")
            if event.key == pygame.K_UP:
                input_beats.append("up")
                print("up")
            else:
                if "up" in input_beats:
                    input_beats.remove("up")
            if event.key == pygame.K_s:
                input_beats.append("s")
            else:
                if "s" in input_beats:
                    input_beats.remove("s")
            if event.key == pygame.K_DOWN:
                input_beats.append("down")
                print("down")
            else:
                if "down" in input_beats:
                    input_beats.remove("down")

    if level=="home": # --------- menu mannager 
        screen.fill(bg_color)
        print(f"sc_w {screen.get_width()} ,  sc_h {screen.get_height()}")
        # buttons
              
        # play
        play_button=visuals.pannel_press(per2pix(35), per2pix(25,"s_h"),per2pix(30),per2pix(10,"s_h"),(100,200,100) )
        play_button.render()
        play_text=visuals.text(per2pix(35),per2pix(25,"s_h"),"Play!",(0,0,0))
        play_text.render()

        # quit
        quit_button=visuals.pannel_press(per2pix(40),per2pix(40,"s_h"),per2pix(20),per2pix(10,"s_h"),(100,200,100))
        quit_button.render()
        quit_text=visuals.text(per2pix(40),per2pix(35,"s_h"),"QUIT",(0,0,0))
        quit_text.render()
        
        # check buttons
        if play_button.check_click():
            start_level("tutorial")
            load_level()

        if quit_button.check_click():
            running=False 
        

        #images 
            # title
        title_text=visuals.text(per2pix(35),per2pix(10,"s_h"),"Split The Beat!",(100,100,250),None, 30)
        title_text.render()

    elif level == "tutorial":
        screen.fill(bg_color)
        if pause :
            if "start" in flags:
                pause_text=visuals.text(per2pix(45),per2pix(10,"s_h"),"paused",(250,250,200))
                pause_text.render()
                # loads acutal pause menu 
                # checks contions to turn off pause 
            else:
                pause_text=visuals.text(per2pix(45),per2pix(5,"s_h"),"start",(200,12,120),None,40)
                start_button=visuals.pannel_press(per2pix(45),per2pix(30,"s_h"),per2pix(30),per2pix(10,"s_h"),(200,200,250))
                pause_button_text=visuals.text(per2pix(45),per2pix(30,"s_h"), "begin", (100,180,100))
                start_button.render()
                pause_button_text.render()
                pause_text.render()

                # loads start menu 
                # button to add pause into flags 
                if start_button.check_click():
                    pause=False
                    # sets other varables for the level
                    # 
                    flags.append("start")
                # then turn off pause 


        else: # the game is running 
            # loads runs function 
            player_circle()


            render_beats={} 


            # checks user imputs 
            
            if "w" in input_beats or "up" in input_beats :

                for beat in  input_beats["up"].keys():
                    check_acreacy(beat)                  
            if "s" in input_beats or "down" in input_beats :
                for beat in  input_beats["down"].keys():
                    check_acreacy(beat)              
            if "d" in input_beats or "left" in input_beats :
                for beat in  input_beats["left"].keys():
                    check_acreacy(beat)              
            if "a" in input_beats or "right" in input_beats :
                for beat in  input_beats["right"].keys():
                    check_acreacy(beat)              

            # makes a list of beats to render based on the time
            # countculates the position of the notes based off age and speed of song
            # generates another notes that holds the beats's data (pos,colro, ect) 
            # sends the new list to the visuals file to generate the visuals(inside of the contidionals) 


            if "debug" in flags :
                # load visuals outlines 
                pass

            else:
                #renders everything 
                pass

    elif level == "level1":
        pass
    
    elif level == "None": # level_outline
        # the basic eliments to call a level 
        pass
    else :
        print(f" {level}  was not idenifyed as a ")




    pygame.display.flip()
