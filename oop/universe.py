#Importing module to enable visualization capabilities
import matplotlib.pyplot as plt
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
    return f"The universe contains {len(self.planets)} planets."


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
  
  #Created a method to plot and show the population (humans vs robots)

  def show_populations(self):
    #Supplying x and y values
    num_subplots = len(self.planets)

    #Creating a figure with 1 subplot
    fig, axs, = plt.subplots(num_subplots, 1)

    #For every index in range of the number of subplots
    #planet = Universe.planets[ and the number of humans/robots will = the number of humans/robots stored in the inhabitants dictionary
    for index in range(num_subplots):
      planet = self.planets[index]
      num_humans = len(planet.inhabitants['humans'])
      num_robots = len(planet.inhabitants['robots'])

      #If the number of subplots = 1 then it will not index and instead show one subplot. However if it is not 1 then it will index and display all the subplots are bar graphs
      if (num_subplots == 1):
        axs.bar([1, 2], [num_humans, num_robots])
      else:
        axs[index].bar([1, 2], [num_humans, num_robots])
    
    #Showing the figure in a tight layout
    plt.tight_layout()
    plt.show()


if(__name__ ==  "__main__"):
  universe = Universe()
  universe.generate()
  print(repr(universe))
  print(universe)
  universe.show_populations()


