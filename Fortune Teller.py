# Outputs instructions to the user
print("Welcome to the Fortune Teller, please follow the instructions \nin order to get your fortune.")

print("""\n __________________________
|    |    |
| yellow | blue |
|_________|_________|
|    |    |
| black | red |
|_________|_________|\n""")

# Prompts user to choose one of the colors shown
color = input("Please choose a color: ")
while color != "yellow" and color != "blue" and color != "black" and color != "red":
    print("That's not the right color!")
    color = input("Please choose a color: ")

# Set a number based on the color
if color == "yellow" or color == "blue":
    num = 1
else:
    num = 0

# Defines the fortunes using a list
fortunes = [
    "Of course",  # Fortune for number 1
    "No way",     # Fortune for number 2
    "Not now",    # Fortune for number 3
    "Go away",    # Fortune for number 4
    "Never",      # Fortune for number 5
    "Yes!",       # Fortune for number 6
    "Maybe",      # Fortune for number 7
    "No"          # Fortune for number 8
]

# Variable to hold the last selected number
lastNumber = 0

# For loop three times for selections
for i in range(3):
    # Handle yellow or blue pattern
    if num == 1:
        print("""\n            /|\\
              /  |  \\
             /   |   \\
            / 6  | 1  \\
           /_____|_____\\
           \\    |    /
            \\ 5 | 2 /
             \\  |  /
              \\ | /
               \\|/    \n""")
    
    # Handle black or red pattern
    else:  
        print("""\n               / |\\
              /  | \\
             /   |  \\
            / 4  | 7 \\
           /_____|____\\
           \\    |    /
            \\ 3 | 8 /
             \\  |  /
              \\ | /
               \\|/    \n""")
    
    # Asks user to select a number
    number = int(input("Please select a number: "))
    # Saves the last number selected
    lastNumber = number  
    # Outputs the number of times the fortune is flippling
    print("Flipping " + str(number) + " times....")
    
    # Shows the pattern based on the selected number
    # Handles when user selects yellow or blue
    if num == 1:  
        if number == 1 or number == 4 or number == 5 or number == 8:
            print("""\n               / |\\
              /  | \\
             /   |  \\
            / 4  | 7 \\
           /_____|____\\
           \\    |    /
            \\ 3 | 8 /
             \\  |  /
              \\ | /
               \\|/    \n""")
            
    # Handles when user selects black or red
    else:  
        valid_numbers = {2, 3, 6, 7}
        if number in valid_numbers:
            print("""\n               / |\\
              /  |  \\
             /   |   \\
            / 6  | 1  \\
           /_____|_____\\
           \\    |    /
            \\ 5 | 2 /
             \\  |  /
              \\ | /
               \\|/    \n""")

# Gets the fortune based on the last number selected by the user
fortune = fortunes[lastNumber - 1]  
# Outputs the last fortune after three numbers are selected
print("Your fortune is: " + fortune)