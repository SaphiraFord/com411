#Defining cross_bridge() user defined function and making it accept the steps argument. The function will output "Crossed step" depending on the value of "steps" so if "steps" = 3 then "Crossed step" would be outputted 3 times. However if "steps" = more than 5 then it would output "Crossed steps" depending on the value of "steps" as well as "The bridge is collapsing". If the value is not a number then the program will print a different message.
def cross_bridge(steps):
  print("Crossed step \n" * steps)
  if(steps > 5):
    print("The bridge is collapsing!")
  else:
    print("We must keep going!")

#Calling the cross_bridge() function
cross_bridge(3)
cross_bridge(6)