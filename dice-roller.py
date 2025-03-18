"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
                                GUESSING GAME
---------------------------------------------------------------------------------
- File Name: dice-roller.py
- Teacher: David Steedman
- Class: Software Engineering
- Description: Complete a functional dice roller app in Python
"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
#show each individual roll
#pick type of die
#pick how many rolls
#input validation



#title.
print("welcome to dice roller!")




#import random
import random



#make function that takes number of sides 


def get_number(prompt):
    #makes a while true loop to continue the program forever if an invalid input is entered 
    while True:
        #asks user for a number and stores it 
        try:
            number=int(input(prompt))
            return(number)
            #if user enters anything but a valid number a prompt is displayed and question is asked again 
        except:
            print("please enter a valid integer")
          

          

def roll(sides, qty):
    total = 0
    for i in range(1, qty+1):
        rnd = random.randint(1, sides)
        total = total + rnd
        print(rnd)
    print(f"The total is {total}")



sides=get_number("how many sides would you have on your dice:  ")
qty=get_number("how many times yould you like to roll the dice: ")
 
roll(sides,qty)
        
    
   


   











#print output with total.




