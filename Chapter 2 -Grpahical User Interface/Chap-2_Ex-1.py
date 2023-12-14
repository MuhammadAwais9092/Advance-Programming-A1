# Chapter 2 Exercise 1: Welcome

# Importing tkinter library
import tkinter as tk
from tkinter import font

# Defining function for changing the fonts
def changing_font():
    font_new = font.Font(label_for_frame, label_for_frame.cget("font"))
    font_new.config(family="Arial", weight="bold", size=16)
    label_for_frame.configure(font=font_new)

# Creating the main window
root = tk.Tk()
root.title("Welcome Message")

# Setting the default window size
root.geometry("400x300")

# Disabling the resizing of the window
root.resizable(False, False)

# Adding background color to the window
root.configure(bg="#ff1f1f")

# Creating a frame
frame = tk.Frame(root, bg="#ff1f1f")

# Creating a label in the frame
label_for_frame = tk.Label(frame, text="Hello there! Welcome to My GUI Prog.!", font=("Helvetica", 14), bg="#ff1f1f")
label_for_frame.pack(pady=20)

# Creating a button to change the font style
changing_font_button = tk.Button(frame, text="Change Font", command=changing_font)
changing_font_button.pack()

# Packing the frame into the main window
frame.pack(expand=True, fill="both")

# Running the main loop
root.mainloop()