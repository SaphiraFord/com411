#Importing abstract class
from inhabitant import Inhabitant
#Human class
class Human(Inhabitant):


  # An initialiser (special instance method)
  def __init__(self, name="Human", age=0):
    super().__init__(name, age)

  
  #Magic methods (repr) returns a formal string representation of the object whilst (str) returns an informal string representation of the object.

  def __repr__(self):
    return f'human(name={self.name}, age={self.age}, energy={self.energy})'

  def __str__(self):
    return(f"My name is {self.name}")

  def display(self):
    print(f"I am {self.name}")


if (__name__ == "__main__"):
  human = Human()
  print(repr(human))
  human.move(10)
  print(repr(human))
  human.eat(5)
  print(repr(human))
  human.eat(20)
  print(repr(human))