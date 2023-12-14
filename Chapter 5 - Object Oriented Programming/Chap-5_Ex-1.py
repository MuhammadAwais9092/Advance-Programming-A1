# Chapter 5 Exercise 1: Woof Woof

# Importing tkinter library
import tkinter as tk

# Making a class called Dog
class Dog:
    def __init__(self, name, age):
        # Initializing the Dog object with name and age attributes
        self.name = name
        self.age = age

    def woof(self):
        # Method to make the dog say woof
        return f"{self.name} says Woof!"

# Creating two dog objects
dog1 = Dog("American Pitbull", 6)
dog2 = Dog("Bull Dog", 2)

# Determining the oldest dog
oldest_dog = dog1 if dog1.age > dog2.age else dog2

# Making class for Tkinter GUI
class DogGUI(tk.Tk):
    def __init__(self):
        # Initializing the DogGUI window
        super().__init__()
        self.title("Dog Information")
        self.geometry("300x200")
        self.display_dog_info()

    def display_dog_info(self):
        # Displaying the information about each dog and the oldest dog
        label1 = tk.Label(self, text=f"Dog 1: {dog1.name}, {dog1.age} years old")
        label1.pack()

        label2 = tk.Label(self, text=f"Dog 2: {dog2.name}, {dog2.age} years old")
        label2.pack()

        # Displaying the information about the dog that is oldest
        oldest_dog_label = tk.Label(self, text=f"The Dog that is the oldest: {oldest_dog.name}")
        oldest_dog_label.pack()

        # Button for making the oldest dog woof
        woof_button = tk.Button(self, text="Make the oldest dog woof", command=self.woof)
        woof_button.pack()

# Defining function for woof
    def woof(self):
        # Codee to make the oldest dog woof
        result = oldest_dog.woof()
        woof_label = tk.Label(self, text=result)
        woof_label.pack()

# Instantiate the DogGUI class
app = DogGUI()
app.mainloop()
