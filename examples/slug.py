from sense_hat import SenseHat
from time import sleep
from random import randint

sense = SenseHat()

# Variables ---------------------------
slug = [[2,4], [3,4], [4,4]]
white = (255, 255, 255)
blank = (0, 0, 0)
red = (255, 0, 0)
direction = "right"
vegetables = []
score = 0
pause = 0.5
dead = False 

# Functions ---------------------------
def draw_slug():
  for segment in slug:
    sense.set_pixel(segment[0], segment[1], white)

def move():
  global score, pause, dead
  remove = True
  
  # Find the last and first items in the slug list
  last = slug[-1]
  first = slug[0]
  next = list(last) # Create a copy of the last item

  # Find the next pixel in the direction the slug is currently moving
  if direction == "right":

    # Move along the column
    if last[0] + 1 == 8:
      next[0] = 0
    else:
      next[0] = last[0] + 1
  
  elif direction == "left":

    if last[0] - 1 == -1:
      next[0] = 7
    else:
      next[0] = last[0] - 1
  
  elif direction == "down":

    if last[1] + 1 == 8:
      next[1] = 0
    else:
      next[1] = last[1] + 1
  
  elif direction == "up":

    if last[1] - 1 == -1:
      next[1] = 7
    else:
      next[1] = last[1] - 1
  
  # Did I die?
  if next in slug:
    dead = True

  # Add this pixel at the end of the slug list
  slug.append(next)

  # Set the new pixel to the slug's colour
  sense.set_pixel(next[0], next[1], white)
  
  if next in vegetables:
    vegetables.remove(next)
    score += 1
    
    if score % 5 == 0:
      remove = False
      pause = pause * 0.8
  
  if remove == True:
    # Set the first pixel in the slug list to blank
    sense.set_pixel(first[0], first[1], blank)
  
    # Remove the first pixel from the list
    slug.remove(first)
    

def joystick_moved(event):
  global direction
  direction = event.direction
  
def make_veg():
  new = slug[0]
  while new in slug:
    x = randint(0, 7)
    y = randint(0, 7)
    new = [x, y]
  sense.set_pixel(x, y, red)
  vegetables.append(new)

# Main program ------------------------
sense.clear()
draw_slug()    

sense.stick.direction_any = joystick_moved

while not dead:
  move()
  sleep(pause)
    
  # Have a 20% chance of making a veggie if there aren't many about
  if len(vegetables) < 3 and randint(1, 5) > 4:
    make_veg()

sense.show_message( str(score) )