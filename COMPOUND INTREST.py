# Taking input from user
principal = float(input("Enter principal amount: "))
rate = float(input("Enter rate of interest: "))
time = float(input("Enter time in years: "))
n = int(input("Enter the number of times interest is compounded per year: "))

# Calculating compound interest
amount = principal * pow((1 + (rate / n)), (n * time))
compound_interest = amount - principal

# Displaying the result
print("Compound interest = ", compound_interest)
