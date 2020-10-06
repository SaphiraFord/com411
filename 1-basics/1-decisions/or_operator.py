#Asking user which adventure to have and stores that input
print("What type of adventure should I have?")
adventure = input()

#If the adventure input is scary or short then it will print entering the dark forest however if the input is safe or long the it will print taking the safe route. If anything else is inputted then it will output not sure which route to take.

if(( adventure == "scary") or (adventure == "short")):
  print("Entering the dark forest!")
elif((adventure == "safe") or (adventure == "long")):
  print("Taking the safe route!")
else:
  print("Not sure which route to take")