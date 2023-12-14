# Chapter 5 Exercise 4: Shapes

# Importing tkinter library
import tkinter as tk

# Importing math library
from math import pi

#  Making a class for shape
class Shape:
    # Defining function for storing the sides
    def __init__(self):
        self.sides = []  # Initializing a list to store the sides of the shape

# Defining function for the sides
    def input_sides(self):
        pass  # To implement it by subclasses, collecting the input for the sides

# Defining function for area
    def area(self):
        pass  # To implement it by subclasses, calculating and returning the area

#  Making a class for circle
class Circle(Shape):

    # Defining function for the input of the sides
    def input_sides(self):
        radius = float(input("Enter the radius of the circle: "))
        self.sides = [radius]  # Storing the radius in the sides list

    # Defining function for the area
    def area(self):
        return pi * self.sides[0] ** 2  # Calculating and returning the area of the circle

#  Making a class for rectangle
class Rectangle(Shape):

    # Defining function for input of the sides of rectangle
    def input_sides(self):
        length = float(input("Enter the length of the rectangle: "))
        width = float(input("Enter the width of the rectangle: "))
        self.sides = [length, width]  # Storing the length and width in the sides list

    # Defining function for input of area of rectangle
    def area(self):
        return self.sides[0] * self.sides[1]  # Calculating and returning the area of the rectangle

#  Making a class for triangle
class Triangle(Shape):

    # Defining function for the sides input of triangle
    def input_sides(self):
        base = float(input("Enter the base of the triangle: "))
        height = float(input("Enter the height of the triangle: "))
        self.sides = [base, height]  # Storing the base and height in the sides list

    # Defining function for the area of triangle
    def area(self):
        return 0.5 * self.sides[0] * self.sides[1]  # Calculating and returning the area of the triangle

#  Making a class for calculations
class ShapeCalculatorGUI(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Shape Area Calculator")
        self.geometry("400x300")
        self.create_widgets()

    # Defining function for the widgets
    def create_widgets(self):
        self.shape_label = tk.Label(self, text="Select a shape:")
        self.shape_label.pack()

        self.shape_var = tk.StringVar()
        self.shape_var.set("Circle")  # Default shape

        # The Option Menu for selecting a shape
        self.shape_menu = tk.OptionMenu(self, self.shape_var, "Circle", "Rectangle", "Triangle")
        self.shape_menu.pack()

        self.calculate_button = tk.Button(self, text="Calculate Area", command=self.calculate_area)
        self.calculate_button.pack()

        self.result_label = tk.Label(self, text="")
        self.result_label.pack()

    # Defining function to calculate the area
    def calculate_area(self):
        selected_shape = self.shape_var.get()
        current_shape = None  # Declaring the shape before the if statements

        # Using if statements to determine the type of shape based on user's selection
        if selected_shape == "Circle":
            current_shape = Circle()
        elif selected_shape == "Rectangle":
            current_shape = Rectangle()
        elif selected_shape == "Triangle":
            current_shape = Triangle()
        else:
            return

        # Collecting input for the selected shape
        current_shape.input_sides()

        # Calculating and displaying the area of the selected shape
        area_result = current_shape.area()
        self.result_label.config(text=f"Area of {selected_shape}: {area_result}")


# Running the ShapeCalculatorGUI class
app = ShapeCalculatorGUI()
app.mainloop()
