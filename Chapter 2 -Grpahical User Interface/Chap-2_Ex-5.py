# Chapter 2 Exercise 5: Calculator

# Importing the tkinter library
import tkinter as tk

# Defining the function for performing operations
def arithmetic_operations():
    # Using Try block to handle potential errors during calculation
    try:
        # Retrieving numerical inputs and selected operator
        first_number = float(enter_first_number.get())
        second_number = float(enter_second_number.get())
        operator = operation_var.get()

        # Performing the selected operation and updating the result
        if operator == "Addition":
            result.set(first_number + second_number)
        elif operator == "Subtraction":
            result.set(first_number - second_number)
        elif operator == "Multiplication":
            result.set(first_number * second_number)
        elif operator == "Division":
            result.set(first_number / second_number)
        elif operator == "Modulo":
            result.set(first_number % second_number)
        else:
            result.set("Invalid Operation")

    # Handling the ValueError that may occur if non-numeric input is provided
    except ValueError:
        result.set("Invalid Input")

# Creating the main window
root = tk.Tk()
root.title("Basic Arithmetic Calculator")

# Using entry function for user input, operation, and result
enter_first_number = tk.Entry(root, width=20)
enter_second_number = tk.Entry(root, width=20)
operation_var = tk.StringVar(value="Addition")
result = tk.StringVar()

# Styling the widgets
tk.OptionMenu(root, operation_var, "Addition", "Subtraction", "Multiplication", "Division", "Modulo").grid(row=1, column=0, columnspan=2, padx=10, pady=10)
tk.Button(root, text="Calculate", command=arithmetic_operations).grid(row=2, column=0, columnspan=2, padx=10, pady=10)
tk.Label(root, textvariable=result).grid(row=3, column=0, columnspan=2, padx=10, pady=10)

# Arranging the entry widgets
enter_first_number.grid(row=0, column=0, padx=10, pady=10)
enter_second_number.grid(row=0, column=1, padx=10, pady=10)

# Running the mainloop
root.mainloop()
