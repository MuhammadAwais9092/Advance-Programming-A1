# Chapter 1 Exercise 12: Area Function


# Given list
staff = ["Arshiya", "Usman", "Iftikhar", "Usman", "Rafia", "Mary", "Anmol", "Zainab", "Iftikhar", "Arshiya", "Rafia", "Jake"]

# Creating an empty dictionary to store the counts
store_counts = {}

# Count the occurrences of each item in the list
for item in staff:
    # If the item is already in the dictionary, increment its count
    if item in store_counts:
        store_counts[item] += 1
    # If the item is not in the dictionary, add it with a count of 1
    else:
        store_counts[item] = 1

# Displaying the counts
print("Number of times each item appears in the list:")
for item, count in store_counts.items():
    print(f"{item}: {count} times")