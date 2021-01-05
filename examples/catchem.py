"""Catchem is a game inspired by Egg drop by Dan Aldred"""

from sense_hat import SenseHat
import time
import random

sense = SenseHat()
sense.clear()

# set up the variables
game_over = False
 
catcher_x = 0 #will only need to move from L to R
score = 0
berry_x = random.randrange(0,7)
berry_y = 0

c = (0, 255, 255)  #cyan color
d = (255, 0 , 128 ) #dark pink for raspberries
o = (255, 128, 0)

"""
Setup the game
"""
sense.show_message("Catchem!", text_colour=o, scroll_speed=0.05)
sense.show_letter("3")
time.sleep(1)
sense.show_letter("2")
time.sleep(1)
sense.show_letter("1")
time.sleep(1)

sense.set_pixel(0, 7 , c)

def move_left():
    global catcher_x
    if catcher_x >= 1:
        catcher_x = catcher_x - 1
        

def move_right():
    global catcher_x
    if catcher_x < 7:
        catcher_x = catcher_x + 1
         
def update():
    global berry_x, berry_y, game_over
    sense.clear()
    sense.set_pixel(catcher_x, 7 , c)

    if berry_y < 7:
        berry_y = berry_y + 1
        sense.set_pixel(berry_x, berry_y, d)

    else:
        print("Dropped!")
        sense.show_message("Game Over!", text_colour=o, scroll_speed=0.05)
        game_over = True
        sense.show_message("Score: " + str(score))
         

def new_berry():
    global berry_x, berry_y, score
   
    sense.show_message( str(score), scroll_speed=.055, text_colour=d)
    berry_y = 0
    berry_x = random.randrange(0,7)


while game_over == False:
    
    for event in sense.stick.get_events():
        print(event)

        if event.action == "pressed" and event.direction == "left":
            move_left()

        if event.action == "pressed" and event.direction == "right":
            move_right()

    if catcher_x == berry_x and berry_y == 7:
        print("You got one!")
        score = score + 1
        new_berry()
    
    update()
    time.sleep(.2)
    

