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


# Purpose: Outputs an approximation of a circle design.
# Name: draw_circle
# Parameters: None
# Return: None
def draw_circle():
    print("""
      ****
     *    *
    *      *
     *    *
      ****
    """)


# Purpose: Draws a set of customizable lines based on user input.
# Name: draw_lines
# Parameters: None
# Return: None
def draw_lines():
    try:
        num_lines = int(input("How many lines to draw? "))
        char = input("What character(s) should be used for the lines? ")
        repetitions = int(input("How many times should the characters repeat per line? "))

        for _ in range(num_lines):
            print(char * repetitions)
    except ValueError:
        print("Invalid input. Please enter numbers where expected.")


# Purpose: Outputs the first random design.
# Name: random_design1
# Parameters: None
# Return: None
def random_design1():
    for i in range(5):
        print(" " * (5 - i) + "*" * (2 * i + 1))


# Purpose: Outputs the second random design.
# Name: random_design2
# Parameters: None
# Return: None
def random_design2():
    for i in range(5, 0, -1):
        print("@" * i)


# Purpose: Outputs the third random design. It is using repeated random characters.
# Name: random_design3
# Parameters: None
# Return: None
def random_design3():
    symbols = "!@#$%^&*()"
    for _ in range(3):  # Draw 3 lines
        line = ""
        for _ in range(10):
            line += random.choice(symbols)
        print(line)



# Purpose: Chooses and outputs one of three random designs.
# Name: draw_random
# Parameters: None
# Return: None
def draw_random():
    random.choice([random_design1, random_design2, random_design3])()


# Purpose: Displays a menu for the user to choose an ASCII art option.
# Name: menu
# Parameters: None
# Return: None
def menu():
    while True:
        print("""
        Welcome to the ASCII Art Program!
        Choose an option:
        1 - Circle
        2 - Lines
        3 - Random Design
        4 - Exit
        """)
        choice = input("Enter your choice: ")

        if choice == "1":
            draw_circle()
        elif choice == "2":
            draw_lines()
        elif choice == "3":
            draw_random()
        elif choice == "4":
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")


# Purpose: Entry point of the program, calls the menu function.
# Name: main
# Parameters: None
# Return: None
def main():
    menu()


main()
