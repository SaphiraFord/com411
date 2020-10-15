def run():
#Asking the user to input an activity
#If the user inputs "calculations" then it will display "Performing calculations"
#If not then the program will display "Perofrming activity"
  print("Please enter the activity to be performed.")
  activity = input()
  if (activity == "calculations"):
    print("Performing calculations!")
  else:
    print("Performing activity...")

  print("Activity completed!!") 