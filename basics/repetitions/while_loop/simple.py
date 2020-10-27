def run():
#Getting the user to input how many cables are holding the robot and storing this value
  print("How many cables should I remove?")
  cables = int(input())

#instantiating variable removedCables to count how many cables have been removed with this variable being set to 1 initially and when the removedCables are less than the user inputted cables then the program will stop. However while the removedCables are less than the user inputted cables then it will print removed cable and add 1 onto the removedCables value so that the iteration will eventually come to a stop

  removedCables = 0

  while(removedCables < cables):
    print("Removed cable")
    removedCables = removedCables + 1

