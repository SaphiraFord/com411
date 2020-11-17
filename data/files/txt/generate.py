#Function that takes the parameter of file name, searches for it, opens it and if a line starts with "section" it will split the line into string and add it to the list "section_name"
def search(namefile):
  print ("Searching...")

#Creating empty dictionary "data" to hold data in

  data = {}
  
  with open(namefile) as file:

#Creates empty list to hold the key for the dictionary
    section_name = ""
    for line in file:

#Deletes "Section" if the line starts with that so it's not duplicated. This is done through spilting the line into two elements 0 and 1 and 1 contains the word "Section" and will be removed with ".strip"

      if (line.startswith("Section")):
        linex = line.split(":")
        section_name = linex[1].strip()

#If the section name is in data it will append the line so that it will remove "Section: " so that it's not duplicated

      else:
        if (section_name in data):
          value = data[section_name]
          value.append(line.strip())
        else:
          data[section_name] = [line.strip()]
  print ("Done!")

#Returning the data which is the dictionary

  return data


#Creating a function which will run the program
def run():

#Will run the search function with the file name "data/files/txt/books1.txt" and store the returned dictionary within data

  data = search("data/files/txt/books.txt")

#Opens the file path "data/files/txt/generate.csv" in write mode.

  with open("data/files/txt/generate.csv", "w") as file:

#For every item in the dictionary it will add an item to section and an item to books. 

    for item in data.items():
      section = item[0]
      books = item[1]

#For every book in books it will write the section and books to the file 

      for book in books:
        file.write(f"{section},{book}\n")

run()