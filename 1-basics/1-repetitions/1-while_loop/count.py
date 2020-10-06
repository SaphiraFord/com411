#Getting the user to input how many cables must be avoided
print("How many live cables must I avoid?")
cables = int(input())

#instantiating variable removedCables to count how many live cables have been removed with this variable being set to 1 initially and when the liveCables are less than the user inputted cables then the program will stop. However while the liveCables are less than the user inputted cables then it will print avoiding... done (current number of live cables) and add 1 onto the liveCables value so that the iteration will eventually come to a stop. Then it will output a message saying that all the live cables have been avoided

liveCables = 0

while(liveCables < cables):
  print("Avoiding...", end="")
  liveCables = liveCables + 1
  print("Done! {} live cables avoided!" .format(liveCables))

print("All live cables have been avoided.")

