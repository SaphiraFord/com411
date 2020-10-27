#Defining the function directions which creates a list and returns the list
def directions():
  directions = [ "Move Forward", "Move Backward", "Turn Left", "Turn Right"]

  return directions

#Defining the function menu which will output text and then create a local variable which will equal the same as the list "directions[]"

def menu():
  print("Please select a direction:")

  localDirections = directions()

  #For index in the range of the length of the list it will print out the current index and the current list item that is directions 
  for index in range(len(localDirections)):
    print("{0}: {1}" .format(index, localDirections[index]))

#Defining a function that will run the program by calling the menu function
def run():
  menu()

run()

