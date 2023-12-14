# Chapter 5 Bonus Exercise: Playing around in class

# Importing the tkinter library
import tkinter as tk

# Using class as animal
class Animal:
    def __init__(self, animal_type, name, color, age, weight, noise):
        # Initializing the Animal object with specified attributes
        self.animal_type = animal_type
        self.name = name
        self.color = color
        self.age = age
        self.weight = weight
        self.noise = noise

    def sayHello(self):
        # Method to make the animal say hello
        return f"{self.name} says hello!"

    def makeNoise(self):
        # Method to make the animal produce its characteristic noise
        return f"{self.name} makes the noise: {self.noise}"

    def animalDetails(self):
        # Method to get a string representation of all details of the animal
        details = (
            f"Type: {self.animal_type}\n"
            f"Name: {self.name}\n"
            f"Color: {self.color}\n"
            f"Age: {self.age}\n"
            f"Weight: {self.weight} kg\n"
            f"Noise: {self.noise}"
        )
        return details # Returning details

# Using class as animalGUI
class AnimalGUI(tk.Tk):
    def __init__(self):
        # Initializing the AnimalGUI window
        super().__init__()
        self.title("Animal Information")
        self.geometry("400x300")
        self.creating_animal_objects()

# Defining function to create animal objects
    def creating_animal_objects(self):
        # Getting user input for creating instances of the Animal class
        animal_type = input("Enter animal type: ")
        name = input("Enter name: ")
        color = input("Enter color: ")
        age = int(input("Enter age: "))
        weight = float(input("Enter weight in kg: "))
        noise = input("Enter characteristic noise: ")

        # Creating an instance of the Animal class with user input
        user_animal = Animal(animal_type, name, color, age, weight, noise)

        # Creating a label to display information for the user's animal
        user_animal_label = tk.Label(self, text=user_animal.animalDetails())
        user_animal_label.pack()

# Instantiate the AnimalGUI class
app = AnimalGUI()
app.mainloop()
