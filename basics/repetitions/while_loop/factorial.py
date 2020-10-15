def run():
#Getting the user to input a phrase and storing it
  print("Please enter a number:")
  number = int(input())

#I created the loop variable to count how many loops have past so that the program will eventually end when the loop is more than the inputted number. I give this the intial value of 0 as no iterations have past yet.
  loop = 0
#I created the factorial value so that the factorial of the inputted number can be calculated within the while loop. This is done through giving the factorial the initial value of 1 so that it can be multiplied with the loop numbers as a factorial of a number if multiplying that number by all the numbers that came before it. If I set the value as 0 then when multiplying the result would always be 0.
  factorial = 1
  while(loop < number):
    loop = loop + 1
    factorial = factorial * loop

#Outputting the calculated factorial number
  print("The factorial is {}" .format(factorial))