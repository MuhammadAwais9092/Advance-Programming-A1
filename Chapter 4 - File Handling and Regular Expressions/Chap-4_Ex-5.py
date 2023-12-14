# Chapter 4 Exercise 5: Password Check

# Importing tkinter library and its modules
import tkinter as tk

# Importing the 'messagebox' module from tkinter for displaying message boxes
from tkinter import messagebox

# Importing the 're' module for regular expressions
import re

# Making a class named 'PasswordValidatorApp'
class PasswordValidatorApp:
    # Using Constructor method, and initializing the class instance
    def __init__(self):
        # Initializing the variable 'attempts_left' to 5
        self.attempts_left = 5

        # Creating the main tkinter window
        self.root = tk.Tk()

        # Setting the title of the window to "Password Validator"
        self.root.title("Password Validator")

        # Setting the initial dimensions of the window to 400x250 pixels
        self.root.geometry("400x250")

        # Calling the 'create_widgets' method to create GUI elements
        self.create_widgets()

    # Defining function for creating GUI elements
    def create_widgets(self):
        # Creating a label with the text "Enter Password:" and pack it with some vertical padding
        tk.Label(self.root, text="Enter Password:").pack(pady=5)

        # Creating an entry widget for password input and setting it to show '*' for each character
        self.password_entry = tk.Entry(self.root, show="*")
        self.password_entry.pack(pady=5)

        # Creating a label with a password hint and pack it with some vertical padding
        tk.Label(self.root, text="Password Hint: one (a, 1, A, $) and should have 6-12 characters.").pack(pady=10)

        # Creating a button for validating the password with a command to call 'validate_password'
        validate_button = tk.Button(self.root, text="Validate Password", command=self.validate_password)
        validate_button.pack(pady=10)

    # Defining a function to validate the entered password
    def validate_password(self):
        # Getting the entered password from the entry widget
        password = self.password_entry.get()

        # Checking if the password is valid using the 'is_valid_password' method
        if self.is_valid_password(password):
            # Showing an information message box if the password is valid
            messagebox.showinfo("Password Valid", "Password is valid!")

            # Closing the application window if the password is valid
            self.root.destroy()
        else:
            # Decreasing the 'attempts_left' variable
            self.attempts_left -= 1

            # Checking if there are any attempts left
            if self.attempts_left > 0:
                # Showing a warning message box with the number of attempts left
                messagebox.showwarning("Invalid Password", f"Invalid password! {self.attempts_left} attempts left.")
            else:
                # Showing an error message box and destroy the application window if attempts are exhausted
                messagebox.showerror("Alert!", "Authorities have been alerted! Too many failed attempts.")
                self.root.destroy()

    # Defining a function to check if the password meets the specified criteria
    def is_valid_password(self, password):
        # The Password criteria using "regular expressions"
        if (
            re.search("[a-z]", password)
            and re.search("[0-9]", password)
            and re.search("[A-Z]", password)
            and re.search("[$#@]", password)
            and 6 <= len(password) <= 12
        ):
            return True
        else:
            return False

    # Defining a function to start the main event loop of the tkinter window
    def run(self):
        self.root.mainloop()

# Instantiating the PasswordValidatorApp class
app = PasswordValidatorApp()

# Running the app
app.run()