# Chapter 2 Exercise 4: Registration page

# Importing tkinter library
import tkinter as tk
from tkinter import ttk

# Defining function for data entry
def submit_form():
    # Retrieving and printing the entered data
    print("Student Name:", entry_name.get())
    print("Mobile Number:", entry_mobile.get())
    print("Email ID:", entry_email.get())
    print("Home Address:", entry_address.get())
    print("Gender:", var_gender.get())
    print("Course Enrolled:", var_course.get())
    print("Languages Known:", var_languages.get())
    print("Communication Skills:", scale_communication.get())

# Defining the function for data clearing
def clear_form():
    # Clear all entry fields and selections
    entry_name.delete(0, tk.END)
    entry_mobile.delete(0, tk.END)
    entry_email.delete(0, tk.END)
    entry_address.delete(0, tk.END)
    gender_choices.set("")  # Clear the combobox
    var_course.set("")  # Clear the radio buttons
    var_languages.set("")  # Clear the checkboxes
    scale_communication.set(0)  # Reset the scale

# Creating the main window
root = tk.Tk()
root.title("Student Management System")

# Codes for the university Picture
img = tk.PhotoImage(file='bath spa.png')
# Adjusting width and height using subsample
img = img.subsample(4, 4)  # Adjusting the values to control the size
label_picture = tk.Label(root, image=img)
label_picture.grid(row=0, column=0, columnspan=2)

# Text labels and entry widgets
tk.Label(root, text="Student Management System").grid(row=1, column=0, columnspan=2)
tk.Label(root, text="New Student Registration").grid(row=2, column=0, columnspan=2)

# Creating labels and entry widgets for student information

# Student Name
tk.Label(root, text="Student Name:").grid(row=3, column=0)
entry_name = tk.Entry(root)
entry_name.grid(row=3, column=1)

# Mobile Number
tk.Label(root, text="Mobile Number:").grid(row=4, column=0)
entry_mobile = tk.Entry(root)
entry_mobile.grid(row=4, column=1)

# Email ID
tk.Label(root, text="Email ID:").grid(row=5, column=0)
entry_email = tk.Entry(root)
entry_email.grid(row=5, column=1)

# Home Address
tk.Label(root, text="Home Address:").grid(row=6, column=0)
entry_address = tk.Entry(root)
entry_address.grid(row=6, column=1)

# Gender
tk.Label(root, text="Gender:").grid(row=7, column=0)
var_gender = tk.StringVar()
gender_choices = ttk.Combobox(root, textvariable=var_gender, values=["Male", "Female"])
gender_choices.grid(row=7, column=1)

# Course Enrolled with the styling of the choices
tk.Label(root, text="Course Enrolled:").grid(row=8, column=0)
var_course = tk.StringVar()
course_choices = ttk.Radiobutton(root, text="Bsc CC", variable=var_course, value="Bsc CC")
course_choices.grid(row=8, column=1, sticky="w")
course_choices = ttk.Radiobutton(root, text="Bsc Cy", variable=var_course, value="Bsc Cy")
course_choices.grid(row=9, column=1, sticky="w")
course_choices = ttk.Radiobutton(root, text="Bsc Psy", variable=var_course, value="Bsc Psy")
course_choices.grid(row=10, column=1, sticky="w")
course_choices = ttk.Radiobutton(root, text="BA & BM", variable=var_course, value="BA & BM")
course_choices.grid(row=11, column=1, sticky="w")

# Languages Known and styling the choices
tk.Label(root, text="Languages Known:").grid(row=12, column=0)
var_languages = tk.StringVar()
language_choices = ttk.Checkbutton(root, text="English", variable=var_languages, onvalue="English", offvalue="")
language_choices.grid(row=12, column=1, sticky="w")
language_choices = ttk.Checkbutton(root, text="Tagalog", variable=var_languages, onvalue="Tagalog", offvalue="")
language_choices.grid(row=13, column=1, sticky="w")
language_choices = ttk.Checkbutton(root, text="Urdu/Hindi", variable=var_languages, onvalue="Urdu/Hindi", offvalue="")
language_choices.grid(row=14, column=1, sticky="w")

# label for Your Communication Skills
tk.Label(root, text="Rate Your Communication Skills:").grid(row=15, column=0)
scale_communication = tk.Scale(root, from_=0, to=10, orient=tk.HORIZONTAL, showvalue=0, length=200)
scale_communication.grid(row=15, column=1)

# Setting date entry labels to grey
for child in root.winfo_children():
    if isinstance(child, tk.Label) and child.cget("text").endswith(":"):
        child.config(fg="grey")

# Clearing and Submitting buttons
clear_button = tk.Button(root, text="Clear", command=clear_form)
clear_button.grid(row=17, column=0, pady=10)

submit_button = tk.Button(root, text="Submit", command=submit_form)
submit_button.grid(row=17, column=1, pady=10)

# Running the mainloop
root.mainloop()