# Code goes here and DO NOT FORGET INTRO COMMENTS

# John Elehwany
# CS151
# Professor Zee
# Due Date: 11/7/24
# PA3
# This program lets the user choose from a selection of certain ASCII art.
# ASCII Art Credits: https://www.asciiart.eu/
# INPUT IN:
# INPUT OUT:

import random

# Purpose: Outputs an ASCII art cat after it is chosen.
# Name: cat
# Parameters: None
# Return: None
def cat():
    print("""
    |\---/|
    | o_o |
     \_^_/
    """)


# Purpose: Outputs an ASCII art dog after it is chosen.
# Name: dog
# Parameters: None
# Return: None
def dog():
    print("""
                __
    (\,--------'()'--o
     (_    ___    /~"
      (_)_)  (_)_)
    """)


# Purpose: Outputs an ASCII art owl after it is chosen.
# Name: owl
# Parameters: None
# Return: None
def owl():
    print("""
     /\_/\
    ((@v@))
    ():::()
     VV-VV
    """)


# Purpose: Chooses a random ASCII art and outputs it.
# Name: random_art
# Parameters: none
# Return: none
def random_art():
    print('Choosing a random ASCII art...')
    # Randomly select and call one of the art functions
    selection = random.choice([cat, dog, owl])
    selection()


# Purpose: Asks for user input of which ASCII art to display
# Name: menu
# Parameters: none
# Return: none
def menu():
    print("""Welcome! Please choose an ASCII art to display:
    1 - ASCII Cat
    2 - ASCII Dog
    3 - ASCII Owl
    4 - Random
    """)
    while True:
        choice = input('Please select 1-4: ')

        # Validate the input to ensure it is within the accepted range
        if choice in ['1', '2', '3', '4']:
            if choice == '1':
                cat()
            elif choice == '2':
                dog()
            elif choice == '3':
                owl()
            elif choice == '4':
                random_art()
            break  # Exit the loop after displaying chosen art
        else:
            print('Invalid answer! Please only input a number between 1 and 4.')


# Calls the menu function
menu()