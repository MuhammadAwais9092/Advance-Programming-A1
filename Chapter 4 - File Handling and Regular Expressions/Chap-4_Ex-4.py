# Chapter 4 Exercise 4: letter count

# Importing tkinter library and its modules
import tkinter as tk
from tkinter import filedialog

# Defining function for the amount of number occurrence
def count_occurrences():
    # Getting the selected file
    file_path = file_var.get()

    # Reading the content of the file
    try:
        with open(file_path, "r") as file:
            content = file.read()

        # Getting the character entered by the user
        char_to_count = char_entry.get()

        # Counting occurrences of the character
        char_count = content.count(char_to_count)

        # Displaying the result
        result_label.config(text=f"Occurrences of '{char_to_count}': {char_count}")

    except FileNotFoundError:
        result_label.config(text="File not found. Please select a valid file.")

# Creating the main window
root = tk.Tk()
root.title("Character Occurrence Counter")

# Creating a frame to hold the controls
frame = tk.Frame(root, padx=20, pady=20)
frame.pack()

# Creating an entry for file path
file_var = tk.StringVar()
file_entry = tk.Entry(frame, textvariable=file_var, state="readonly", width=40)
file_entry.grid(row=0, column=0, padx=10, pady=10)

# Creating a button to browse for a file
browse_button = tk.Button(frame, text="Browse", command=lambda: browse_file("sentences.txt"))
browse_button.grid(row=0, column=1, padx=10, pady=10)

# Creating an entry for the character
char_entry_label = tk.Label(frame, text="Enter a character:")
char_entry_label.grid(row=1, column=0, padx=10, pady=5, sticky="e")

char_entry = tk.Entry(frame, width=5)
char_entry.grid(row=1, column=1, padx=10, pady=5)

# Creating a button to count occurrences
count_button = tk.Button(frame, text="Count Occurrences", command=count_occurrences)
count_button.grid(row=2, column=0, columnspan=2, pady=20)

# Creating a label to display the result
result_label = tk.Label(frame, text="")
result_label.grid(row=3, column=0, columnspan=2, pady=5)

# Defining a function to browse for a file
def browse_file(default_filename):
    file_path = filedialog.askopenfilename(filetypes=[("Text Files", "*.txt")], initialfile=default_filename)
    file_var.set(file_path)

# Running the Tkinter event loop
root.mainloop()
