#Instantiating a function to create a dictionary called sequences which is populated which variables and then returning that variable so other functions can access it
def pattern():

  sequences = {"Short Sequence":3, "Medium Sequence":2, "Long Sequence":1}

  return sequences

#Instantiating run function will calls the pattern function and stores the list in there inside localDictionary and then prints it

def run():

  localDictionary = pattern()

  print(localDictionary)


run()
