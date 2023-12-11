# Chapter 1 Bonus C: Calculators Function

# Defining function for adding two numbers
def adding(a, b):
    return a + b

# Defining function for subtracting two numbers
def subtracting(a, b):
    return a - b

# Defining function for multiplying two numbers
def multiplying(a, b):
    return a * b

# Defining function for dividing two numbers
def dividing(a, b):
    if b != 0:
        return a / b
    else:
        return "Unable to divide by zero."

# Defining function to calculate modulus of two numbers
def modulus(a, b):
    if b != 0:
        return a % b
    else:
        return "Cannot calculate modulus with zero divisor."

# Main loop for calculator functionality
while True:
    # Display calculator menu
    print("\nCalculator Menu:")
    print("a. Add")
    print("b. Subtract")
    print("c. Multiply")
    print("d. Divide")
    print("e. Modulus")

    # Get user's choice
    choice = input("Enter your choice (a-e): ")

    # Input values for the calculation
    num1 = float(input("Enter the first number: "))
    num2 = float(input("Enter the second number: "))

    # Perform calculation based on user's choice
    if choice == "a":
        result = adding(num1, num2)
    elif choice == "b":
        result = subtracting(num1, num2)
    elif choice == "c":
        result = multiplying(num1, num2)
    elif choice == "d":
        result = dividing(num1, num2)
    elif choice == "e":
        result = modulus(num1, num2)
    else:
        print("Invalid choice. Please enter a number between a to e.")
        continue

    # Display the result
    print(f"\nResult: {result}")

    # Asking the user if they are looking to perform another calculation
    more_cal = input("Do you want to perform another calculation? (yes/no): ").lower()
    # If entered 'yes' the calculation will continue
    if more_cal == 'yes':
        continue
    # If entered 'no' the calculation will stop
    elif more_cal == 'no':
        print("Exiting the calculator. Goodbye!")
        break
