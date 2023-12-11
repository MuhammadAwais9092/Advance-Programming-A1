# Chapter 1 Bonus B: Locations List

# Given list
locations = ['dubai', 'paris', 'switzerland', 'London', 'amsterdam', 'New York']

# Print the original list and find its length
print("Original List:", locations)
print("Length of the List:", len(locations))

# Use sorted() to print the list in alphabetical order without modifying the actual list
sorted_alphabetical = sorted(locations)
print("\nSorted in Alphabetical Order:", sorted_alphabetical)

# Print the original list to show that it's still in its original order
print("Original List (unchanged):", locations)

# Use sorted() to print the list in reverse alphabetical order without changing the order of the original list
sorted_reverse = sorted(locations, reverse=True)
print("\nSorted in Reverse Alphabetical Order:", sorted_reverse)

# Print the original list to show that it's still in its original order
print("Original List (unchanged):", locations)

# Use reverse() to change the order of the list
locations.reverse()
print("\nReversed List:", locations)

# Use sort() to change the list so it's stored in alphabetical order
locations.sort()
print("\nList Sorted in Alphabetical Order:", locations)

# Use sort() to change the list so it's stored in reverse alphabetical order
locations.sort(reverse=True)
print("\nList Sorted in Reverse Alphabetical Order:", locations)