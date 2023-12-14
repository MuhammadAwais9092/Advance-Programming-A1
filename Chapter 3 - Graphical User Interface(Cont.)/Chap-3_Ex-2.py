# Chapter 3 Exercise 2: Coffee Vending Machine

# Importing tkinter library and modules
import tkinter as tk
from tkinter import ttk, messagebox

# Making a class for the coffee machine
class Coffee_Vending_Machine:
    def __init__(self, root):
        self.root = root
        self.root.title("Coffee Vending Machine")

        # Displaying the message for options that would be given for the Coffee
        self.coffee_var = tk.StringVar()
        self.coffee_var.set("Select type of Coffee")

        # Adding the coffee options
        coffee_options = ["Espresso", "Cappuccino", "Latte", "Americano"]

        # Creating the Coffee Frame
        coffee_frame = tk.Frame(root, padx=20, pady=20)
        coffee_frame.grid(row=0, column=0)

        # Labeling and Dropdown for Coffee selection
        coffee_label_text = tk.Label(coffee_frame, text="Select Coffee:")
        coffee_label_text.grid(row=0, column=0)

        coffee_dropdown = ttk.Combobox(coffee_frame, textvariable=self.coffee_var, values=coffee_options)
        coffee_dropdown.grid(row=0, column=1)

        # Creating Options Frame
        options_frame = tk.Frame(root, padx=20, pady=20)
        options_frame.grid(row=1, column=0)

        # Checkbuttons for option of sugar
        self.sugar_var = tk.IntVar()
        sugar_check = tk.Checkbutton(options_frame, text="Sugar", variable=self.sugar_var)
        sugar_check.grid(row=0, column=0)

        # Checkbuttons for option of milk
        self.milk_var = tk.IntVar()
        milk_check = tk.Checkbutton(options_frame, text="Milk", variable=self.milk_var)
        milk_check.grid(row=0, column=1)

        # Button that is to confirm and display message
        confirm_button = tk.Button(root, text="Confirm", command=self.message_displayed)
        confirm_button.grid(row=2, column=0, pady=10)

# Defining a function for displaying the message
    def message_displayed(self):
        coffee_choice = self.coffee_var.get()
        sugar_choice = "with Sugar" if self.sugar_var.get() else "without Sugar"
        milk_choice = "with Milk" if self.milk_var.get() else "without Milk"

        message = f"You selected {coffee_choice} {sugar_choice} {milk_choice}."

        # Displaying the message using messagebox
        messagebox.showinfo("Order Summary", message)

# And making sure it runs properly
if __name__ == "__main__":
    root = tk.Tk()
    app = Coffee_Vending_Machine(root)
    root.mainloop() # With closing the mainloop