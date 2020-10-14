#Defining a function to display each step.
#For every step in the range of steps it will print out the top part of the ladder as well as the steps, then it will display the bottom of the ladder
def display_ladder(steps):
    
    for step in range(steps):
        print("| |")
        print("***") 

    
    print("| |")

#Defining the create ladder function which will print to ask the user to input how many steps are remaining and will store the user input and then call the display ladder function to output the ladder. 
def create_ladder():
    print("How many steps remain?")
    steps = int(input())
    display_ladder(steps)
#Calling the create ladder function
create_ladder()
  





