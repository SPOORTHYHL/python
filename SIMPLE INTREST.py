# Taking input from user
principal = float(input("Enter principal amount: "))
rate = float(input("Enter rate of interest: "))
time = float(input("Enter time in years: "))

# Calculating simple interest
simple_interest = (principal * rate * time) / 100

# Displaying the result
print("Simple interest = ", simple_interest)
