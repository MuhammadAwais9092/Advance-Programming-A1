# Chapter 1 Exercise 8: Print Pattern

# Defining a function to display a pattern with ascending numbers in each row
def displaying_pattern(rows):
    # Iterating in each row
    for a in range(1, rows + 1):
        # Iterating through each column in the current row
        for b in range(1, a + 1):
            # Printing the current number with a space at the end
            print(b, end=" ")
        # Move to the next line after printing all numbers in the current row
        print()

# Executing the display_pattern function
displaying_pattern(5)
