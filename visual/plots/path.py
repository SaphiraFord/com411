#Importing module to enable visualization capabilities
import matplotlib.pyplot as plt

#Getting users to enter values for x and y
def coordinate():
  
  print("Please enter a value for x:")
  x = input()
  
  print("Please enter a value for y:")
  y = input()
  
  #Turning x and y into a tuple then returning it
  
  x_y = (x, y)
  
  return x_y
  
def path():
  
  print("Retrieving path...")

  #Creating empty lists to store x and y values
  
  x_values = []
  
  y_values = []
  
  #For 4 iterations it will call the first method making the user input x and y values

  for count in range (4):

    #Data = the tuple of the user inputted y and x values
    
    data = coordinate()

    #Appending the lists to store the x values which are at position 0 and the y values which are at position 1
    
    x_values.append(data[0])
    
    y_values.append(data[1])
    
  #Returning the x and y lists

  return x_values, y_values
  

  #Function that runs the program
def run():
  
  #The x and y lists are now stored in values

  values = path()

  #X = values at position 0 while Y = values at position 1
  
  x = values[0]
  
  y = values[1]

  #Plotting the x and y values with a red dashed line with circles
  
  plt.plot(x, y, 'ro--')  

  #Labeling the axis
  
  plt.xlabel("x values")
  plt.ylabel("y values")

  #Showing the data visually 
  
  plt.show()




run()

