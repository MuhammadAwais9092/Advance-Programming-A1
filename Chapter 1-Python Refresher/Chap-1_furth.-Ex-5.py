# Chapter 1 Exercise 12: Area Function


# Given list of tuples
marks = [("CodeLab I", 67), ("Web Development", 75), ("CodeLab II", 74), ("Smartphone Apps", 68), ("Games Development", 70), ("Responsive Web", 65)]

# Sorting the list based on marks low to high
low_to_high = sorted(marks, key=lambda x: x[1])

# Sorting the list based on marks high to low
high_to_low = sorted(marks, key=lambda x: x[1], reverse=True)

# Display the sorted lists

# Displaying the sorted list from low to high
print("Sorted by marks low to high:")
for subject, mark in low_to_high:
    print(f"{subject}: {mark}")

# Displaying the sorted list from high to low
print("\nSorted by marks high to low:")
for subject, mark in high_to_low:
    print(f"{subject}: {mark}")