import clothing_size as ClothingSize

class Clothing():

  def __init__(self, colour, material, size):
    self.colour = colour
    self.material = material
    self.size = size

if __name__ == "__main__":
  my_clothing = Clothing("pink", "wool", ClothingSize.MEDIUM)

  if (my_clothing.size.value == ClothingSize.MEDIUM.value):
    print("e")
