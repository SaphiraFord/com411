def run():
# Ask user to enter a cover type and reading in that input
  print("What type of cover does the book have?")
  bookCover = input()

#If the book cover is soft then program will ask if it is a perfect=bound and ask for an input. If "yes" then it will output a message, else it will output a different message. And if the user hasn't inputted "soft" then it will output a message. 

  if (bookCover == "soft"):
      print("Is the book perfect-bound?")
      perfectBound = input()

      if (perfectBound == "yes"):
          print("Soft cover, perfect bound books are very popular!")
      else:
          print("Soft covers with coils or stitches are great for short books") 
  else:
      print("Books with hard covers can be more expensive!")

