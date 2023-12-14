# Chapter 6 Exercise 3: Calculator

# Importing operator library
import operator

# Defining function to perform addition
def add(x, y):
    return operator.add(x, y)

# Defining function to perform subtraction
def subtract(x, y):
    return operator.sub(x, y)

# Defining function to perform multiplication
def multiply(x, y):
    return operator.mul(x, y)

# Defining function to perform division
def divide(x, y):
    if y != 0:
        return operator.truediv(x, y)
    else:
        return "Unable to divide by zero"

# Defining function to calculate modulus
def modulus(x, y):
    return operator.mod(x, y)

# Defining function to check and return the greater number
def checking_greater(x, y):
    return f"{max(x, y)} is greater"

# Defining function to get user input for the calculator
def getting_input():
    try:
        # Getting user input for the operation choice
        choose = input("Choose operation (1-6) or Q to quit: ").upper()
        if choose == 'Q': # Using if statement for choice selection
            return 7, None, None  # Returning a different choice value for quitting
        else:
            choose = int(choose)
            # Checking if the choice is within the valid range or not
            if choose < 1 or choose > 6: # Using if statement for choice condition
                raise ValueError("Invalid choice") # If not show invalid
            x = float(input("Enter first number: "))
            y = float(input("Enter second number: "))
            return choose, x, y
    except ValueError:
        print("Invalid input. Please enter a valid choice and numerical values.")
        return None, None, None

# Defining Main function to run the calculator
def main():
    while True:
        print("\nCalculation Menu: Select your choice")
        print("1. Add\n2. Subtract\n3. Multiply\n4. Divide\n5. Modulus\n6. Check greater number")

        # Getting user input for the operation choice and numbers
        choose, x, y = getting_input()

        # Using if statement for choice selection
        if choose is None:
            continue

        if choose == 6:
            final = checking_greater(x, y)
            print(f"Result: {final}")
        elif choose == 7:
            print("Exiting calculator. Goodbye!")
            break
        elif 1 <= choose <= 5:
            operations = [add, subtract, multiply, divide, modulus]
            # Performing the selected operation and print the result
            final = operations[choose - 1](x, y)
            print(f"Result: {final}")

# Running the main function
if __name__ == "__main__":
    main()
