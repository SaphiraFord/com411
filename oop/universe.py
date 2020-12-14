
#Importing class's in to the file
from planet import Planet
from robot import Robot
from human import Human
#Importing module to enable visualization capabilities
import matplotlib.pyplot as plt
#Importing random to randomized the amount of robots, planets and humans
import random
#Creating a class called universe
#Instantiating a list called planets
class Universe:

  def __init__(self):
    self.planets = []


  #Returning number of planets if prompted
  def __repr__(self):
    return f"universe(planets={self.planets})"

  def __str__(self):
    return f"The universe contains {len(self.planets)} planets."


  #Creating an instanced method that will generate planets that are populated with random humans and robots 
  def generate(self):
    # create a new planet
    planet = Planet()

    #Will pick a random number between 1 - 10 for number of robots and then make those robots, the same for humans
    for index in range(random.randint(1, 10)):
      robot = Robot(f"Robot{index}")
      planet.add(robot)

    for index in range(random.randint(1, 10)):
      human = Human(f"Human{index}")
      planet.add(human)

    #Appending the planet that's just been created
    self.planets.append(planet)

  #Created a method to plot and show the population (humans vs robots)
  def show_populations(self):
    num_subplots = len(self.planets)
    #Creating a figure with 1 subplot
    fig = plt.figure()
    
    #For every subplot, planet = a new planet
    for index in range(num_subplots):
      planet = self.planets[index]

      #Variables to store the number of humans/robots in
      num_humans = 0
      num_robots = 0

      #For every inhabitant in inhabitants check what instance of inhabitant it is and if its human/robot/alien + 1 to that category
      for inhabitant in planet.inhabitants:
        if isinstance(inhabitant, Human):
          num_humans += 1
        elif isinstance(inhabitant, Robot):
          num_robots += 1

      #Adding subplots to the figure
      ax = fig.add_subplot(1, num_subplots, index+1)
      ax.bar([1, 2], [num_humans, num_robots])

    #Showing the figure in a tight layout
    plt.tight_layout()  
    plt.show()


if (__name__ == "__main__"):
  universe = Universe()
  universe.generate()
  universe.generate()
  universe.show_populations()
