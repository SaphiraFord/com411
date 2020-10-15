def run():
#Getting the user to input a phrase and storing it
  print("Please enter a phrase:")
  phrase = input()
#Using the len() function to count the number of characters within the inputted phrase and multiplying that by "Bop " and so if only one character was inputted Bop would only be printed once to the screen however if 3 characters were inputted then Bop would be printed 3 times
  print("Bop " * len(phrase))
