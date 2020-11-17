#Importing module to enable visualization capabilities
import matplotlib.pyplot as plt


#Defining funcitont hat takes the filepath as a parameter
def read_data(filename):

  #Creating an empty list to store the temperature data within
  temperature_data= []

  #Opening the filename as a file 
  with open (filename) as file:

    #For every line in the file it will convert the line to a float and seperate that line from the rest of the text and store it within the temperature data list
    for line in file:
      temperature = float(line.strip())
      temperature_data.append(temperature)

  #Returning temperature data list
  return temperature_data

#Defining a funciton to run the program
def run():

  #Calls the read_data function with the given file path as a parameter 
  data = read_data("visual/plots/subplots/temps.txt")

  #Creating two subplots ax1 and ax2 
  fig , (ax1, ax2) = plt.subplots(1, 2)

  #Plotting the subplots on their figures
  ax1.plot(range(1, 8), data)
  ax2.bar(range(1, 8), data)

  #Creating a tight layout to give the subplots enough space from eachother
  plt.tight_layout()

  #Showing the graphs
  plt.show()

#running the program
run()