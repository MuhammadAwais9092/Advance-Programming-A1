# Chapter 6 Exercise 2: Numpy Array

# Importing the numpy library
import numpy as np

# The given array
a = np.array([20, 23, 82, 40, 32, 15, 67, 52])

# Finding the indices of even numbers
indices_even = np.where(a % 2 == 0)
print(f"Indices of even numbers: {indices_even}")

# Sorting the array
array_sorted = np.sort(a)
print(f"Sorted array: {array_sorted}")

# Slicing the elements beginning from index 3 to the end of the array
slice_01 = a[3:]
print(f"Slice from index 3 to the end: {slice_01}")

# Slicing the elements beginning from index 0 to index 4
slice_02 = a[:5]
print(f"Slice from index 0 to index 4: {slice_02}")

# Printing the following [32 15 67] using negative slicing
slice_negative = a[-5:-2]
print(f"Negative slicing to get [32 15 67]: {slice_negative}")
