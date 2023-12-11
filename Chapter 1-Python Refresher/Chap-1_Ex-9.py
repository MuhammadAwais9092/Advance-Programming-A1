# Chapter 1 Exercise 9: Integer List

# Creating an int list with 10 values
my_list = [5, 10, 3, 8, 1, 7, 2, 9, 4, 6]

# Output the list using a for loop
print("Original List:")
for num in my_list:
    print(num, end=" ")

# Output the highest and lowest value
print("\nHighest Value:", max(my_list))
print("Lowest Value:", min(my_list))

# Sort the elements in ascending order
my_list.sort()
print("\nAscending Order:", my_list)

# Sort the elements in descending order
my_list.sort(reverse=True)
print("Descending Order:", my_list)

# Append two elements
my_list.append(11)
my_list.append(0)

# Print the list after appending
print("\nList after Appending:")
for num in my_list:
    print(num, end=" ")