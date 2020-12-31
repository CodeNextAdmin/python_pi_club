from time import sleep
from random import randint



# Challenge 1
def mood(name):
  mood = input("happy or sad?")

  if mood == "happy":
    print("yay "+name + " feels "+mood+" :)")
  else:
    print("aw "+name + " feels "+mood+ " :( ")

 
mood("Alex")

# Challenge 2
def area(shape):
  if shape == "square":
    l = int(input("length?  "))
    w = int(input("width?  "))
    return l*w
  elif shape == "triangle":
    l = int(input("length?  "))
    w = int(input("width?  "))
    return l*w*0.5
  else:
    r = int(input("radius?"))
    return 2*r*3.14

# shape = input ("square, triangle, or circle?")
# print(area(shape))
# shape = input ("square, triangle, or circle?")
# print(area(shape))