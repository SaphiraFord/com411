def run():
#Asking user to input what they saw and heard and storing these inputs
  print("What did I hear?")
  hear = input()
  print("What did I see?")
  see = input()
    
#Identifying what they saw and heard and if it was "grrr" and "two red eyes" then the program will display a message related to that. If the user inputs anything else then it will print a different message.
  if ((hear == "grrr") and (see == "two red eyes")):
      print("There is a scary creature. I should get out of here!")
  else:
      print("I am a little scared but I will continue.")