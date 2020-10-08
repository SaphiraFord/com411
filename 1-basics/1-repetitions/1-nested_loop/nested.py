#Getting the user to input how many rows and columns they want and storing this information
print("How many rows should I have?")
rows = int(input())
print("How many columns should I have?")
columns = int(input())

#Created a nested for loop that for every inputted row the for loop that outputs a smiley face is outputted depending on the amount of columns there are

for row in range(0, rows, 1):
    for column in range(0, columns, 1):
        print(":-)" , end="")
    print()

    
