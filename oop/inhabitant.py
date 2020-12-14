#Importing ABC, abstract base class to make a class abstract
from abc import ABC

#Creating inhabitant abstract class that other classes like Robot and Human can have this as a base

class Inhabitant(ABC):

  #Attributes common to other classes
  MAX_ENERGY = 100

  def __init__(self, name="Inhabitant", age=0, energy=MAX_ENERGY):
    #Instanced attributes
    self.name = name
    self.age = age
    self.energy = Inhabitant.MAX_ENERGY

  #Method to grow the inhabitant and + its age by 1
  def grow(self):
    self.age += 1

  #Method to eat, takes parameters self and amount to eat
  def eat(self, amount):

    #If the inhabitant energy + the amount of energy is bigger than the max energy then the energy will be set to the robots max energy
    if (self.energy + amount > Inhabitant.MAX_ENERGY):
      self.energy = Inhabitant.MAX_ENERGY
      #Else + the amount of energy to the inhabitants energy
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