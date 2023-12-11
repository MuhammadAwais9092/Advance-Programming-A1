# Chapter 1 Exercise 13: Product of list items

def calculating_the_product(value_in_list):
    # Initializing the number to 1 so if multiplied the value remains the same
    number = 1

    # Multiplying each number in the list
    for value in value_in_list:
        number *= value

    return number

# Making a list
my_list = [4, 6, 8, 7, 4]

# Creating a variable for the calculation of the result
result = calculating_the_product(my_list)

# Displaying the output(result)
print(f"The product of the values in the list is: {result}")