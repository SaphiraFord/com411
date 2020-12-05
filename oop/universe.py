#Importing class's in to the file
from human import Human 
from robot import Robot
from planet import Planet
#Importing random to randomized the amount of robots, planets and humans
import random
#Creating a class called universe
#Instantiating a list called planets
class Universe:

  def __init__(self):
    self.planets = []

  #Returning values of humans and robots to output to the screen if prompted
  def __repr__(self):
    return f"universe(planets={self.planets})"

  def __str__(self):
    return f"The universe contains{len(self.planets)} planets."


  #Creating an instanced method that will generate planets that are populated with random humans and robots 
  def generate(self):
    #creating a planet
    planet = Planet()

    #Will pick a random number between 1 - 10 for number of robots and then make those robots
    for index in range(random.randint(1, 10)):
      robot = Robot(f"Robot{index}")
      planet.add_robot(robot)



    #Will pick a random number between 1 - 10 for number of humans and then make those humans
    for index in range(random.randint(1, 10)):
      human = Human(f"Human{index}")
      planet.add_human(human)


    #Appending the planet that's just been created
    self.planets.append(planet)


if(__name__ ==  "__main__"):
  universe = Universe()
  universe.generate()
  print(repr(universe))
  print(universe)

