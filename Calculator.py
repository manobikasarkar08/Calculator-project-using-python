# Simple Python Calculator 
# Author: Manobika Sarkar
# Description: Performs basic arithmetic operations directly without functions.

print("Welcome to the Python Calculator!")
print("Select Operation:")
print("1. Add")
print("2. Subtract")
print("3. Multiply")
print("4. Divide")

# Taking user input for operation
choice = input("Enter choice (1/2/3/4): ")

# Taking user input for numbers
try:
    num1 = float(input("Enter first number: "))
    num2 = float(input("Enter second number: "))
except ValueError:
    print("Invalid input! Please enter numeric values.")
    exit()

# Performing operations without functions
if choice == '1':
    result = num1 + num2
    print("Result:", result)
elif choice == '2':
    result = num1 - num2
    print("Result:", result)
elif choice == '3':
    result = num1 * num2
    print("Result:", result)
elif choice == '4':
    if num2 != 0:
        result = num1 / num2
        print("Result:", result)
    else:
        print("Error! Division by zero.")
else:
    print("Invalid choice! Please select 1, 2, 3 or 4.")
