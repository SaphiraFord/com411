def run():
#Getting the user to input how far the robots are from the cave and adding 1 to the value so that it will display for example if the number inputted was 7, then 7 steps are remaining and then count down
  print("How far are we from the cave?")
  distance = int(input()) + 1
#A for iteration that for the distance inputted in the range inputted it will go through the iteration in reverse and print out the number of steps remaining
  for distance in reversed(range(distance)):
    print("{} steps remaining" .format(distance))