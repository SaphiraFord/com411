#Importing module to enable visualization capabilities
import matplotlib.pyplot as plt 
#Importing module to enable animations to be made using matplotlib
import matplotlib.animation as animation

#Creating a figure with 1 subplot
fig, ax = plt.subplots()
#Creating an empty dictionary called data
data = []

#Defining a function that creates 3 seperate dictionaries nested within the previously empty data dictionary. These 3 dictionaries store the x and y values for squares, small, medium and large.
def init():
  data.append({'x':[3, 3, 4, 4, 3], 'y':[3, 4, 4, 3, 3]})
  data.append({'x':[2, 2, 5, 5, 2], 'y':[2, 5, 5, 2, 2]})
  data.append({'x':[1, 1, 6, 6, 1], 'y':[1, 6, 6, 1, 1]})

#creating a function called animate which takes the frame parameter sets the figure to global then clears any visualization before setting the limits of the x and y values and then plotting the currently indexed square values within the dictionary. 

#It goes through all 3 nested dictionaries within the
def animate(frame):
  global fig
  index = frame % len(data)
  ax.cla()
  ax.set_xlim(0, 7)
  ax.set_ylim(0, 7)
  ax.plot(data[index]['x'], data[index]['y'])

#Defining a funciton to run the program
def run():
  #Setting the figure as global again
  global fig
  #Creating the squares animation with the FuncAnimation function using the figure, making it 100 frames, having a interval between frames of 100 and calling the init function which sets the values.  
  squares_animation = animation.FuncAnimation(fig, animate, frames=100, interval=100, init_func= init)

  #showing the subplots
  plt.show()

run()
