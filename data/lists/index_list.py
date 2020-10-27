#Defining movements function which creates a list with both text and numbers and then returns the list
def movements():
  path = ["Move Forward", 10, "Move Backward", 5, "Move Left", 3, "Move Right", 1]

  return path

#Defining a function that will print text then call the movements() function and make it the same as the local Variable localMovements. 
def run():
  print("Moving...") 

  localMovements = movements()

  #Printing items off the list by referencing their index e.g. 0, 1, 2, 3...

  print("{0} for {1} steps" .format(localMovements[0],localMovements[1]))

  print("{0} for {1} steps" .format(localMovements[2],localMovements[3]))

  print("{0} for {1} steps" .format(localMovements[4],localMovements[5]))

run()
