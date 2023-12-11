# Chapter 1 Exercise 3: Is it Triangle

# Defining a function to check if the entered lengths form a triangle
def check_triangle(a, b, c):
    return a + b > c and b + c > a and c + a > b

# Defining a function to determine the type of triangle based on its side lengths
def type_of_triangle(a, b, c):
    # Checking if all three sides are equal, which indicates an equilateral triangle.
    if a == b == c:
        return "Equilateral"
    # Checking if at least two sides are equal, which indicates an isosceles triangle.
    elif a == b or b == c or c == a:
        return "Isosceles"
    # If conditions are not met, then it's a scalene triangle.
    else:
        return "Scalene"

def valid():
    # The main function for taking user input and determining triangle validity and type
    print("Enter the three sides of the triangle to check if it's valid or invalid:")
    side_a = float(input("Side A: "))
    side_b = float(input("Side B: "))
    side_c = float(input("Side C: "))

    if check_triangle(side_a, side_b, side_c):
        # If the sides are forming a valid triangle, then determining the type
        print("The entered lengths of the sides form a valid triangle.")
        classifying_triangle = type_of_triangle(side_a, side_b, side_c)
        print(f"The triangle is {classifying_triangle}.")
    else:
        # If the sides do not form a valid triangle, inform the user
        print("The entered lengths of the sides do not form a valid triangle.")

# Executing the main function
valid()
