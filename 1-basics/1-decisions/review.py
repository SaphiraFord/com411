#Showcasing:Decisions with if...elif...else statements Nested decisions Multiple conditions with logical (AND. OR and NOT) operators

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

#Asks the user where the uer should look for their battery and will read in this answer to answer

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

#Asking user to input what they saw and heard and storing these inputs
print("What did I hear?")
hear = input()
print("What did I see?")
see = input()
    
#Identifying what they saw and heard and if it was "grrr" and "two red eyes" then the program will display a message related to that. If the user inputs anything else then it will print a different message.
if ((hear == "grrr") and (see == "two red eyes")):
    print("There is a scary creature. I should get out of here!")
else:
    print("I am a little scared but I will continue.")


#Getting user to input a two digit number and storing that value

print("You have found a safe, the safe has a lock of 2 digits please input a guess to try and unlock the safe")
number = int(input())

#I have created a list have contains 5 two digit numbers

list = [10, 20, 30, 40, 50 ]; 

#If the inputted number is not in the list then the text the safe remains locked is outputted however if the inputted number is on the list then the safe is opened
  
if ( number not in list ): 
   print("The safe remains locked") 
else: 
   print("You have successfully opened the safe, great job!!") 
  
