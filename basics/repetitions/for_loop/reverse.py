def run():
#Getting the suer to input what phrase they see and storing this variable
  print("What phrase do you see?")
  phrase = input()



#A for iteration which uses the len() function to find out the amount of characters within the inputted word and goes through each one in reverse order due to "- 1, -1, -1" it prints out the phrase position each iteration and forms the word to output

  print("\nReversing...\nThe phrase is: ")

  for position in range(len(phrase) - 1, -1, -1):
    print(phrase[position], end="")