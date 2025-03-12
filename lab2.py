"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
                                    LAB 2
---------------------------------------------------------------------------------
- File Name: lab2.py
- Teacher: David Steedman
- Class: Software Engineering
- Description: Create and use functions with parameters in Python
"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""

# Create a function named say_hello that accepts a person's name as a parameter and prints "Hello" followed by the name.
def say_hello(name):
    print(f"hello {name}")


# Develop a function named triple that takes one number as a parameter and returns the number multiplied by three.
number=3

def triple(number):
    multiply=(number * 3)
    return(multiply)





# Write a function called add that takes two numbers as parameters and returns their sum. 

#defining numbers
num1=2
num2=4

#function that adds numbers.
def add(sum):
    sum=(num1+num2)
    return(sum)


# Create a function named draw_line that takes one parameter for the length of the line and prints a straight line of that many hyphens.

length=52

def draw_line(hyphens):
    hyphens=(length * "-")
    return(hyphens)

# Call your functions, printing out the return result where appropriate

x=triple(number)
print(x)

y=add(sum)
print(y)

z=draw_line(length)
print(z)



