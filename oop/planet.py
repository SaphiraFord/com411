#Importing robot and human classes
from human import Human
from robot import Robot

#Creating class planet with an empty list of inhabitants
class Planet:
  #List of inhabitants
  def __init__(self):
    self.inhabitants = []
  #Methods to output list of inhabitants
  def __repr__(self):
    return f"planet(inhabitants={self.inhabitants})"

  def __str__(self):
    return f"This planet has {len(self.inhabitants)} inhabitants."

  #Adding inhabitant
  def add(self, inhabitant):
    self.inhabitants.append(inhabitant)
  #Removing inhabitant
  def remove(self, inhabitant):
    self.inhabitants.remove(inhabitant)

if (__name__ == "__main__"):
  planet = Planet()
  print(repr(planet))
  prins = Human("Prins")
  planet.add(prins)
  print(repr(planet))
  print(planet)