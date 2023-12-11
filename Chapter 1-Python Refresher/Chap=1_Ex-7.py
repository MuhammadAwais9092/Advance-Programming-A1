# Chapter 1 Exercise 7: Even Numbers

def print_even_numbers():
    # Using for loop to print even numbers from 1 to 100
    for a in range(1, 101):
        # Checking if the number is odd, and if it is, skip to the next continuation
        if a % 2 != 0:
            continue
        # Printing the even number
        print(a)

# Calling the function to print even numbers
print_even_numbers()
