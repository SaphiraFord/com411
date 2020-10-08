#Getting the user to input what markings they see and storing this variable
print("What strange markings do you see?")
markings = input()

print("Identifying...")

index = 0

#A for iteration which uses the len() function to find out the amount of characters within the inputted word and goes through each one, indexing them through using the already instantiated index and then displaying it to the user and adding 1 to it each iteration

for position in range(0, len(markings), 1):
  print("index", index, ":", end="")
  print(markings[position])
  index = index + 1

print("Done!")
