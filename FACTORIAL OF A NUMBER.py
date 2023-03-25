# function to find the factorial of a number
def factorial(num):
    # base case
    if num == 0 or num == 1:
        return 1
    # recursive case
    else:
        return num * factorial(num - 1)

# main program
num = int(input("Enter a number: "))
# check if the input is non-negative
if num < 0:
    print("Factorial does not exist for negative numbers")
else:
    print("Factorial of", num, "is", factorial(num))
