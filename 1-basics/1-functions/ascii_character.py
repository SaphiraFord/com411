#This program will prompt the user to enter a positive interger within the range of 32-126 and then it will output the corresponding letter to the user
print("Program Started!")
#Telling user what to input
print("Please enter an ASCII code:")
number = int(input())

#Will convert a negative number to a positive one with the "abs()" function then it will check if that integer is within the range of 32 - 126. If this is true then the program will output the number as well as convert the number into it's ascii character and output that. However if it is false then it will print that an error has occured. 
if(abs(number) in range(32, 126)):
  print("The character represented by the ASCII code {} is {}." .format(number, chr(number)))
else:
  print("An error has occured")
print("Program Ended!")
