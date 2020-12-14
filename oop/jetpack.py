from alien_tech import Tech

#Creating Jetpack which is a subclass of the abstract class Tech
class Jetpack(Tech):

  #Overiding the behaviours of the abstract methods
  def activate(self):
    print("Activating jetpack")

  def fly(self):
    speed = 4
    print(f"Flying at a speed of {0}" speed)

  def deactivate(self):
    print("Deactivating jetpack")

