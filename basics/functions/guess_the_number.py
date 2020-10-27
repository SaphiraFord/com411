def run():
#Importing the "random" module which implements pseudo-random number generators.
  import random

#Asking for and storing user inputted minimum and max values . Then using "random.randrange" on min and max value to create a random number variable. 

  print("Please enter the minimum value:")
  min_value = int(input())

  print("Please enter the maximum value:")
  max_value = int(input())

  random_number = random.randrange(min_value, max_value)

#Asking user to input a guess of a random number between the min and max inputted numbers and creating a while loop so that the user can keep inputting numbers when they do not get the answer correct. 

#If it is correct then it will say Congratulations and end the game, breaking out of the for loop. But if the number is higher/lower than the random number the program will output that it is and allow the user to keep guessing until it is the correct answer.

  print("I am thinking of a number between {} and {}.".format(min_value, max_value))
  print("Can you guess what it is?")

  guess = 0

  while(guess != random_number):
    print("Please enter a number:")
    guess = int(input())

    if (guess == random_number):
      print("Congratulations!")
      break
    elif (guess < random_number):
      print("Guess higher")
    else:
      print("Guess lower")
  
  print("Game over!")