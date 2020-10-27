#Defining a function that creates a tuple and then returns that tuple
def steps():
  likelihoods = [("step 1", 50), ("step 2", 38), ("step 3", 27), ("step 4", 99), ("step 5", 4)]


  return likelihoods

 #Defining a function that first creates a local variable which will store the "likelihood" tuple

def run():

  #storing the likelihoods tuple in steps

  all_steps = steps()

  #Creating two empty lists

  good_steps = []
  bad_steps = []
  
  #A for loop that for every step in steps it will check if the step in the current position is equal or less to 50 if it is then it will be added to the bad steps list and if it isn't it will be added to the good steps list
  for step in all_steps:
    if (step[1] >= 50):
      bad_steps.append(step)
    else:
      good_steps.append(step) 

  print(f"Good steps: {len(good_steps)}, Bad steps: {len(bad_steps)}")

run()
