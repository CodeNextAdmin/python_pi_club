from sense_hat import SenseHat
import time
import random


sense = SenseHat()

#declare color tuples
r = (255,0,0)
w = (255,255,255)
k = (0,0,0)


left =[   
w,w,w,w,w,w,w,w,
w,w,r,w,w,w,w,w,
w,r,r,w,w,w,w,w,
r,r,r,r,r,r,r,w,
w,r,r,w,w,w,w,w,
w,w,r,w,w,w,w,w,
w,w,w,w,w,w,w,w,
w,w,w,w,w,w,w,w
]

right =[   
w,w,w,w,w,w,w,w,
w,w,w,w,w,r,w,w,
w,w,w,w,w,r,r,w,
w,r,r,r,r,r,r,r,
w,w,w,w,w,r,r,w,
w,w,w,w,w,r,w,w,
w,w,w,w,w,w,w,w,
w,w,w,w,w,w,w,w
]

down =[   
w,w,w,w,w,w,w,w,
w,w,w,r,w,w,w,w,
w,w,w,r,w,w,w,w,
w,w,w,r,w,w,w,w,
w,w,w,r,w,w,w,w,
w,r,r,r,r,r,w,w,
w,w,r,r,r,w,w,w,
w,w,w,r,w,w,w,w
]

up =[   
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
arrows = [up, down, left, right]


#variable to hold score
score = 0


while True:
    
    time.sleep(.8)
    sense.set_pixels(up)