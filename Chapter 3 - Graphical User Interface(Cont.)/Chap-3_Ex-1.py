# Chapter 3 Exercise 1: Greeting App

# Importing tk inter library and modules
import tkinter as tk
from tkinter import ttk

# making a class for Greetings
class GreetingApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Greeting App")

        # Setting the background colors
        input_frame_color = "#90C3D4"  # Light blue
        display_frame_color = "#FFD700"  # Gold

        # Creating the InputFrame
        self.input_frame = tk.Frame(root, bg=input_frame_color, padx=20, pady=20)
        self.input_frame.grid(row=0, column=0)

        # Titling the label in blue
        title_label = tk.Label(self.input_frame, text="Personalized Greeting", font=("Helvetica", 14, "bold"), fg="blue", bg=input_frame_color)
        title_label.grid(row=0, column=0, columnspan=2, pady=(0, 10))

        # Making an Entry field for the user's name
        self.name_entry = tk.Entry(self.input_frame)
        self.name_entry.grid(row=1, column=0, columnspan=2, pady=(0, 10))

        # Making a dropdown menu for selecting color
        color_label = tk.Label(self.input_frame, text="Select Color:", bg=input_frame_color)
        color_label.grid(row=2, column=0, sticky="e")
        # And styling it
        self.color_var = tk.StringVar()
        self.color_dropdown = ttk.Combobox(self.input_frame, textvariable=self.color_var, values=["Red", "Green", "Blue"])
        self.color_dropdown.grid(row=2, column=1, pady=(0, 10))

        # Updating the Greeting button
        update_button = tk.Button(self.input_frame, text="Update Greeting", command=self.update_greeting)
        update_button.grid(row=3, column=0, columnspan=2, pady=(0, 10))

        # Creating the DisplayFrame
        self.display_frame = tk.Frame(root, bg=display_frame_color, padx=20, pady=20)
        self.display_frame.grid(row=0, column=1)

        # Labeling to display personalized greeting
        self.greeting_label = tk.Label(self.display_frame, text="", font=("Helvetica", 14, "bold"), bg=display_frame_color)
        self.greeting_label.pack()

# Defining a function for the updated greeting
    def update_greeting(self):
        # Getting the user's name and selected color
        name = self.name_entry.get()
        selected_color = self.color_var.get()

        if name and selected_color:
            # Creating a personalized greeting
            greeting_text = f"Hello, {name}!"
            self.greeting_label.config(text=greeting_text, fg=selected_color)

# Making sure it runs properly
if __name__ == "__main__":
    root = tk.Tk()
    app = GreetingApp(root)
    root.mainloop()