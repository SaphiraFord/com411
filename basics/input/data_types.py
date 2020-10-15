def run():
# Asks user to enter their name, age, height and weight
#Storing values as strings, floats and intergers respectively
  print("What is your name human?")
  name = input()
  print("How old are you (in years)?")
  age = int(input())
  print("How tall are you (in meters)?")
  height = float(input())
  print("How much do you weigh (in kilograms)?")
  weight = float(input())

#calculating bmi 

  bmi= float(weight / (height * height))

#rounded down the bmi to 2 decimal places

  roundedBmi = round(bmi, 2)

#outputting bmi and other inputs to user

  print(name,"you are ",age,"  years old and you bmi is ", roundedBmi,".")
