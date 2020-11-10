#Importing module to enable visualization capabilities
import matplotlib.pyplot as plt

def small():

  #Will display circle markers with a red dotted line

  x = [3, 3, 4, 4, 3]
  y = [3, 4, 4, 3, 3]

  plt.plot(x, y, 'ro--')  

def medium():
  
  x = [2, 2, 5, 5, 2]
  y = [2, 5, 5, 2, 2]
  #Will display square markers with a green dashed line
  plt.plot(x, y, 'gs--') 

def large():

  x = [1, 6, 6, 1, 1]
  y = [1, 1, 6, 6, 1]
  #Will display pentagon markers with a blue solid line
  plt.plot(x, y, 'bp-')  


def run():

  #Plotting the x and y values then showing them
  small()

  medium()

  large()
  plt.show()


run()