from time import sleep
from random import randint


#challenges 1 & 2

def guessNum1():
  num = randint(0,100)
  counter  = 3
  while counter > 0:
    guess = input("pick a number between 0 and 100 ")
    if num == int(guess):
      counter  = 0
      print("Correctomundo")
    else:
      counter -= 1
      if int(guess) > num:
        print("too high bud")
      else:
        print("too low bud")
  print("the right answer was " + str(num))

guessNum1()