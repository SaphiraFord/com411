#Asking the user what direction should the robot paint in
#If the user inputs "up" then it output that it is painting upwards and the same for down, left and right
print("Towards which direction should I paint (up, down, left or right)?")
direction = input()
if (direction == "up"):
  print("I am painting in the upward direction!")
elif (direction == "down"):
    print("I am painting in the downward direction!")  
elif (direction == "left"):
    print("I am painting to the left direction!")   
else:
    print("I am painting to the right direction!")

