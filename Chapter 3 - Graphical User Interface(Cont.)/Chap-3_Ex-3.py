# Chapter 3 Exercise 3: Area Function

# Importing tkinter library and its module
import tkinter as tk
from tkinter import ttk
# Importing the math library
import math

# Defining function for the calculation of area of circle
def calculate_circle_area():
    try: # Codes for the calculation of area of circle
        radius = float(entry_circle_radius.get())
        area = math.pi * (radius ** 2)
        result_circle_var.set(f"The Area of the given Circle is: {area:.2f} square units")
    except ValueError:
        result_circle_var.set("The Input is Invalid. Please enter a valid number.")

# Defining function for the calculation of area of square
def calculate_square_area():
    try: # Codes for the calculation of area of square
        side_length = float(entry_square_side.get())
        area = side_length ** 2
        result_square_var.set(f"The Area of the given Square ia: {area:.2f} square units")
    except ValueError:
        result_square_var.set("The Input is Invalid. Please enter a valid number.")

# Defining function for the calculation of area of rectangle
def calculate_rectangle_area():
    try: # Codes for the calculation of area of rectangle
        length = float(entry_rectangle_length.get())
        width = float(entry_rectangle_width.get())
        area = length * width
        result_rectangle_var.set(f"The Area of the given Rectangle is: {area:.2f} square units")
    except ValueError:
        result_rectangle_var.set("The Input is Invalid. Please enter valid numbers.")

# Creating the main window
root = tk.Tk()
root.title("Shape Area Calculator")

# Creating a notebook
notebook = ttk.Notebook(root)

# Creating the tabs for Circle, Square, and Rectangle
tab_circle = ttk.Frame(notebook)
tab_square = ttk.Frame(notebook)
tab_rectangle = ttk.Frame(notebook)

# Notebook output for Circle
notebook.add(tab_circle, text="Circle")
# Notebook output for square
notebook.add(tab_square, text="Square")
# Notebook output for rectangle
notebook.add(tab_rectangle, text="Rectangle")

notebook.pack(fill="both", expand=True)
# The Tab for circle
# Labels and entry for circle radius
label_circle_radius = tk.Label(tab_circle, text="Enter Radius:")
entry_circle_radius = tk.Entry(tab_circle)
button_calculate_circle = tk.Button(tab_circle, text="Calculate", command=calculate_circle_area)
result_circle_var = tk.StringVar()
label_result_circle = tk.Label(tab_circle, textvariable=result_circle_var)

# Grid layout for circle labels, entry, button, and result
label_circle_radius.grid(row=0, column=0, padx=10, pady=5)
entry_circle_radius.grid(row=0, column=1, padx=10, pady=5)
button_calculate_circle.grid(row=1, column=0, columnspan=2, pady=10)
label_result_circle.grid(row=2, column=0, columnspan=2)

# The Tab for square
# Labels and entry for square side length
label_square_side = tk.Label(tab_square, text="Enter Side Length:")
entry_square_side = tk.Entry(tab_square)
button_calculate_square = tk.Button(tab_square, text="Calculate", command=calculate_square_area)
result_square_var = tk.StringVar()
label_result_square = tk.Label(tab_square, textvariable=result_square_var)

# Grid layout for square labels, entry, button, and result
label_square_side.grid(row=0, column=0, padx=10, pady=5)
entry_square_side.grid(row=0, column=1, padx=10, pady=5)
button_calculate_square.grid(row=1, column=0, columnspan=2, pady=10)
label_result_square.grid(row=2, column=0, columnspan=2)

# The Tab for rectangle
# Labels and entry for rectangle length and width
label_rectangle_length = tk.Label(tab_rectangle, text="Enter Length:")
label_rectangle_width = tk.Label(tab_rectangle, text="Enter Width:")
entry_rectangle_length = tk.Entry(tab_rectangle)
entry_rectangle_width = tk.Entry(tab_rectangle)
button_calculate_rectangle = tk.Button(tab_rectangle, text="Calculate", command=calculate_rectangle_area)
result_rectangle_var = tk.StringVar()
label_result_rectangle = tk.Label(tab_rectangle, textvariable=result_rectangle_var)

# Grid layout for rectangle labels, entry, button, and result
label_rectangle_length.grid(row=0, column=0, padx=10, pady=5)
entry_rectangle_length.grid(row=0, column=1, padx=10, pady=5)
label_rectangle_width.grid(row=1, column=0, padx=10, pady=5)
entry_rectangle_width.grid(row=1, column=1, padx=10, pady=5)
button_calculate_rectangle.grid(row=2, column=0, columnspan=2, pady=10)
label_result_rectangle.grid(row=3, column=0, columnspan=2)
# Run the Tkinter event loop
root.mainloop()