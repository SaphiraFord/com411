#Created a function that creates an empty set then populates it with string variables and then returns the set
def observed():
  observations = set()

  observations = {"Flying Car", "Sky Scraper", "Laser", "Dome"}

  return observations


#Created a functoin that will call the previous function and store the returned set inside of "localObservationsSet" variable and then output the set the the screen
def run():
  localObservationsSet = observed()

  print(localObservationsSet)

run()