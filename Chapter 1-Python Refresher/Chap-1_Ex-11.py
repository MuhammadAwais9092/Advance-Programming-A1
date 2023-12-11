# Chapter 1 Exercise 11: Year Tuples

# Create a tuple with values
year = (2017, 2003, 2011, 2005, 1987, 2009, 2020, 2018, 2009)

# Accessing the value at index -3
value_at_minus_3 = year[-3]
print("Value at index -3:", value_at_minus_3)

# Reversing the tuple and print the original tuple and reversed tuple
reversed_year = tuple(reversed(year))
print("\nOriginal Tuple:", year)
print("Reversed Tuple:", reversed_year)

# Counting the number of times 2009 is in the tuple (use count() method)
count_2009 = year.count(2009)
print("\nNumber of times 2009 is in the tuple:", count_2009)

# Getting the index value of 2018 using index method
index_of_2018 = year.index(2018)
print("\nIndex of 2018:", index_of_2018)

# Finding the length of the given tuple using len() method
tuple_length = len(year)
print("\nLength of the tuple:", tuple_length)