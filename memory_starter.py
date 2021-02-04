from sense_hat import SenseHat
import time
import random


sense = SenseHat()

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


#variable to hold level
level = 0


while True:
    
    time.sleep(.3)
    sense.set_pixels(up_arrow)
    time.sleep(.3)
    sense.set_pixels(down_arrow)

