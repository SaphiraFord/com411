from tech import Tech

#Creating Jetpack which is a subclass of the abstract class Tech
class JetPack(Tech):


  #Using the "super()" to give access to methods and properties of a parent or sibling class.
  def __init__(self):
    super().__init__()

  def __repr__(self):
    return "jetpack()"

  #Overiding the behaviours of the abstract methods

  def activate():
    print("Jetpack has been activated.")

  def deactivate():
    print("Jetpack has been deactivated.")

if __name__ == "__main__":
  jetpack = JetPack()
  print(repr(jetpack))


