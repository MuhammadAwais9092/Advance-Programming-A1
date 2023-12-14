# Chapter 2 Exercise 2 b: Square Grid

# Importing tkinter library
import tkinter as tk

# Defining a function for creating square grids
def creating_square_grid():
    root = tk.Tk()
    root.title("Square Grid with Labels")

    # Creating frames with a border of 5
    left_frame = tk.Frame(root, bd=5)
    right_frame = tk.Frame(root, bd=5)

    # Creating labels for the frames
    label_a = tk.Label(left_frame, text="A", padx=10, pady=5, bd=5, relief=tk.GROOVE, bg="#2f2e42", fg="white")
    label_b = tk.Label(left_frame, text="B", padx=10, pady=5, bd=5, relief=tk.GROOVE, bg="white")
    label_c = tk.Label(right_frame, text="C", padx=10, pady=5, bd=5, relief=tk.GROOVE, bg="white")
    label_d = tk.Label(right_frame, text="D", padx=10, pady=5, bd=5, relief=tk.GROOVE, bg="#2f2e42", fg="white")

    # Packing the labels with expand and fill options
    label_a.pack(side=tk.TOP, fill=tk.BOTH, expand=1)
    label_b.pack(side=tk.BOTTOM, fill=tk.BOTH, expand=1)
    label_c.pack(side=tk.TOP, fill=tk.BOTH, expand=1)
    label_d.pack(side=tk.BOTTOM, fill=tk.BOTH, expand=1)

    # Packing the frames with a border of 5, expand, and fill options
    left_frame.pack(side=tk.LEFT, fill=tk.BOTH, expand=1)
    right_frame.pack(side=tk.LEFT, fill=tk.BOTH, expand=1)

    # Running the mainloop
    root.mainloop()

# Call the function to create the square grid
creating_square_grid()