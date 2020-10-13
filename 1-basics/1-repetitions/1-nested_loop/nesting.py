#Getting the user to input a sequence such as "x--x" and finding out the distance between both the x markers
print("Please enter a sequence")
sequence = input()
print("Please enter the character for the marker")
marker = input()


#Instantiating variables that will contain the position of the markers
marker1_position = -1
marker2_position = -1

#A for iteration that for the position in the inputted characters will make the letter variable the same as the sequence position. This for loop will run as many times as there are characters within the sequence and within that an if and nested if statement will run. This will calculate if a letter holds the same value as the inputted marker and if it does then it will check if marker1_position has already been set from -1 and if it hasnt then it will set it to the current position. If it's hasn't and the letter holds the same value as the marker then it will set marker2_position to the current position. And if letter is not the same value as marker then the loop will move onto the next character or end.

for position in range(0, len(sequence), 1):
    letter = sequence[position]

    if (letter == marker):
        if (marker1_position == -1):
            marker1_position = position
        else:
            marker2_position = position

# Displaying the results
print("The distance between the markers is", marker2_position - marker1_position - 1)
