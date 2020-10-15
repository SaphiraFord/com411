def run():
#Asks the user where the robot should look for his battery and will read in this answer to answer

  print("Where should I look?")
  answer = input()


#If the answer is bedroom/lab/bathroom it will ask the user where in that location to look. If the user doesn't input one of those 3 locations it will output dialog and end the program. If the user inputs "under the bed" for the bedroom/ "in the bathtub" for the bathroom or "on the table" in the lab then it will print out dialog based on that input. And if they reply with anything else then it will output a different message.

  if(answer == "bedroom"):
    print("Where in the bedroom should I look?")
    bedroomAnswer = input()

    if(bedroomAnswer == "under the bed"):
      print("Found some shoes but no battery")
    else:
      print("Found some mess but no battery")

  elif(answer == "in the bathroom"):
    print("Where in the bathroom should I look?")
    bathroomAnswer = input()

    if(answer == "in the bathtub"):
      print("Found a rubber duck but no battery")
    else:
      print("Found a wet surface but no battery.")

  elif(answer == "in the lab"):
    print("Where in the lab should I look?")
    labAnswer = input()

    if(labAnswer == "on the table"):
      print("Yes! I found my battery!")
    else:
      print("Found some tools but no battery")

  else:
    print("I do not know where that is but I will keep looking.")
