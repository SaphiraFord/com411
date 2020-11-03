#Instantiating a function to create a dictionary called pattern which is populated which variables and then returning that variable so other functions can access it
def shortPattern():

  pattern = {"sequence":"101", "occurrences":5}

  

  return pattern

#Instantiating a function to create a dictionary called pattern which is populated which variables and then returning that variable so other functions can access it
def mediumPattern():

  pattern = {"sequence":"111000", "occurrences":25}

  return pattern


#Instantiating a function to create a dictionary called pattern which is populated which variables and then returning that variable so other functions can access it
def longPattern():

  pattern = {"sequence":"1100110011001100", "occurrences":50}

  return pattern

#Instantiating run function will calls the patterns functions and stores the items inside the variable patterns to then be printed

def run():


  print ("Analysing patterns...")

  pattern = {
   "short sequence": shortPattern(),
   "medium sequence": mediumPattern(),
   "long sequence": longPattern()
   }

  print(pattern)


run()