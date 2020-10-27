#Defining directions which is a function which will create a list called "directions" and it is populated with variables.
def directions():

  directions = ["Move Forward", "Move Backward", "Turn Left", "Turn Right"] 

  #returning directions
  return directions

#Defining a function which will call the directions function and then output the variables within the directions list
def run():
  print(directions())

run()