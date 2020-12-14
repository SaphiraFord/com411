#Importing abstract class
from inhabitant import Inhabitant
from alien_tech import Tech
#Alien class
class Alien(Inhabitant):


  # An initialiser (special instance method)
  def __init__(self):
    self.Tech = []

  def pickup(self, Tech):
    self.Tech.append(Tech)

  def drop(self, Tech):
    self.Tech.remove(Tech)


  # An instance method
  def display(self):
    print(f"My name is {self.name} and I am {self.age} years old and I have {self.energy} energy.")

  #Magic methods (repr) returns a formal string representation of the object whilst (str) returns an informal string representation of the object.

  def __repr__(self):
    return f"alien(tech={self.Tech)"

  def __str__(self):
    return(f"Alien has: {self.Tech})"

if __name__  ==  "__main__":
  alien = Alien()
  print(repr(alien))
