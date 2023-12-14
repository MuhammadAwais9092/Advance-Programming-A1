# Chapter 4 Exercise 1: User information

# Importing tkinter library and its modules
import tkinter as tk
from tkinter import ttk

# Defining a function for saving the data
def save_info():
    # Geting user input
    name = entry_name.get()
    age = entry_age.get()
    hometown = entry_hometown.get()

    # Write data to the file
    file_path = "bio.txt"
    with open(file_path, "w") as file:
        file.write(f"Name: {name}\n")
        file.write(f"Age: {age}\n")
        file.write(f"Hometown: {hometown}\n")

# Defining function for bio data input
def read_info():
    # Reading data from the file
    file_path = "bio.txt"
    try:
        with open(file_path, "r") as file:
            bio_data = file.read()
        text_output.delete(1.0, tk.END)  # Clearing the previous output
        text_output.insert(tk.END, bio_data)
    except FileNotFoundError: # If data not entered show the error
        text_output.delete(1.0, tk.END)
        text_output.insert(tk.END, "Entered Bio file not found. Please save your bio first.")

# Creating the main window
root = tk.Tk()
root.title("Bio Data App")

# Creating a frame to hold the controls
frame = ttk.Frame(root, padding=20)
frame.grid(row=0, column=0)

# Creating the entry widgets for user input
label_name = ttk.Label(frame, text="Name:")
label_age = ttk.Label(frame, text="Age:")
label_hometown = ttk.Label(frame, text="Hometown:")
entry_name = ttk.Entry(frame)
entry_age = ttk.Entry(frame)
entry_hometown = ttk.Entry(frame)

# Setting the grid layout for labels and entry widgets
label_name.grid(row=0, column=0, padx=10, pady=10, sticky="e")
entry_name.grid(row=0, column=1, padx=10, pady=10)
label_age.grid(row=1, column=0, padx=10, pady=10, sticky="e")
entry_age.grid(row=1, column=1, padx=10, pady=10)
label_hometown.grid(row=2, column=0, padx=10, pady=10, sticky="e")
entry_hometown.grid(row=2, column=1, padx=10, pady=10)

# Creating buttons for saving and reading bio
button_save = ttk.Button(frame, text="Save Bio", command=save_info)
button_save.grid(row=3, column=0, columnspan=2, pady=20)
button_read = ttk.Button(frame, text="Read Bio", command=read_info)
button_read.grid(row=4, column=0, columnspan=2, pady=20)

# Creating the text widget to display bio data
text_output = tk.Text(root, width=40, height=10)
text_output.grid(row=1, column=0, padx=20, pady=20)

# Running the Tkinter loop
root.mainloop()