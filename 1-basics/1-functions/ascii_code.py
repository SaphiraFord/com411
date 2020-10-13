#This program will prompt the user to enter a single character and then it will output the ascii value of that character to the user
print("Program Started!")
#Telling user what to input
print( "Please enter a standard character:")
singleCharacter = input()
#Calculating the length of the input and seeing if it's less than 2, if it is then it will find out the ascii value of that character and output it. If it isn't then it will say that an error has occured
if(len(singleCharacter) < 2):
  characterAscii = ord(singleCharacter)
  print("The ASCII code for {} is {}." .format(singleCharacter, characterAscii))
else:
  print("An error has occured")
print("Program Ended!")