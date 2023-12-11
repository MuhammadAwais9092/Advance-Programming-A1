# Chapter 1 Exercise 12: Area Function

# Importing math library for math calculations
import math

# Defining function to calculate the area of a square
def calculating_square_area():
    length_of_side = float(input("Enter the side length of the square: "))
    area = length_of_side ** 2
    print(f"The area of the square is: {area}")

# Defining function to calculate the area of a circle
def calculating_circle_area():
    radius = float(input("Enter the radius of the circle: "))
    area = math.pi * (radius ** 2)
    print(f"The area of the circle is: {area:.2f}")

# Defining function to calculate the area of a triangle
def calculating_triangle_area():
    base = float(input("Enter the base length of the triangle: "))
    height = float(input("Enter the height of the triangle: "))
    area = 0.5 * base * height
    print(f"The area of the triangle is: {area}")

# Displaying the menu
while True:
    # Printing the menu options
    print("\nMenu:")
    print("1: Calculate the area of a square")
    print("2: Calculate the area of a circle")
    print("3: Calculate the area of a triangle")
    print("4: Exit")

    # Taking user input for menu choice
    choice = input("Enter your choice (1-4): ")

    # Checking the user's choice and calling the corresponding function
    if choice == "1":
        calculating_square_area()  # Calling function to calculate the area of a square
    elif choice == "2":
        calculating_circle_area()  # Calling function to calculate the area of a circle
    elif choice == "3":
        calculating_triangle_area()  # Calling function to calculate the area of a triangle
    elif choice == "4":
        print("Exiting the program. Goodbye!")
        break  # Exiting the loop and ending the program
    else:
        print("Invalid choice. Please enter a number between 1 and 4.")  # Informing the user about an invalid choice

