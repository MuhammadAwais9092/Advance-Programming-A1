# Chapter 2 Bonus B: Age Calculator

# Importing date and time from datetime library
from datetime import datetime
import tkinter as tk

# Defining function for handling every click event
def entry_click(event):
    if enter_date.get() == 'MM/DD/YYYY':
        enter_date.delete(0, "end")  # Clearing the default text
        enter_date.config(fg='black')  # Changing text color to black

# Defining function for calculating the age
def age_calculation():
    try:
        # Getting the user input for date of birth
        dob_str = enter_date.get()

        # Checking if the default text is entered
        if dob_str == 'MM/DD/YYYY':
            raise ValueError("Invalid Input")

        d_o_b = datetime.strptime(dob_str, "%m/%d/%Y")

        # Codes for calculating the age
        today = datetime.today()
        age = today.year - d_o_b.year - ((today.month, today.day) < (d_o_b.month, d_o_b.day))

        # Displaying the final result
        result.set(f"Your age is {age} years")
        text_label.config(text="")  # Remove the text "How are you?"

    # Displaying the error message if data not entered per the specification
    except ValueError:
        result.set("Invalid Input")
        text_label.config(text="")


# Creating the the main window
root = tk.Tk()
root.title("Age Calculator")

# Variables for input from the user and result
enter_date = tk.Entry(root, width=20, fg='grey')
enter_date.insert(0, 'MM/DD/YYYY')  # Setting default text
enter_date.bind("<FocusIn>", entry_click)  # Binding the click event
result = tk.StringVar()

# Creating a label to cover the entire background
background_label = tk.Label(
    root,
    text="",  # Empty text
    font=("Helvetica", 12),
    bg="lightblue",  # Setting background color
)
background_label.pack(expand=True, fill='both')  # Expand to fill the available space

# styling the Widgets
tk.Button(root, text="Calculate Age", command=age_calculation).pack(pady=10)
text_label = tk.Label(
    root,
    text="Please! Enter Your Age in the given Format.\n 'MM/DD/YYYY'",
    font=("Helvetica", 12),
    bg="lightblue",
)
text_label.pack(pady=10)
enter_date.pack(pady=10)
tk.Label(root, textvariable=result).pack(pady=10)

# Running the main loop
root.mainloop()

