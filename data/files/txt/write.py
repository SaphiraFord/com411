#This program sorts given information into Sections and Books 

#This function searches for and opens the given file name and sorts the contents into two lists sections and books and returns this as a tuple
def search(fileName):
  print("Searching...", end = '')

  #Creating two empty lists
  sections = []

  books = []

  #Opening the file name and closing it  after use through using "with"
  with open(fileName) as file:


  #For every line in the file, check if the line starts with "Sections" and if it does spilt the line into seperate strings and add it to the empty sections list.

  #And if it doesn't start with "Sections" add it to books instead
   for line in file:
      if(line.startswith("Section")):
          x = line.split(":")
          sections.append(x[1].replace('\n',''))
      else:
          books.append(line.replace('\n',''))

  print("Done!")

  #Returning the lists sections and books as a tuple later called data
  return (sections, books)



def save(fileName, dataLists):

  print("Saving...", end = '')

  #Opens the given file name in write mode. Then it writes "Section: " and then for the first element in dataLists (sections) it will write the sections to the file and then it will write "Books: " and for the second element in dataLists (books) it will write the books to the file

  #To not display the comma at the end of the books and sequences. I calculated the length of Sequence (e.g. it would be a length of 3 if: cat, dog, bird) and so if the index is less than the length of the Sequence it will print the line of the sequence with a comma. Else if the index is bigger than the length of the Sequence then it will print the line of the sequence without a comma

  #Then it is the same with Books and I calculated the length of Books and so if the index is less than the length of the Books it will print the line of the books with a comma. Else if the index is bigger than the length of the Books then it will print the line of the books without a comma

  with open((fileName), "w") as file:
    file.write("Section: ")
    for index in range(len(dataLists[0])):
      if (index < len(dataLists[0]) - 1):
       file.write(f"{dataLists[0][index]},")
      else:
        file.write(f"{dataLists[0][index]}")

    file.write("\n")

    file.write("Books: ")
    for index in range(len(dataLists[1])):
      if (index < len(dataLists[1]) - 1):
       file.write(f"{dataLists[1][index]},")
      else:
        file.write(f"{dataLists[1][index]}")


  print("Done!")


#Instantiating a function to run the program
def run():

  #Calls the first function with a fileName

  data = search("data/files/txt/section-books.txt")

  #Calls the second function with a fileName as well as the data variable is the tuple of sections and books

  save("data/files/txt/section-books.txt", data)


run()











