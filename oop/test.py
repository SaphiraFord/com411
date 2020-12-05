#Robot Class
class Robot:
    # Class attributes law and max energy
  laws = "Protect, Obey and Survive"
  MAX_ENERGY = 100

  # A class method taht prints robot laws
  def the_laws():
    print(Robot.laws)

  # An initialiser (special instance method)
  def __init__(self):

    #instantiates attributes
    self.name = "Robot"
    self.age = 0
    self.energy = Robot.MAX_ENERGY

  #Method to grow the robot and + its age by 1
  def grow(self):
    self.age += 1

  #Method to eat, takes parameters self and amount to eat
  def eat(self, amount):

    #If the robot energy + the amount of energy is bigger than the max energy then the energy will be set to the robots max energy
    if (self.energy + amount > Robot.MAX_ENERGY):
      self.energy = Robot.MAX_ENERGY
      #Else + the amount of energy to the robots energy
    else:
      self.energy += amount

  #Method method based on self and distance
  def move (self, distance):
    #potential energy = energy - distance
    potentialenergy = self.energy - distance
    #If energy is less than 0, set energy to 0
    if (potentialenergy < 0):
      self.energy = 0
      #returns the positive numeric of energy - potential energy 
      return self.energy - abs(potentialenergy)
    else:
      #Else energy = potential energy and return 0
      self.energy = potentialenergy
      return 0


  # An instance method which says the robots name
  def display(self):
    print(f"I am {self.name}")

  #Another instanced method which outputs the robots name, age and energy
  def __repr__(self):
   return f'robot(name={self.name}, age={self.age}, energy={self.energy})'

#if name is the same as main then it will run this code

#robot = robot(), run display method for robot, print robots repr method, make robot grow, move(10), eat(5) and print repr(robot)
if (__name__ == "__main__"):
  robot = Robot()
  robot.display()
  print(robot.__repr__())
  robot.grow()
  robot.move(10)
  robot.eat(5)
  print(repr(robot))

#Human Class
class Human:
  
  MAX_ENERGY = 100
  def __init__(self):
    
    self.name = "Human"
    self.age = 0
    self.energy = Human.MAX_ENERGY

  def display(self):
    print(f"I am {self.name}")

  def __str__(self):
   return f'My name is {self.name} and I am {self.age} years old.'

  def __repr__(self):
   return f'human(name={self.name}, age={self.age}, energy={self.energy})'

#Displaying human info
if (__name__ == "__main__"):
  human = Human()
  human.display()
  print(human.__str__())
  print(human.__repr__())

    