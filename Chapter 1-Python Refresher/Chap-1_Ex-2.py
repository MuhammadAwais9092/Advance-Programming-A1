# Chapter 1 Exercise 1: Maths

# Getting the integer from the user
num1 = int(input("Enter the first number: "))
num2 = int(input("Enter the second number: "))

# Creating variables for the calculations and writing codes for it
cal_sum = num1 + num2
cal_diff = num1 - num2
cal_product = num1 * num2
# Writing code for checking if the second number is not zero before performing division
if num2 != 0:
    cal_quot = num1 / num2
    cal_remain = num1 % num2
else: # If number is 0 then print the following
    cal_quot = "Undefined (division by zero)"
    cal_remain = "Undefined (division by zero)"

# Printing the result of the calculations
print(f"Sum: {cal_sum}")
print(f"Difference: {cal_diff}")
print(f"Product: {cal_product}")
print(f"Quotient: {cal_quot}")
print(f"Remainder: {cal_remain}")