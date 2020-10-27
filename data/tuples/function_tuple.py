#Defining a function that creates a tuple and then returns both the smallest and biggest numeric of that tuple so that other functions can access them
def likelihood():
  likelihoods = (50, 38, 27, 99, 4)


  #Finding out and storing the biggest/smallest items in the tuple in variables 
  minL = min(likelihoods)

  maxL = max(likelihoods)

  #Returning the biggest and smallest items
  
  return minL, maxL



    #Defining a function that first creates a local variable which will store the biggest and smallest numerics from the "likelihood" tuple then printing that to the user using their index to display the correct one
def run():

    localLikelihood = likelihood()


    print("Minimum likelihood of falling: {}%" .format(localLikelihood[0]))
    print("Maximum likelihood of falling: {}%" .format(localLikelihood[1]))

run()


  