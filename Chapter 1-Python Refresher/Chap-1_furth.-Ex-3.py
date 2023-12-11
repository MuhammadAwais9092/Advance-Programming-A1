# Chapter 1 Exercise 12: Area Function


# Defining a function to print the asterisk pattern
def print_asterisk_pattern(rows):
    for a in range(1, rows + 1):
        # Print spaces
        for b in range(rows - a):
            print(" ", end="")
        # Print asterisks
        for k in range(2 * a - 1):
            print("*", end="")
        # Move to the next line after each row
        print()

# Number of rows in the pattern
rows = 5

# Call the function to print the asterisk pattern
print_asterisk_pattern(rows)