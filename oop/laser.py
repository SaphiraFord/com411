#Importing tech as the derived class of the superclass laser
from tech import Tech

#Creating Laser which is a subclass of the abstract class Tech

class Laser(Tech):

  #Creating a constant of a maximum range
  MAX_RANGE = 100

  #Using the "super()" to give access to methods and properties of a parent or sibling class.
  def __init__(self):
    super().__init__()

  def __repr__(self):
    return "laser()"

  #Overiding the behaviours of the abstract methods
  def activate():
    print("Laser has been activated.")

  def deactivate():
    print("Laser has been deactivated.")

  #Firing has a range distance and will check if its higher than MAX_RANGE and will output different outputs depending on the conditions

  def fire(range_distance):
    if (range_distance > Laser.MAX_RANGE):
      print(f"Fired maximum range of {Laser.MAX_RANGE}")
    else:
      print(f"Fired a distance of {range_distance}")


if __name__ == "__main__":
  laser = Laser()
  print(repr(laser))