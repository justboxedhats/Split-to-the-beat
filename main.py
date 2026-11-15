import pygame 
import visuals 
import sound 
import time 
from levels import tutorial  
pygame.init()
screen=pygame.display.set_mode((500,200))
# settinsg varables 
flags=[]
runnning=True
pause=False
input_list=[]
level="home"
level_beats={}
level_song=None
level_bpm=None
health=None
bg_color=(200,200,200)


def per2pix (part,whole="s_w") :
    m_whole=whole
    if whole == "s_h":
        m_whole= screen.get_height()
    elif whole == "s_w":
        m_whole= screen.get_width()
    print(m_whole/part)
    return int(m_whole/part)

def load_level ():
    # the conditions may problamatic 
    # so I might work on it later :(
    # so I can get a prototype as soon as 
    # possable 
    imported_level=tutorial
    level_song=imported_level["song_filepath"]
    del imported_level["song_filepath"]
    level_bpm=imported_level["song_bpm"]
    del imported_level["song_bpm"]
    level_beats=imported_level

def start_level(level_num):
    bg_color=(20,20,20)
    level=str(level_num)
    pause=True


    
def check_acreacy (beat):

        if  abs(beat-time.current)<0.15: # perfect 
            print("perfect")
            score+=100
            del level_beats["w"][beat]
            # delets teh beat from other menus 
            # renders particles and circle 
        elif abs(beat-time.current)>0.15 and abs(beat-time.current)<0.35:# great 
            print("great")
        elif abs(beat-time.current)>0.35 and abs(beat-time.current)<0.65:# good 
            print("good")
        elif abs(beat-time.current)>0.65 and abs(beat-time.current)<0.9:# ok
            print("ok")
        elif abs(beat-time.current)<0.9 and abs(beat-time.current)> 1.1 :# miss
            # miss sound 
            print("input miss")
            health-=1
    
        elif beat-time.current < -1.5:#miss :(
            print("automatic miss")
            health-=1 


        # loads sounds
        # it determens the  acreacy of the input and ranks it(miss,good, great, perrfcet)
        # changes varables (points, health, beats list )    


while runnning :

    events=pygame.event.get()
    for event in events:
        if event == pygame.QUIT:
            running=False 
        if event == pygame.K_ESCAPE:
            # I'm not sure if a list of inputs would be best :( \
            # but it will have to due for now  
            #add to input 
            input_list.append("escape")
        else:
            if "escape" in input_list:
                input_list.remove("escape")
        if event == pygame.K_a: 
            input_list.append("a")
        else:
            if "a" in input_list:
                input_list.remove("a")
        if event == pygame.K_LEFT:
            input_list.append("left")
        else:
            if "left" in input_list:
                input_list.remove("left")
        if event == pygame.K_d:
                input_list.append("d")
        else:
            if "d" in input_list:
                input_list.remove("d")
        if event == pygame.K_RIGHT:
            input_list.append("right")
        else:
            if "right" in input_list:
                input_list.remove("right")
        if event == pygame.K_w:
            input_list.append("w")
        else:
            if "w" in input_list:
                input_list.remove("w")
        if event == pygame.K_UP:
            input_list.append("up")
        else:
            if "up" in input_list:
                input_list.remove("up")
        if event == pygame.K_s:
            input_list.append("s")
        else:
            if "s" in input_list:
                input_list.remove("s")
        if event == pygame.K_DOWN:
            input_list.append("down")
        else:
            if "down" in input_list:
                input_list.remove("down")

    if level=="home":
        screen.fill(bg_color)
        # buttons
            # play
            # quit  
        play_button=visuals.pannel_press(per2pix(35), per2pix(25,"s_h"),per2pix(30),per2pix(10,"s_h"),(100,200,100) )
        play_button.render()
        play_text=visuals.text(per2pix(35),per2pix(25,"s_h"),"Play!",(100,200,100))
        play_text.render()

        quit_button=visuals.pannel_press(per2pix(40),per2pix(35,"s_h"),per2pix(20),per2pix(10,"s_h"),(100,200,100))
        quit_button.render()
        quit_text=visuals.text(per2pix(40),per2pix(35,"s_h"),"QUIT",(100,200,100))
        quit_text.render()
        
        # check buttons
        if play_button.check_click():
            start_level(0)

        if quit_button.check_click():
            running=False 
        

        #images 
            # title
        title_text=visuals.text(per2pix(45),per2pix(10,"s_h"),(200,200,250))

    elif level == "tutorial":
        screen.fill(bg_color)
        if "pause" in flags :
            if "start" in flags:
                pass
                # loads acutal pause menu 
                # checks contions to turn off pause 

            else:
                pass
                # loads start menu 
                # button to add pause into flags 
                # then turn off pause 


        else: # the game is running 
            print("level") 
            # loads runs function 
            

            # checks user imputs 
            if "w" in input_list or "up" in input_list :
                for beat in  level_beats["w"].keys():
                    check_acreacy(beat)                    
            if "s" in input_list or "down" in input_list :
                for beat in  level_beats["down"].keys():
                    check_acreacy(beat)              
            if "d" in input_list or "left" in input_list :
                for beat in  level_beats["left"].keys():
                    check_acreacy(beat)              
            if "a" in input_list or "right" in input_list :
                for beat in  level_beats["right"].keys():
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





pygame.QUIT()
