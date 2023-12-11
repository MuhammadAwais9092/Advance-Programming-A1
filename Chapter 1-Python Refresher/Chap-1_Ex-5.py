# Chapter 1 Exercise 5: Continue

# Defining main function to ask the user if they want to continue repeatedly
def main():
    Times = 0  # Initializing a counter for the number of times the loop is executed

    while True:
        # Prompting the user to enter 'Y' or 'N' to continue or exit the loop
        user_input = input("Do you want to continue? (Y/N): ").upper()

        # Exiting the loop if the user enters 'N'
        if user_input == 'N':
            break

        # Increasing the counter if the user enters 'Y'
        if user_input == 'Y':
            Times += 1
        else:
            print("Invalid input. Please enter 'Y' or 'N'.")

    # Displaying the number of times the loop was executed
    print(f"The loop was executed {Times} times.")

# Executing the main function
main()
