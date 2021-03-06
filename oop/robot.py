#Importing abstract class
from inhabitant import Inhabitant
#Robot class
class Robot(Inhabitant):

  #A class attribute 
  laws = "Protect, Obey and Survive"

  # A static method, which is bound to the class robot rather than an object
  @staticmethod
  def the_laws():
    print(Robot.laws)

    #An initialiser (special instance method)
  def __init__(self, name="Robot", age=0):
    super().__init__(name, age)

  # An instance method
  def display(self):
    print(f"I am {self.name}")

  #Magic methods (repr) returns a formal string representation of the object whilst (str) returns an informal string representation of the object.

  def __repr__(self):
    return f'robot(name={self.name}, age={self.age}, energy={self.energy})'

  def __str__(self):
    return(f"My name is {self.name} and I am {self.age} years old and I have {self.energy} energy.")

if (__name__ == "__main__"):
  robot = Robot()
  Robot.the_laws()
  print(repr(robot))
  robot.move(10)
  print(repr(robot))
  robot.eat(5)
  print(repr(robot))
  robot.eat(20)
  print(repr(robot))
