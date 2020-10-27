#Defining a function that creates a tuple and then returns the smallest numeric of that tuple so that other functions can access it
def likelihood():
  likelihood = (50, 38, 27, 99, 4)

  return min(likelihood)

#Defining a function that first creates a local variable which will store the smallest numeric from "likelihood" then printing that to the user
def run():
  localLikelihood = likelihood()

  print("Minimum likelihood of falling: {}%" .format(localLikelihood))

run()