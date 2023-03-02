my_input = input("Write a positive number:")
factorial = 1
if my_input == 0:
    print("Factorial of 0 is 1")
else:
    for i in range (1,int(my_input)+1):
        factorial = factorial * i
    print("The factorial of", my_input, "is", factorial)