
def printmenu():
    print()

print("""" 
    1. Check balance
    2. Deposit
    3. Withdrawal
    4. Exit 
    """)

i = int(input("Choose transaction number: "))
#while i==4:
if (i==1):
    print("balance")
elif(i==2):
    print("deposit")
elif(i==3):
    print("withdrawal")
elif(i==4):
    print("Thank you for using ATM. You exit the program")
else:
    print("Choose number 1, 2, 3, 4")


