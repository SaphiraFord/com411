#Importing module to enable visualization capabilities
import matplotlib.pyplot as plt   
#Importing module to enable animations to be made using matplotlib
import matplotlib.animation as animation
     
#Creating a figure with 1 subplot
fig, ax = plt.subplots()
    
#Defining a function that takes the parameter frame, this function sets the limits of the x and y axis and plots the subplots inputs as frame and frame for x and y. 

#ro = red circles on the graph
def animate(frame):
  #Will delete the plots from the graph
  ax.cla()    
  ax.set_xlim(0,10)
  ax.set_ylim(0,10)
  ax.plot(frame, frame, 'ro')
     
#Defining a run function, making the figure globalso it's assessable outside of the scope of the run function
def run():
  global fig  

  #Creating a simple animation with the FuncAnimation function using the figure, making it 10 frames and having a interval between frames
  simpleAnimation = animation.FuncAnimation(fig, animate, frames = 10, interval = 1000)

  #Showing the plot
  plt.show()
  
      
run()  