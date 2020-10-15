def run():
#Asking for user to enter a whole number then the program will work out if theat number is even/odd and display that result to the user
#This is worked out through using the modulus and dividing a number by 2, if the number is 0 then the number is even however, if the number is anything else then it is odd
  print("Please enter a whole number.")
  wholeNumber = int(input())
  wholeNumber = wholeNumber % 2

  if(wholeNumber == 0):
    print("The number is even.")
  else:
    print("The number is odd.")