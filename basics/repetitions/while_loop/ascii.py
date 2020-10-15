def run():
#Getting the user to input how many bars must be charged and storing this 
  print("How many bars should be charged?")
  bars = int(input())

#instantiating variable chargedBars to count how many bar have been charged with this variable being set to 1 initially and when the chargedBars are less than the user bars then the program will stop. However while the chargedBars are less than the user inputted bars then it will print charging... (current number of chargedBars) and add 1 onto the chargedBars value so that the iteration will eventually come to a stop. Then it will output a message saying that the battery is fully charged

  chargedBars = 0

  while(chargedBars < bars):
    print("Charging:...", end="")
    chargedBars = chargedBars + 1
    print(chargedBars * " █ ")

  print("The battery is fully charged.")
