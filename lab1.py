"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
                                    LAB 1
---------------------------------------------------------------------------------
- File Name: lab1.py
- Teacher: David Steedman
- Class: Software Engineering
- Description: Create and use functions in Python
"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
import random

# Write a function named welcome_message that prints out "Welcome to our program!" whenever it is called.
def welcome_messsage():
    print("welcome to my program!")

    

# Create a function named print_divider that prints out a line of asterisks (e.g., "**********") to act as a section divider.  
def print_divider():
    print("*" * 10)

# Write a function named get_number that asks the user to input a whole number and then returns the result as an integer.
def get_number():
    number=input(" please enter an integer")
    return int

# Create a function named get_random_colour that, when called, returns a random colour from a predefined list of colours.

def get_random_colour():
    a = random.randint(1,3)

    if a == 1:
        return("red")
    
    if a== 2:
        return("blue")
    
    if a == 3:
        return("yellow")
    
    

   

  

# Call all of your functions to demonstrate that they work





