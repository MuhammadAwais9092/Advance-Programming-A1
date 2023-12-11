# Chapter 1 Exercise 1: User Input Output

# Using print for the opening statement
print("Hello! Mr/Mrs,")

# Using input function to gather data from the user
User_name = input("Please state your name?\n").title()
# Using input function to gather data from the user
Users_age = int(input("And your age?\n"))

# Using print function to print again and calling the variable for the users name
print(f"It is very nice meeting you, {User_name}.")

# Writing the code for the calculations of the length of the name using len function
name_length = len(User_name)
# Printing the length of the name and calling the variable of the length
print(f"Your name consists of '{name_length}' numbers of alphabets.")

# Writing the code for adding one in the users age by calling the variable
adding_age = Users_age + 1
print(f"You will be turning {adding_age} in a years time.")