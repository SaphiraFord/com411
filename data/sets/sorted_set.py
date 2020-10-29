#Created a function that creates an empty list then populates it with variables that the user inputs and then returns the set
def observed():
  observations = []
  
  index = 0
  #Running a for loop 5 times which asks the user for an observation and adds the user input to the set
  for index in range(5):
    print("Please enter an observation:")
    observation = input()
    observations.append(observation)
    index = index + 1

  return observations


#Instantiating a function which will remove observations from the list
def remove_observations(observations):

  #Making runs = true so that a while loop that is dpeendent on the runs variable can be made. The program will ask the user if they wish to remove a observation and if the answer = yes then it will promt them to input which observation they wish to remove then remove it fropm the list then the while loop will ask the user again if they wish to remove anything. However if the answer does not = yes then runs will = false and the while loop will end.
  runs = True
  while(runs):
    print("Do you wish to remove an observation (yes/no)?")

    userAnswer = input()

    if(userAnswer == "yes"):
      print("What observation do you wish to remove?")

      removedObservation = input()

      observations.remove(removedObservation)
    
    else:

      #while loop ends, program moves forward

      runs = False


def run():

   #storing the list from the previous function into "observations"

   list_of_observations = observed()


    #Calling remove_observations with the list of observations to be altered 
   remove_observations(list_of_observations)


    #Creating an empty set called observations_set to store the set
   observations_set = set()

    #for each observation in observations, the current observation and the amount of that observation are added to data. E.g. if "cat" is inputted then it would be stored in the set like (cat, 1)and if cat was inputted again it wouldn't create a new tuple it instead would be stored as (cat, 2)

   for observation in list_of_observations:
    data = list_of_observations.count(observation)
    observations_set.add((observation, data))

    #For each tuple in data print out the observation and how many times it's been inputted
   for data in observations_set:
    print(f"{data[0]} observed {data[1]} times.")


run()

   






