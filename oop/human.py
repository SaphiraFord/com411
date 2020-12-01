#A class
class Robot:

  # A class attribute
  laws = "Protect, Obey and Survive"

  # A class method
  def the_laws():
    print(Robot.laws)

  # An initialiser (special instance method)
  def __init__(self):

    # An instance attribute
    self.name = "Robot"
    self.age = 0

  # An instance method
  def display(self):
    print(f"I am {self.name}")
    Robot.the_laws()

#A class
class Human:

  # A class attribute
  MAX_ENERGY = "100"

  # An initialiser (special instance method)
  def __init__(self):

    # An instance attribute
    self.name = "Richard"
    self.age = 0
    self.energy = Human.MAX_ENERGY


  # An instance method
  def display(self):
    print(f"I am {self.name}")
    print(f"I have {self.energy} energy")

#Displaying some of the robot and human attributes
if (__name__ == "__main__"):

  robot = Robot()
  robot.display()

  human = Human()
  human.display()


    