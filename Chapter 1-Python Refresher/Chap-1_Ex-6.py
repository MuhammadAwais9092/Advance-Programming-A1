# Chapter 1 Exercise 6: FizzBuzz

# Defining function to perform the FizzBuzz operation from numbers 1 to 100
def fizz_or_buzz():
    for a in range(1, 101):
        # Checking if the number is divisible by both 3 and 5
        if a % 3 == 0 and a % 5 == 0:
            print("FizzBuzz")
        # Checking if the number is divisible by 3
        elif a % 3 == 0:
            print("Fizz")
        # Checking if the number is divisible by 5
        elif a % 5 == 0:
            print("Buzz")
        # If none of the above conditions are applicable, print the number itself
        else:
            print(a)

# Executing the fizz_buzz function
fizz_or_buzz()
