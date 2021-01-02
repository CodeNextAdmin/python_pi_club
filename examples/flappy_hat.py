import sense_hat
from time import sleep, time
from random import randint

sense = sense_hat.SenseHat()
sense.clear()

"""

  Make your Sense HAT into a Flappy HAT!
  
  Help the bird fly though the columns.  Each column is
  one point.  How many points can you get?
  
  Read through the code to learn how the game is made and
  try changing some of the variables at the top. Turn on
  debug_mode to print extra information about what the program
  is doing.
  
  Inspired by the Astro Pi team's flappy astronaut!
  https://www.raspberrypi.org/learning/flappy-astronaut

  Note: Requires sense_hat version 2.2.0 or later
"""

# Edit these variables to change key game parameters
col_color = (0,255,0)      # RGB color of column pixels
bg_color = (0,0,0)         # RGB color of background pixels
bird_color = (200,200,0)   # RGB color of the bird pixel
bird_y = 2                 # Where the player starts 
bird_lives = 3             # How many lives does the bird get?
columns = [ (7, 3, 3)]     # Starting column x index, gap y start, gap size
column_speed_base = 1      # Base speed for column movement, from 1 to 5
debug_mode = False         # Set to true to print extra information

# Variables for convenience and readability
up_key = sense_hat.DIRECTION_UP
pressed = sense_hat.ACTION_PRESSED

# Initial settings - should be no need to alter these
speed = 0
game_over = False
setup = True
moved = False
column_interval = 10

# Debug functions: pause or print messages if debug_mode is set to True
def debug_message(message):
  if debug_mode:
    print(message)

def debug_pause(message):
  # Currently not used
  # To examine a specific portion of the program, add a debug_pause with a message
  # Or, change an existing debug_message call to debug_pause to pause there
  if debug_mode:
    input(str(message) + "  Press enter to continue...")
    
# Get true color values for comparisons: get_pixel() sometimes returns different values
sense.set_pixel(0,0, col_color)
col_color = sense.get_pixel(0,0)
sense.set_pixel(0,0, bg_color)
bg_color = sense.get_pixel(0,0)
sense.set_pixel(0,0, bird_color)
bird_color = sense.get_pixel(0,0)
sense.clear()

# Save setup in a tuple to restart game
reset_state = (col_color, bg_color, bird_color, bird_y, bird_lives, columns, column_speed_base, speed, game_over)

####
# Game functions
####

def move_columns():
  debug_message("Moving columns")
  global columns
  starting_cols = len(columns)
  
  # Shift x coordinate of colums to left
  columns = [(c[0] -1, c[1], c[2]) for c in columns]

  # Add a new column if needed
  if max([c[0] for c in columns]) == 4:
    gap_size = randint(2,4)
    row_start = randint(1 + gap_size, 6)
    columns.append((7,row_start,gap_size))

def draw_column(col, custom_color = None):
  debug_message("Drawing column")
  
  if custom_color:
    back_color = custom_color
  else:
    back_color = bg_color

  # Construct a list of column color and background color tuples, then set those pixels
  x, gap_start, gap_size = col
  c = [col_color] * 8
  c[gap_start - gap_size: gap_start] = [back_color] * gap_size
  for y, color in enumerate(c):   
    sense.set_pixel(x,y,color)

def draw_screen(custom_color = None):
  debug_message("Drawing screen")
  
  if custom_color:
    back_color = custom_color
  else:
    back_color = bg_color
  
  sense.clear(back_color)
  # Filter out offscreen columns then draw visible columns
  visible_cols = [c for c in columns if c[0] >= 0] 
  for c in visible_cols:
    draw_column(c, back_color)  

def draw_bird(falling = True):
  debug_message("drawing bird")
  global bird_y, bird_lives, game_over
  # Replace bird with upcoming background or column at x=4
  sense.set_pixel(3,bird_y,sense.get_pixel(3, bird_y))
  
  if falling:
    bird_y += speed

  # Stay onscreen
  if bird_y > 7:
    bird_y = 7
  if bird_y < 0:
    bird_y = 0
  
  # Collisions are when the bird moves onto a column
  hit = sense.get_pixel(3, bird_y) == col_color
  if hit:
    flash_screen()
    bird_lives -= 1
    # ignore any keypresses here
    sense.stick.get_events()
  
  # Draw bird lives
  if bird_lives > 8:
    # Can only draw 8 at a time
    draw_lives = 8
  else:
    draw_lives = bird_lives
    
  for i in range(draw_lives):
    sense.set_pixel(0,i, (200,200,200))
  
  game_over = bird_lives < 0
  
  # Draw bird in new position
  sense.set_pixel(3,bird_y,bird_color)
  debug_message("Bird drawn")

def flash_screen():
  for i in range(3):
    custom_color = ([randint(50, x) for x in [255,255,255]])
    draw_screen(custom_color)
    # Make sure bird is still visible
    sense.set_pixel(3,bird_y,bird_color)
    sleep(.1)
  draw_screen()

####
# Main Game Loop
####

while True:

  if setup:
    col_color, bg_color, bird_color, bird_y, bird_lives, columns, column_speed_base, speed, game_over = reset_state
    # Initial screen setup
    last_redraw = round(time(), 1) * column_interval
    draw_screen()
    draw_bird()
    
    # Clear joystick events
    sense.stick.get_events()
    column_speed = int(column_speed_base)
    
    setup = False
  
  column_tick = round(time(), 1) * column_interval

  if (column_tick % (column_interval - column_speed) == 0) and (column_tick > last_redraw):
    # Enough time has passed: columns move 
    debug_message("Tick!")
    speed = 1
    # make columns faster if possible as game goes on
    if column_interval > (column_speed + 2):
      column_speed = column_speed_base + len(columns) // (column_interval * 3)

    move_columns()
    draw_screen()
    draw_bird()
    debug_message("Tick length: " + str(column_tick - last_redraw) \
                   + " Speed: " + str(column_speed)\
                   + "Columns: " + str(len(columns)))
    last_redraw = column_tick

  events = sense.stick.get_events()
  if events:
    for e in events:
      debug_message("Processing joystick events")
      if e.direction ==  up_key and e.action == pressed:
        # User pressed up: move bird up and columns over
        debug_message("Joystick up press detected")
        move_columns()
        draw_screen()
        speed = -1
        draw_bird()
        moved = True
        # Prevent double falls
        last_redraw -= column_interval // 2
  else:
    moved = False
    
  if game_over:
    flash_screen()
      
    # Score is number of columns survived
    score = len(columns) - 2 
    sense.show_message(str(score) + "pts!", text_colour=(255,255,255))
    
    # Start over
    setup = True