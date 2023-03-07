def printmenu():
    print()
print(""" 
    1. Check balance
    2. Deposit
    3. Withdrawal
    4. Exit 
    """)

def my_choice():
    while True:
        amount = int(input('Test'))
        try:
            val = int(amount)
            if val == 1:
                print("xxxxx")
            else: print("yyy")
    return val