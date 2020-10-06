#Getting the user to input 2 numbers and then using code to find out which is the smallest number inputted or if the 2 numbers are equal
print("Please input the 1st number.")
number1 = input() 
print("Please input the 2nd number.")
number2 = input() 


# Finding out the smallest, largest and if two numbers are equal 
if (number1 < number2):
    print("\nThe first number is the smallest!!")
elif (number1 > number2):
    print("\nThe second number is the smallest!!")
else:
    print("\nThe two numbers are equal!!")


