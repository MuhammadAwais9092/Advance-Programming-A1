# Chapter 1 Exercise 4: Largest Number

# Defining a function to find the largest number among three input numbers
def find_largest_number(a, b, c):
    # Comparing the numbers to find the largest
    if a >= b and a >= c:
        return a
    elif b >= a and b >= c:
        return b
    else:
        return c

# Defining main function to take user input and find the largest number
def main():
    print("Enter the three numbers:")
    num1 = float(input("Number 1: "))
    num2 = float(input("Number 2: "))
    num3 = float(input("Number 3: "))

    # Calling the function to find the largest number
    largest_number = find_largest_number(num1, num2, num3)
    print(f"The largest number is: {largest_number}")

# Executing the main function
main()
