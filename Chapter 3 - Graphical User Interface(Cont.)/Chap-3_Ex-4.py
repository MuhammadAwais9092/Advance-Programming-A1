# Chapter 3 Exercise 4: Draw Shape

# Importing tkinter library and modules
import tkinter as tk
from tkinter import ttk

# Defining a function for drawing the shape
def draw_shape():
    canvas.delete("all")  # Clearing the canvas
    # Get the selected shape from the dropdown menu
    shape_selected = shape_var.get()

    # Drawing the selected shape on the canvas
    if shape_selected == "Oval":
        # Drawing an oval with specified coordinates, outline, and fill color
        canvas.create_oval(100, 100, 300, 200, outline="black", fill="red")
    elif shape_selected == "Rectangle":
        # Drawing a rectangle with specified coordinates, outline, and fill color
        canvas.create_rectangle(100, 100, 300, 200, outline="black", fill="green")
    elif shape_selected == "Square":
        # Drawing a square with specified coordinates, outline, and fill color
        canvas.create_rectangle(100, 100, 200, 200, outline="black", fill="blue")
    elif shape_selected == "Triangle":
        # Drawing a triangle with specified coordinates, outline, and fill color
        canvas.create_polygon(100, 200, 200, 100, 300, 200, outline="black", fill="yellow")

# Creating the main window
root = tk.Tk()
root.title("Shape Drawer")

# Creating a frame to hold the controls
frame = ttk.Frame(root, padding=20)
frame.grid(row=0, column=0)

# Creating a Label and Combobox for shape selection
label_shape = ttk.Label(frame, text="Select Shape:")
label_shape.grid(row=0, column=0, padx=10, pady=10)

# Setting the shapes
shapes = ["Oval", "Rectangle", "Square", "Triangle"]
shape_var = tk.StringVar()
shape_combobox = ttk.Combobox(frame, textvariable=shape_var, values=shapes)
shape_combobox.grid(row=0, column=1, padx=10, pady=10)
shape_combobox.set(shapes[0])  # Set the default shape

# Creating a button to draw the selected shape
draw_button = ttk.Button(frame, text="Draw Shape", command=draw_shape)
draw_button.grid(row=1, column=0, columnspan=2, pady=20)

# Creating a canvas to draw the shapes
canvas = tk.Canvas(root, width=400, height=300, borderwidth=2, relief="solid")
canvas.grid(row=1, column=0, padx=20, pady=20)

# Running the Tkinter event loop
root.mainloop()
