#Importing csv module to allow the program to read csv files and separate the values with the comma
import csv
#Importing module to enable visualization capabilities
import matplotlib.pyplot as plt

#Creating empty string to store the first and second values
first_key = None
second_key = None

#Creating a function to read the data and store it
def read_data():
  #Making the first_key and second_key variables global so that they can be used throughout the program
  global first_key, second_key

  #Opening the file path as an CSV file
  with open('visual/plots/subplots/temps.csv') as csv_file:

    #csv_reader = the contents of the csv file
    csv_reader = csv.reader(csv_file)

    #making the header have the value of week 1 and 2 using Next() to skip the blank space so that csv reader can read the data
    header = next(csv_reader)

    #first_key = first element of the string seperated with a comma in header
    first_key = header[0].strip()
    #second_key = second element of the string seperated with a comma in header
    second_key = header[1].strip()

    #Creating a dictionary called data with the first_key and second_key lists inside
    data = {first_key:[], second_key:[]}

    #For every row in csv_reader append the dictionary at position 0 to hold the first_key and append position 1 to hold the second_key
    for row in csv_reader:
      data[first_key].append(row[0].strip())
      data[second_key].append(row[1].strip())

  #Returning tha dicitonary data
  return data

#Creating a funciton that will run the program
def run():

  #Calling read_data() and storing the dicitonary in data
  data = read_data()

  #Creating two subplots which share the same data
  fig, (ax1, ax2) = plt.subplots(2, 1, sharex='all')

  #Plotting the subplots
  ax1.plot(data[first_key])
  ax2.plot(data[second_key])

  #Creating a tight layout to give the subplots enough space from eachother
  plt.tight_layout()

  #Showing the figure
  plt.show()

run()