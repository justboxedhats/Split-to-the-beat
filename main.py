import pygame 
import visuals 
import sound 
import time 
import tutorial from levels 
pygame.init()
screen=pygame.#screen
# settinsg varables 
flags=[]
runnning=True
pause=False
input_list=[]
level="tutorial"
level_beats={}
level_song=None
level_bpm=None
health=None


def per2pix (part,whole) :
    if whole == "s_h":
        part= screen.height()
    elif whole == "s_w":
        part= screen.width()
    return int(whole/part)

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
    
    
    

while runnning :

    events=pygame.event.get()
    for event in events:
        if event == pygame.QUIT:
            running=False 
        if event = pygame.K_ESCAPE:
            # I'm not sure if a list of inputs would be best :( \
            # but it will have to due for now  
            #add to input 
            input_list.append("escape")
        else: 
            input_list.pop("escape")
        if event == pygame.K_A:
            input_list.append("A")
        else:
            input_list.pop("A")
        if event == pygame.K_LEFT:
            input_list.append("left")
        else:
            input_list.pop("left")
        if event == pygame.K_D:
            input_list.append("D")
        else:
            input_list.pop("D")
        if event == pygame.K_RIGHT:
            input_list.append("right")
        else:
            input_list.pop("right")
        if event == pygame.K_W:
            input_list.append("W")
        else:
            input_list.pop("W")
        if event == pygame.K_UP:
            input_list.append("up")
        else:
            input_list.pop("up")
        if event == pygame.K_S:
            input_list.append("S")
        else:
            input_list.pop("S")
        if event == pygame.K_DOWN:
            input_list.append("down")
        else:
            input_list.pop("down")


    if level == "tutorial":
        if "pause" in flags :
            if "start" in flags:
                # loads acutal pause menu 
                # checks contions to turn off pause 

            else:
                # loads start menu 
                # button to add pause into flags 
                # then turn off pause 


        else: # the game is running 
            print("level") 
            # loads runs function 
            

            # checks user imputs 
            if "w" in input_list and "up" in input_list :
                for beat in  level_beats["w"].keys():

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
                    elif abs(beat-time.current)<0.9 and abs(beat-time.current)> 1.1 :
                        # miss sound 
                        print("input miss")
                        health-=1
                
                    elif beat-time.current < -1.5:#miss :(
                        print("automatic miss")
                        health-=1

                    


                # loads sounds
                # it determens the  acreacy of the input and ranks it(miss,good, great, perrfcet)
                # changes varables (points, health, beats list )

            # makes a list of beats to render based on the time
            # countculates the position of the notes based off age and speed of song
            # generates another notes that holds the beats's data (pos,colro, ect) 
            # sends the new list to the visuals file to generate the visuals(inside of the contidionals) 


            if "debug" in flags :
                # load visuals outlines 

            else:
                #renders everything 

    elif level == "level1"
    
    elif level == "None": # level_outline
        # the basic eliments to call a level 
    else :
    print(f" {level}  was not idenifyed as a ")





pygame.QUIT()