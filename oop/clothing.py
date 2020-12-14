from clothing_size import ClothingSize

class Clothing:

  def __init__(self, colour, material, size):
    self.colour = colour
    self.material = material
    self.size = size

if __name__ == "__main__":
  red_silk = Clothing("Red", "Silk", ClothingSize.MEDIUM)



