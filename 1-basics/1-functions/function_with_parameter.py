#Defining a user function which accepts the parameter plan. Depending on the value of the parameter there will be different sentences outputted in string
def escape_by(plan):
  if(plan == "jumping over"):
    print("We cannot escape that way! The boulder is too big!")
  elif(plan == "running around"):
    print("We cannot escape that way! The boulder is moving too fast!")
  elif(plan == "going deeper"):
    print("That might just work! Let's go deeper!")
  else:
    print("We cannot escape that way! The boulder is in the way!")

#When the program starts any input will be stored in the plan variable and then "escape_by()" function is called which accepts the "plan" argument through "escape_by(plan)".
#Calling the escape_by() function
escape_by("jumping over")
escape_by("running around")
escape_by("going deeper") 
plan = input()
escape_by(plan)
