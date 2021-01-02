################################################
### Battleships coded by TeCoEd ################
################################################

'''Text to Speach from http://www.fromtexttospeech.com/'''

import random
import time
import pygame
from pygame.locals import *
from sense_hat import SenseHat

pygame.init()

pygame.display.set_mode((400, 400))
sense = SenseHat()
#sense.low_light = True '''enable to turn down brightness'''

global x #led position
global y
global score
x = 0
y = 0
score = 0

#################################################
######## Main Game Function #####################
#################################################

def main():
    global x
    global y
    global score

    '''Creates a hidden list of ships, ammo and sea'''
    Sea2 = []
   
    '''colours for ships and water'''
    ship = [160, 200, 140]
    water = [0, 0, 255]
    hit = [255, 0, 0]
    ammo = [255, 255, 0]

    '''Creates a random mix of ships and water in a new hidden list'''
    for i in Sea:
        item = random.randrange(1, 6)
        if item == 1:
            Sea2.append(ship)
        elif item == 2:
            Sea2.append(water)
        elif item == 3:
            Sea2.append(water)
        elif item == 4:
            Sea2.append(water)
        elif item == 5:
            Sea2.append(ammo) 
            
    '''Counts how many ships there are in the sea'''
    '''Looks through Sea2 list and counts number of ships'''
    number_of_ships = 0
    for entry in Sea2:
        if entry == [160, 200, 140]:
            number_of_ships = number_of_ships + 1
        
    print("Number of Ships to find", number_of_ships)
    sense.show_message(str(number_of_ships), text_colour=[255, 0, 0])
    '''Sets the number of torpedos to match the ships'''
    torpedos = number_of_ships + 5

    ####################################################### 
    ############ Code to control joystick #################
    ### controls the movement of the targetting system ####
    #######################################################
    
    while torpedos > 0:  
        for event in pygame.event.get():
            if event.type == KEYDOWN:
                sense.set_pixel(x, y, 0, 0, 0)  # Black 0,0,0 means OFF

                if event.key == K_DOWN and y < 7:
                    y = y + 1
                elif event.key == K_UP and y > 0:
                    y = y - 1
                elif event.key == K_RIGHT and x < 7:
                    x = x + 1
                elif event.key == K_LEFT and x > 0:
                    x = x - 1
                elif event.key == K_RETURN:
                    print (x)
                    print (y)
                    torpedos = torpedos - 1
                    print ("You have", torpedos, "torpedos")
                    
                    '''calculate your position on the grid as a 2d array'''
                    your_position = (y*8)+x

                    '''check what you hit and update the list'''

                    if Sea2[your_position] == ship:
                        print ("HIT")
                        Sea[your_position] = hit
                        sense.set_pixels(Sea)

                        ### sound ###

                        time.sleep(4)
                        
                        number_of_ships = number_of_ships - 1
                        print ("There are", number_of_ships, "left to find")
                                                

                        sense.show_message(str(number_of_ships), text_colour=[255, 0, 0])
                        
                        score = score + 1

                    elif Sea2[your_position] == water:
                        print ("MISS")
                        Sea[your_position] = water
                        sense.set_pixels(Sea)

                        ### sound ###

                        time.sleep(1)
                        
                    elif Sea2[your_position] == ammo:
                        
                        Sea[your_position] = ammo
                        sense.set_pixels(Sea)
                        torpedos = torpedos + 1

                        ### ammo up sound ###

                        time.sleep(3)
                        
                         
            sense.set_pixel(x, y, 0, 255, 0) #colour of pixel for location target
            
      

    print ("TEST GAME OVER")
    
    sense.show_message("Game Over", text_colour=[0, 255, 255], scroll_speed=0.07) #change to an animation


    time.sleep(2)

    #### add a score    

    time.sleep(1)

    sense.show_message(str(score), text_colour=[0, 200, 255])
    
    print ("There are", number_of_ships, "ships left")
       
    if number_of_ships == 0:
        print ("WELL DONE, TOP JOB") #ADD SOME ANIMATION
        sense.show_message("TOP JOB", text_colour=[0, 255, 255])

        time.sleep(3)
    else:
        print ("better luck next time") #ADD SOME ANIMATION


        
   ### end of game ###     
    

#####################################################
########### Intro to Game  ##########################
#####################################################                   
                    



import intro_ship                        

##### Welcome Message ###
sense.show_message("BATTLE SHIPS!", text_colour=[150, 150, 190], back_colour=[0, 0, 100])


play_game = True

### add main def and play again###
while play_game == True:
    play_again = 1
    print ("Welcome")
    time.sleep(1)

    S = [49, 49, 49] ### change to 000 
    '''Creates a grid of 64 blue pixels, the sea'''
    Sea = [
    S, S, S, S, S, S, S, S, S, S, S, S, S, S, S, S, S, S, S, S, S, S, S, S, S, S, S, S, S, S, S, S, S, S, S, S, S, S, S, S, S, S, S, S, S, S, S, S, S, S, S, S, S, S, S, S, S, S, S, S, S, S, S, S
    ]

    sense.set_pixels(Sea)
    time.sleep(1)

   

    
    for num in reversed(range(1,4)):
        sense.show_letter(str(num))
        time.sleep(1)

  

    ### Begin the main game ###
    main()

    ### Play again? ###
    print ("Would you like to play again? ")
      
    sense.load_image("choice.png")
    pygame.mixer.music.load("sounds/playagain.mp3")
    pygame.mixer.music.play() 
    while play_again == 1:
        for event in pygame.event.get():
            if event.type == KEYDOWN:
                    if event.key == K_DOWN:
                        play_again = 0
                        play_game = False
                        pygame.mixer.music.load("sounds/soon.mp3")
                        pygame.mixer.music.play()
                        print ("Bye Bye")
                        import end_animation
                        break

                    elif event.key == K_UP:
                        play_again = 0
                        
    
