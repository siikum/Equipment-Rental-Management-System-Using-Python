from datetime import datetime
from read import *
from operation import *

# Calling Function for Welcome Message
welcome_message()

loop=True
while loop==True:
    try:
        #displaying options to the user
        userinput=display_opt()
        
        if userinput == 1:
            rent_function()
            print("Your item has been rented")

        elif userinput == 2:
            return_function()
            print("Your item has been returned")
            
        elif userinput == 3:
            print("Thank you for visting us")
            loop = False
        
        elif userinput > 3 or userinput < 0:
            print("Enter the correct option")
    except ValueError:
        print("Invalid Entry. Please Enter a valid numerical option")
