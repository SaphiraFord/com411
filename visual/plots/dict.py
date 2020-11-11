#Importing module to enable visualization capabilities and importing random to enable random generation
import matplotlib.pyplot as plt
import random as rnd


#Defining data function
def data():
  #Creating an empty dictionary called paths
  paths = {}
  #Asking user for input and saving that input
  print("What type of line (:,-- or-)?")
  linetype = input()
  #Asking user for input and saving that input
  print ("What color (r,g or b)?")
  color = input()
  #Asking user for input and saving that input
  print("What type of marker(o,s or ^)?")
  markerstyle = input()
  #Storing the user inputs into the empty dictionary
  paths['linetype'] = linetype
  paths['color'] = color
  paths['markerstyle'] = markerstyle
  #Returning paths so that other functions can access the dictionary
  return paths

#Defining a function generate 
def generate():
  #Asking user for input and saving that input, making sure that input is an integer
  print ("How many lines would you like to display?")
  numberlines = int(input())
  #For the amount of lines the user has inputted it will run this for loop which sets x and y at random values between 1 and 10. It then plots the graph based on x, y, user inputted colour, linetype and marker style.
  for numberline in range(numberlines):
    values = data()
    x = [0, rnd.randrange(1, 10)]
    y = [0, rnd.randrange(1, 10)]
    plt.plot(x, y, f"{values['color']}{values['linetype']}{values['markerstyle']}")

#function to run the program
def run():
  print ("Running...")
  #Calls generate
  generate()
  #Shows the plotted graph
  plt.show()
  print ("Done!!")

run()