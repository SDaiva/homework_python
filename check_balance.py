from deposit1 import deposit_1
from withdrawal1 import withdrawal_1
balance = 0
deposit = deposit_1
withdrawal = withdrawal_1
balance = balance + deposit - withdrawal
print("Total balance is",  balance)




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