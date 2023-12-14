# Chapter 4 Exercise 3: Reading to a List

# Opening the file in read mode
with open('numbers.txt', 'r') as file:
    # Reading all lines from the file and converting each line to an integer
    numbers = [int(line.strip()) for line in file]

# Outputting the values in integer format
for number in numbers:
    print(number)
