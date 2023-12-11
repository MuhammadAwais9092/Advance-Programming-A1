# Chapter 1 Exercise 12: Area Function


# Get input from the user with error handling
while True:
    try:
        number = int(input("Enter a non-negative integer: "))
        if number < 0:
            raise ValueError("Please enter a non-negative integer.")
        break  # Break out of the loop if input is valid
    except ValueError as e:
        print(f"Error: {e}")

# Calculate the sum of digits and display the result
digit_sum = sum(map(int, str(number)))
print(f"The sum of digits in {number} is: {digit_sum}")