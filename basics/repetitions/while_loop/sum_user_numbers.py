def run():
#Getting the user to input how many numbers to sum up and storing thisas totalNumbers
  print("How many numbers should I sum up?")
  totalNumbers = int(input())
def run():
#instantiating numbers variable to 0 so it wouldnt start with a value and it controls the iteration so that if numbers is less than the totalNumbers inputted by the user the program will continue the while loop but in that loop it will increment 1 onto it's preexisting value to eventually reach totalNumbers and end the program
  numbers = 0
#I have instantiated sum1 to 0 so it wouldn't start with a value and so it can store and add up the user inputs together
  sum1 = 0

  while(numbers < totalNumbers):
    numbers = numbers + 1
    print("Please enter number {} of {}:" .format(numbers, totalNumbers))
    sum1 = sum1 + int(input())

#Outputting the answer of all the inputted numbers added up
  print("The answer is" ,sum1,".")



