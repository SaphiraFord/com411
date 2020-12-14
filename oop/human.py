#Importing abstract class
from inhabitant import Inhabitant
#Human class
class Human(Inhabitant):


  # An initialiser (special instance method)
  def __init__(self, name = "Human", age = 0, energy = 0):


  # An instance method which says the robots name
  def display(self):
    print(f"My name is {self.name} and I am {self.age} years old and I have {self.energy} energy.")
  
  #Magic methods (repr) returns a formal string representation of the object whilst (str) returns an informal string representation of the object.

  def __repr__(self):
    return f'human(name={self.name}, age={self.age}, energy={self.energy})'

  def __str__(self):
    return(f"My name is {self.name} and I am {self.age} years old and I have {self.energy} energy.")

if (__name__ == "__main__"):
  human = Human()
  print(human)
  print(human.__repr__())
  human.grow()
  human.move(10)
  human.eat(5)
  print(repr(human))