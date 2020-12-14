#Importing abstract class
from inhabitant import Inhabitant
#Creating a class called Planet and instantiating a dictionary called inhabitants with 2 empty lists, humans and robots inside

class Planet():

  #List of inhabitants
  def __init__(self):
    self.inhabitants = []

    
  #Returning values of inhabitants to output to the screen if prompted
  def __repr__(self):
    return f"planet(inhabitants={self.inhabitants})"

  #An informal string saying that the planet has x amount of inhabitants

  def __str__(self):
    return f"This planet has {len(self.inhabitants)} inhabitants."

  #Instance methods that will add and remove inhabitants
  def add(self, inhabitant):

    self.inhabitants.append(inhabitant)

  def remove(self, inhabitant):

    self.inhabitants.append(inhabitant)

    

if(__name__ ==  "__main__"):
    planet = Planet()
    print(repr(planet))
    prins = Inhabitant("Prins")
    planet.add("Prins")
    print(planet)
    print(repr(planet))
    

