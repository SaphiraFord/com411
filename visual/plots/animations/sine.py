#Importing module to enable visualization capabilities
import matplotlib.pyplot as plt   
#Importing module to enable animations to be made using matplotlib
import matplotlib.animation as animation
#Importing Numpy to allow the generation of arrays of numbers
import numpy as np

#Creating a figure with 1 subplot
fig, ax = plt.subplots()
    
#Defining a function that takes the parameter frame, this function sets the limits of the x and y axis and plots the subplots inputs as x and y values and defines those values to create a sine wave.

#r-- = red dashes on the graph
def animate(frame):    
  ax.set_xlim(0,720)
  ax.set_ylim(-1,1)

  x_values = np.arange(0, frame)
  #creating sine wave 
  y_values = np.sin((np.pi / 180) * x_values)
  ax.plot(x_values, y_values, 'r--')


#Defining a run function, making the figure global so it's assessable outside of the scope of the run function
def run():
  global fig  

  #Creating a simple animation with the FuncAnimation function using the figure, making it 720 frames and having a interval between frames
  simpleAnimation = animation.FuncAnimation(fig, animate, frames = 720, interval = 100)

  #Showing the plot
  plt.show()
  
      
run() 