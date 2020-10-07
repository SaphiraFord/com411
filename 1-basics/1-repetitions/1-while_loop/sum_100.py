#Calculating the sum of the first 100 numbers with a while loop
print("Calculating the sum of the first 100 numbers...")
#Within the calculation variable which I set to 0 so that it has not value in the begining, I will be adding up numbers while the program goes through it's iteration of 100 and will add up all the numbers so that 5050 is the answer
calculation = 0
#I set numbers to 0 so it wouldnt start with a value and it controls the iteration so that if numbers is less than 100 the program will continue the while loop but in that loop it will increment 1 onto it's preexisting value to eventually reach 100 and end the program
numbers = 0
while(numbers < 100):
  numbers = numbers + 1
  calculation = calculation + numbers
#outputted the calculation of the first 100 numbers all added up
print("Done! The answer is {}" .format(calculation))