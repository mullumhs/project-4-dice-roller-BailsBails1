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

def get_sides():

    while True:
        try:
            sides=input(int(prompt))
            
            return sides 
        
        except:
            print("please enter a valid choice")




get_sides()


'''
def output():
    for i in range(qty)

'''


#print output with total.




