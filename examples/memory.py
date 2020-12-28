from sense_hat import SenseHat
import time
import random

sense = SenseHat()
sense.clear()

delay = 0.8

#declare color tuples
r = (255,0,0)
w = (255,255,255)
k = (0,0,0)

no_arrow = [
w,w,w,w,w,w,w,w,
w,w,w,w,w,w,w,w,
w,w,w,w,w,w,w,w,
w,w,w,w,w,w,w,w,
w,w,w,w,w,w,w,w,
w,w,w,w,w,w,w,w,
w,w,w,w,w,w,w,w,
w,w,w,w,w,w,w,w
]

left_arrow =[   
w,w,w,w,w,w,w,w,
w,w,r,w,w,w,w,w,
w,r,r,w,w,w,w,w,
r,r,r,r,r,r,r,w,
w,r,r,w,w,w,w,w,
w,w,r,w,w,w,w,w,
w,w,w,w,w,w,w,w,
w,w,w,w,w,w,w,w
]

right_arrow =[   
w,w,w,w,w,w,w,w,
w,w,w,w,w,r,w,w,
w,w,w,w,w,r,r,w,
w,r,r,r,r,r,r,r,
w,w,w,w,w,r,r,w,
w,w,w,w,w,r,w,w,
w,w,w,w,w,w,w,w,
w,w,w,w,w,w,w,w
]

down_arrow =[   
w,w,w,w,w,w,w,w,
w,w,w,r,w,w,w,w,
w,w,w,r,w,w,w,w,
w,w,w,r,w,w,w,w,
w,w,w,r,w,w,w,w,
w,r,r,r,r,r,w,w,
w,w,r,r,r,w,w,w,
w,w,w,r,w,w,w,w
]

up_arrow =[   
w,w,w,r,w,w,w,w,
w,w,r,r,r,w,w,w,
w,r,r,r,r,r,w,w,
w,w,w,r,w,w,w,w,
w,w,w,r,w,w,w,w,
w,w,w,r,w,w,w,w,
w,w,w,r,w,w,w,w,
w,w,w,r,w,w,w,w
]

#list of arrows
arrows = ["up", "right", "down", "left"]

#will hold the current pattern
current_pattern = []

#player_patter
player_pattern =[]

#a boolean that tracks if the player is playing
player_turn = False

#level, start at 1
level = 1

#submit guess
def submit_guess():
    global player_pattern, current_pattern, player_turn

    if current_pattern == player_pattern:
        sense.show_message("LEVEL CLEAR", text_colour=r, back_colour=w, scroll_speed=0.05)
        player_turn = False

    else:
        sense.show_message("Game Over")

#this function creates a new pattern, increasing in difficuly
def next_level():
    global player_turn, level, current_pattern, player_pattern

    print("LEVEL " + str(level))
    current_pattern = [] #clear it before refilling
    player_pattern =[]

    sense.show_message( str(level), scroll_speed=.2)

    #build the new pattern with random choices from the arrows list
    for i in range(level+2):
        current_pattern.append(random.choice(arrows))

    print(current_pattern)

    for arrow in current_pattern:

        if arrow == "up":
            sense.set_pixels(up_arrow)

        elif arrow == "right":
            sense.set_pixels(right_arrow)

        elif arrow == "down":
            sense.set_pixels(down_arrow)

        else:
            sense.set_pixels(left_arrow)
     
        time.sleep(delay)
        sense.set_pixels(no_arrow)

        #prevent two repeating arrows from appearing as one.
        time.sleep(0.2)

    player_turn = True
    level = level + 1

#begin the game
next_level()

#main game loop
while True:

    if player_turn:
        
        sense.show_letter("?")

        for event in sense.stick.get_events():
            # print(event.direction, event.action)

            if event.action == "pressed" and event.direction != "middle":
                #store each event in player_pattern
                player_pattern.append(event.direction)

            if event.action == "released" and event.direction == "middle":
                print("player: " + str(player_pattern))
                print("Comptuer : " + str(current_pattern))
                submit_guess()

    else:
        next_level()

 
 
