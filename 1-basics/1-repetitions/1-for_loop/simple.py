#Getting the user to input how many mountains should be displayed and storing that value
print("How many mountains should I display?")
mountains = int(input())

#for every mountain in the range of mountains ascii art of a mountain will be printed to the screen 

for mountain in range(mountains):
 print("""
           __
          /  \\_  
         /^    \\
        /  ^    \\_
      _/ ^ ^     ^\\
     /  ^     ^    \\


     """)