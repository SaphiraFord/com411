#Defining a function to search for the user inputted file name
def search(fileName):
  print("Searching...")

  #Opening the file name and closing it  after use through using "with"

  with open(fileName) as file:
    #for every line in the file, printing out the line

    for line in file:
      print("Looked in {}" .format(line))
  print("...Done!")


#Calling the function with a file name in the function run()
def run():
  search("data/files/txt/locations.txt")

run()