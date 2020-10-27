def run():
#Getting the user to input how what level of brightness is required and storing this 
  print("What level of brightness is required?")
  brightnessLevel = int(input())

  print("Adjusting brightness...")
#A for iteration that for the brightnessLevel in the range of the inputted brightnessLevel it will count only the even numbers within that range given between 0 and the input. Then it will output the brightness level only in even outputs such as 0, 2, 4, and 6 if the number inputted was 6. brightness level will +1 every iteration until it is at the number inputted.

  for brightnessLevel in range(0, brightnessLevel + 1, 2):
    print("Beep's brightness level: ", "*" * brightnessLevel)
    print("Bop's brightness level: ", "*" * brightnessLevel)
    print("Adjustments complete!")