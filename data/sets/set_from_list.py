#Created a function that creates an empty list then populates it with variables that the user inputs and then returns the set
def observed():
  observations = []
  
  index = 0
  #Running a for loop 7 times which asks the user for an observation and adds the user input to the set
  for index in range(7):
    print("Please enter an observation:")
    observation = input()
    observations.append(observation)
    index = index + 1

  return observations

def run():

  print("Counting observations...")

  #storing the list from the previous function into "observations"

  observations = observed()

  #Creating a set called "observations_set" which will store tuplets of a string that's been duplicated and and amount of times it's been duplicated

  observations_set = set()


#for each observation in observations, the current observation and the amount of that observation are added to data. E.g. if "cat" is inputted then it would be stored in the set like (cat, 1)and if cat was inputted again it wouldn't create a new tuple it instead would be stored as (cat, 2)

  for observation in observations:
    data = (observation, observations.count(observation))
    observations_set.add(data)

  #For each tuple in data print out the observation and how many times it's been inputted
  for data in observations_set:
    print(f"{data[0]} observed {data[1]} times.")

run()


