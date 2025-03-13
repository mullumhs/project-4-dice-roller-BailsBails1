"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
                                    LAB 3
---------------------------------------------------------------------------------
- File Name: lab3.py
- Teacher: David Steedman
- Class: Software Engineering
- Description: Learn how to use exception handling in Python
"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""

# Define a function called get_number(prompt) that returns an integer. 
# Include a while loop and try/except blocks inside the function to handle non-integer inputs.


  #makes a function to get a number


def get_number():
      #makes a while true loop to continue the program forever if an invalid input is entered
      while True:
        #asks user for a number and stores it 
        try:
          number=int(input("enter a number: "))
          return(number)
         #if user enters anything but a valid number a prompt is displayed and question is asked again 
        except:
          print("please enter a valid integer")
          
  #makes the function under x and prints the answer.



   
    
            





    


# Use the get_number function to ask for a numerator, then again for a denominator.
# Divide the numerator by the denominator and print the result, handling any division by zero errors.


while True:
  try:
      numerator= get_number()
      denominator=get_number()
      
      answer=(numerator/denominator)
      print(answer)
      break
     
      
      
  except:
      print("please enter a valid number")

     

# Use the get_number function to ask the user for an index to access an element from a predefined list. 
# Print out the value from the list, handling the index error if the user selects a non-existent index.

my_list = ["beer","wine","spirits"]

