#Human class
class Human:

  #A class attribute 
  #Capitalized attributes are constant
  MAX_ENERGY = 100


  # An initialiser (special instance method)
  def __init__(self):

    # An instance attribute
    self.name = "Human"
    self.age = 0
    self.energy = Human.MAX_ENERGY

  #Method to grow the robot and + its age by 1
  def grow(self):
    self.age += 1

  #Method to eat, takes parameters self and amount to eat
  def eat(self, amount):

    #If the robot energy + the amount of energy is bigger than the max energy then the energy will be set to the robots max energy
    if (self.energy + amount > Human.MAX_ENERGY):
      self.energy = Human.MAX_ENERGY
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
  
  #Magic methods (repr) returns a formal string representation of the object whilst (str) returns an informal string representation of the object.

  def __repr__(self):
    return f'human(name={self.name}, age={self.age}, energy={self.energy})'

  def __str__(self):
    return f'human(name={self.name}, age={self.age}, energy={self.energy})'

if (__name__ == "__main__"):
  human = Human()
  human.display()
  print(human.__repr__())
  human.grow()
  human.move(10)
  human.eat(5)
  print(repr(human))