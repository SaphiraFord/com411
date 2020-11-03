#Instantiating a function 
def cwd():
  #Using the method getcwd and importing module os which displays the file path of the current working  

  import os
  path = os.getcwd()
  print("Current Working Folder is {}" .format(path))

  print("The folder contains the following:")

  #displaying the contents of this folder using the method listdir of the module os

  for file in os.listdir(path):
    print(file)

def run():
  print("Processing...")

  #Calling the first function
  cwd()

run()


