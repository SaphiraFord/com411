def run():
#Creating a user defined function "identify()" and calling it within the program.
#It will ask for an input and if the input is "a large boulder" then it will print certain string else it will print a different string. 
  def identify():
    print("What lies before us?")
    object = input()
    if("a large boulder" == object):
      print("It's time to run!")
    else:
      print("We will be fine.")

  identify()

