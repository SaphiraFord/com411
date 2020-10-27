#Defining directions function which will create a populated list and then return that list
def directions():
  directions = ["Move Forward", "Move Backward", "Turn Left", "Turn Right"]
  return directions

#Defining a menu function which gets the user to input a direction and then create a local variable "localDirections" to equal the same as the populated list "directions"
def menu():
  print("Please select a direction:")
  localDirections = directions()

#Then there is a for loop that for index in the range of the length of the user inputted list, it will print out the current index as well as the current item in the list localDirections 

  for index in range(len(localDirections)):
    print("{}: {}".format(index, localDirections[index]))

#Taking in the user input 

  userInput = int(input())

#Returning the user inputted index which is bound to the localDirections direction for example "forward" direction wouold be when the user inputs 0

  return localDirections[userInput]

#Defining a function which will run the program. It first creates an empty list called "route" then it prints out some text. 

#Then it has a for loop that for count in range of 5 it will call the menu function and anything returned from the menu() function will be stored in "direction". Then the route list will be appengded so that it will store all the answers that the user picked. 

#Finally it will print out those answers to the user

def run():
  route = []
  print("Working out an escape route...")
  for count in range(5):
    direction = menu()
    route.append(direction)
  print("Escape route: {}" .format(route))

run()
