# Asked user to enter their name, age, height and weight
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

#outputting bmi and other inputs to user

print(name,"you are ",age,"  years old and you bmi is ",bmi,".")
