from time import sleep


#Challenge 1 Solution
def quickLib(name):
  noun = input("An item really important to you?")
  place = input("A place in your home")
  mood = input("An emotion")
  print ("Once upon a time " +name+ " looked all over the house and couldnt find "+ pronoun + noun+" Eventually it was found in the " + place+". "+name +" was so "+mood+"!" )

# name = input("whats your name")
# pronoun= input("whats your pronoun")
# quickLib(name)


#Challenge 2 Solution
def smile():
  while True:
    print("\033c", end="")
    print(":)")
    sleep(1)
    print("\033c", end="")
    print(":(")
    sleep(1)

# smile()