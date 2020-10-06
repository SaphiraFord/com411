#Getting the user to input 3 numbers and then using code to find out which is the smallest number inputted or if the 2 numbers are equal
print("Please input the 1st number.")
number1 = int(input())
print("Please input the 2nd number.")
number2 = int(input()) 
print("Please input the 3rd number.")
number3 = int(input()) 

#instantiating even and odd

even = 0

odd = 0

#using if else statements to find out which have a remainder of 0 with the modulus function to find out if they are even or odd

if(number1 % 2 == 0):
  even = even + 1
else: 
  odd = odd + 1
if(number2 % 2 == 0):
 even = even + 1
else: 
 odd = odd + 1
if(number3 % 2 == 0):
 even = even + 1
else: 
  odd = odd + 1

#Displaying how many odd and even numbers there are

print("There were ",  odd, " odd numbers and ", even, " even ones.")