#Defining a user function which accepts two parameters sRemaining and sCrossed which stands for steps remaining and steps crossed
#If sRemaining is more than sCrossed then string will be outputted, otherwise a different string will be ouputted
def climb_ladder(sRemaining, sCrossed):
  if(sRemaining > sCrossed):
    print("Still some way to go!")
  else:
    print("We are almost there!")

#Calling the function
climb_ladder(5, 2)
climb_ladder(2, 5)
