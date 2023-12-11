# Chapter 1 Exercise 12: Area Function


# Defining function to calculate seconds from days
def calculating_seconds(days):
    hours = days * 24
    minutes = hours * 60
    seconds = minutes * 60
    return seconds

# Getting input from the user
try:
    days = float(input("Enter the number of days: "))
    if days < 0:
        raise ValueError("Please enter a non-negative number of days.")
except ValueError as e:
    print(f"Error: {e}")
else:
    # Calculating seconds and displaying the result
    total_seconds = calculating_seconds(days)
    print(f"\nThe equivalent number of seconds in {days} days is: {total_seconds} seconds.")