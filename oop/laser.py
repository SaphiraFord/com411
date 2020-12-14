from alien_tech import Tech

#Creating Laser which is a subclass of the abstract class Tech
class Laser(Tech):
  #Contsnat attribute
  MAX_RANGE = 5

  #Overiding the behaviours of the abstract methods
  def activate(self):
    print("Activating laser")

  #Firing has a shots distance and will check if its lower than MAX_RANGE and will say if shots are hitting or not
  def fire(self):
    shots_distance = 4

    if shots_distance < MAX_RANGE:
      print(f"Laser shots hitting targets")
    else:
      print(f"Laser shots missing targets")

  def deactivate(self):
    print("Deactivating laser")