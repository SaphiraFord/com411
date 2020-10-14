#Defining a function that will display an ascii box around the inputted word
def display_box(word):
    num_dashes = 4 + len(word)
    print("-" * num_dashes)
    print("| {} |".format(word))
    print("-" * num_dashes)
#Defining a function that will display the word in lowercase
def display_lower_case(word):
    print(word.lower())
#Defining a function that will display the word in uppercase
def display_upper_case(word):
    print(word.upper())
#Defining a function that will display the word in reverse
def display_mirrored(word):
    mirrored = ""
    for letter in reversed(word):
        mirrored += letter
    print("{} | {}".format(word, mirrored))
#Defining a function that will ask the user to input how many times the already inputted word should be repeated and then output the inputted word a number of times based on that input
def display_repeated(word):
    print("How many times should the word be displayed?")
    repetitions = int(input())

    for repetition in range(repetitions):
        #If the repetition is even then the outputted words will be in lower case
        if (repetition % 2 == 0):
            print(display_lower_case(word))
        #If the repetition is odd then the outputted words will be in upper case
        else:
            print(display_upper_case(word))

#Defining a function that will run the program as a whole by asking the user to input a word and then asking the user to input a number which corresponds to the outputted menu.

#The user can enter options from a range of 1-6 which all function differently and have their functions called to carry out their task on the inputted word.
def run():
    print("Please enter a word:")
    word = input()

    # remember the user has not yet selected an option
    response = 0

    while (response != 6):
        # get the user's selection
        print("What would you like to do with this word?")
        print("[1] Display in a box")
        print("[2] Display lower-case")
        print("[3] Display upper-case")
        print("[4] Display mirrored")
        print("[5] Display repeated")
        print("[6] Quit")

        response = int(input()) 
 
        # determine and execute action
        if (response == 1):
            display_box(word)
        elif (response == 2):
            display_lower_case(word)
        elif (response == 3):
            display_upper_case(word)
        elif (response == 4):
            display_mirrored(word)
        elif (response == 5):
            display_repeated(word)
        elif (response == 6):
            break
        else:
            print("Unknown option.") 
#Running the program
run()