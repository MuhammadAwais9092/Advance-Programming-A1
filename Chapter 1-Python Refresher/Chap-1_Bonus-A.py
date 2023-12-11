# Chapter 1 Bonus A: Multiplication Tables

# Outer loop for each table from 1 to 10
for a in range(1, 11):
    print(f"\nMultiplication table of : {a}")

    # Inner loop for multiplying numbers from 1 to 10
    for b in range(1, 11):
        result = a * b
        print(f"{a} x {b} = {result}")