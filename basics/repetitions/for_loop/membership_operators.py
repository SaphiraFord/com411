def run():
#Getting the user to input what phrase they see and storing this variable
  print("What strange markings do you see?")
  phrase = input()

  print("Identifying...\nThe phrase is", end="")

#The reversed variable I instaniated starts off blank but within the for iteration that will go through every letter in phrase it will add th inputted letters and print them out in a reversed order. 

  reversed = ""

  for letter in phrase:
    reversed = letter + reversed

  print(reversed) 
