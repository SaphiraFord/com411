#Defining function that will add the two inputted weights together to make the total weight and then return that value. 

def sum_weights(beep_weight, bop_weight):
    total_weight = beep_weight + bop_weight
    return total_weight

#Defining a function that will calculate the average weight by adding the two inputted weights together, dividing it by 2 to make the average weight then  will return this value.

def calc_avg_weight(beep_weight, bop_weight):
    avg_weight = (beep_weight + bop_weight) / 2
    return avg_weight

#Defining a run function which will output all the text to the user as well as gather and store all their inputs. It will store the weights as well as the decision of either calculating the sum or the average.

def run():
    # retrieve required user data
    print("What is the weight of Bop?")
    bop_weight = float(input())

    print("What is the weight of Beep?")
    beep_weight = float(input())

    print("What would you like to calculate (sum or average)?")
    action = input()

    #If the action is "sum" then the answer will be sum weights which is both beeps and bops weights added together and this will be outputted for the user. 

    #If the action is "average" then the answer will be both beeps and bops weights added together and divided by 2 to make the average. This will then be outputted to the user. 

    #If a different input has been inputted then the program will print string saying that it is not sure what the user would like to do

    if (action == "sum"):
        answer = sum_weights(beep_weight, bop_weight)
        print("The sum of Beep's and Bop's weight is {:.2f}".format(answer))
    elif (action == "average"):
        answer = calc_avg_weight(beep_weight, bop_weight)
        print("The average of Beep's and Bop's weight is {:.2f}".format(answer))
    else:
        print("I am not sure what you would like to do.")

#Running the program
run()