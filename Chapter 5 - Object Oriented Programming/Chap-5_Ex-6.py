# Chapter 5 Exercise 6: Arithmetic Operation

# Importing modules from the tkinter library
from tkinter import *
from tkinter import messagebox

# Making a Class for performing arithmetic operations
class ArithmeticCalculator:
    def perform_operation(selected_operation, num1, num2):
        try:
            # To Perform the selected arithmetic operation
            if selected_operation == "Addition":
                return num1 + num2
            elif selected_operation == "Subtraction":
                return num1 - num2
            elif selected_operation == "Multiplication":
                return num1 * num2
            elif selected_operation == "Division":
                # Check for division by zero
                return num1 / num2 if num2 != 0 else messagebox.showerror("Error", "Cannot divide by zero.")
            elif selected_operation == "Exponentiation":
                return num1 ** num2
        except ValueError:
            # Handle invalid input values
            messagebox.showinfo("Error", "Please enter valid numeric values.")
            return

# Function to perform calculation when the "Calculate" button is clicked
def calculate_result():
    # Getting the selected arithmetic operation
    selected_operation = operation_var.get()

    try:
        # Getting values from entry widgets
        result = ArithmeticCalculator.perform_operation(selected_operation, float(num1_entry.get()), float(num2_entry.get()))
        if result:
            # Displaying the result in a messagebox pop-up
            messagebox.showinfo("Result", f"The result is: {result}")
    except ValueError:
        # Handle invalid input values
        messagebox.showinfo("Error", "Please enter valid numeric values.")

# Creating the main window
root = Tk()

# Setting the title for the window
root.title("Arithmetic Operations Calculator")

# Setting the window size
root.geometry("400x300")

# Widgets for Arithmetic Operations tab
arithmetic_tab = Frame(root, bg="#E6E6FA", pady=20)

# Label for selecting the arithmetic operation
operation_label = Label(arithmetic_tab, text='Select Operation:', font=("Helvetica", 12), bg="#E6E6FA")
operation_label.pack()

# Options for the arithmetic operations presented in a drop-down menu
operations = ["Addition", "Subtraction", "Multiplication", "Division", "Exponentiation"]
operation_var = StringVar()
operation_var.set(operations[0])
operation_option = OptionMenu(arithmetic_tab, operation_var, *operations)
operation_option.pack(pady=10)

# Labels and Entry widgets for inputting numeric values
num1_label = Label(arithmetic_tab, text="Enter Number 1:", font=("Helvetica", 12), bg="#E6E6FA")
num1_label.pack(pady=5)
num1_entry = Entry(arithmetic_tab, font=("Helvetica", 12))
num1_entry.pack(pady=5)

num2_label = Label(arithmetic_tab, text="Enter Number 2:", font=("Helvetica", 12), bg="#E6E6FA")
num2_label.pack(pady=5)
num2_entry = Entry(arithmetic_tab, font=("Helvetica", 12))
num2_entry.pack(pady=5)

# Button to trigger the calculation with specified text, command, font, and color
calculate_button = Button(arithmetic_tab, text='Calculate', command=calculate_result, font=("Helvetica", 12), bg="#4CAF50", fg="white")
calculate_button.pack(pady=10)

# Packing the Arithmetic Operations tab
arithmetic_tab.pack(fill=BOTH, expand=YES)

# Run the main event loop
root.mainloop()

# End Marker