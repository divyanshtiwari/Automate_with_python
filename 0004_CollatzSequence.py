import sys
def collatz(number):
    if number % 2 ==0 :
        return number //2
    else :
        return 3*number + 1
try:
    number = int(input("Enter number to start Collatz Sequence from : "))
    while number != 1 :
        number = collatz(number)
        print(number)
except ValueError :
    print("You have not entred a valid input, the input should be a valid integer.")
    sys.exit()