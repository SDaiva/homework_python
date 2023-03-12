from deposit1 import deposit_1
from withdrawal1 import withdrawal_1
balance = 0
deposit = deposit_1
withdrawal = withdrawal_1
balance = balance + deposit - withdrawal
print("Total balance is",  balance)

receipt = input("Do you need a receipt? Y/N: ")
if receipt == "Y":
    print("Here is your receipt and come back to main menu")
else:
    print("Come back to maim menu")





"""""""""""
#from file import variable
#from file2 import variable
balance = 0
#deposit = variable1
#withdrawal = variable2
balance = balance + deposit - withdrawal
print("Total balance is",  balance)


import sys

def exit():
    # clean up resources
    sys.exit()
    
    
    

receipt = input("Do you need a receipt? Y/N: ")
if receipt == "Y":
    print("Here is your receipt", "come back to main menu")
else:
    print("Come back to maim menu")
"""""""""""