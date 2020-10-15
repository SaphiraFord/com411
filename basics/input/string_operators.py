def run():
# Asked user to enter the number of lives, energy and shield levels
#Storing their values as whole numbers
  print("Please enter Bob's number of lives")
  lives = int(input())
  print("Please enter Bob's energy levels.")
  energy = int(input())
  print("Please enter Bob's shield levels.")
  shield = int(input())

  print("Health has been set")
  print("Energy has been set")
  print("Shields have been set")

#Multiplying the value inputed by a string symbol to give a visual effect

  print("Lives:   " ,lives * "♥")
  print("Energy:  " ,energy * "♦")
  print("Shield:  " ,shield * "♦")
