#Defining a function which will take user input and ouput it to the user
def listen():
  print("What sound did I hear?")
  sound = input()
  print("That was a loud {}!" .format(sound))

#Calling the function I have just created
listen()
