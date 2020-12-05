#Importing class's in to the file
from human import Human 
from robot import Robot
#Creating a class called Planet and instantiating a dictionary called inhabitants with 2 empty lists, humans and robots inside

class Planet():

  def __init__(self):
    self.inhabitants = {
      'humans':[],
      'robots':[]
    }


  #Returning values of humans and robots to output to the screen if prompted
  def __repr__(self):
    return f"planet(humans={self.inhabitants['humans']}, robots={self.inhabitants['robots']})"

  #An informal string saying that the planet has x amount of humans and robots
  def __str__(self):
    return f"This planet has {len(self.inhabitants['humans'])} humans and {len(self.inhabitants['robots'])} robots."

  #Instance methods that will add and remove humans and robots
  def add_human(self, human):

    self.inhabitants['humans'].append(human)

  def remove_human(self, human):

    self.inhabitants['humans'].remove(human)

  def add_robot(self, robot):

    self.inhabitants['robots'].append(robot)

  def remove_robot(self, robot):

    self.inhabitants['robots'].remove(robot)
    

if(__name__ ==  "__main__"):
    planet = Planet()
    print(repr(planet))
    prins = Human("Prins")
    planet.add_human("Prins")
    print(planet)
    print(repr(planet))
    

