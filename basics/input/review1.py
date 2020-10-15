def run():
#I have now learnt a number of fundamental programming concepts including displaying text, reading user input, storing data and converting between data types. And I can use these to create a range of simple programs.

#Below I have created a program that demonstrates all I have learned

  print("I have almost created a robot named Bob, please input characters for his eyes to complete him...")

#Asking for input for both of the robot eyes

  leftEye = input("Please enter a character for the left eye")
  rightEye = input("Please enter a character for the right eye")

#Outputting a robot with eyes that are inputted by the user

  print("##########")
  print("# {}   {}  #".format(leftEye, rightEye))
  print("#        #")
  print("##########")  


  print("Thank you, I would now like to calculate his BMI for research purposes if you could answer the following questions...")

# Asking user to enter their name, age, height and weight
#Storing values as strings, floats and intergers respectively

  print("How old is Bob (in years)?")
  age = int(input())
  print("How tall is Bob (in meters)?")
  height = float(input())
  print("How much does Bob weigh (in kilograms)?")
  weight = float(input())

#calculating bmi 

  bmi= float(weight / (height * height))

#rounded down the bmi to 2 decimal places

  roundedBmi = round(bmi, 2)

#outputting bmi and other inputs to user

  print("Bob is ",age,"  years old and his bmi is ", roundedBmi,".")

  print("Thank you, finally if you could help input his lives, energy levels and shield levels he will be complete...")

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

  print("Thank you assisting with Bob's creation.")