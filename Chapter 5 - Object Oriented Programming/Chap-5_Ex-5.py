# Chapter 5 Exercise 5: Playing around in class

# Importing the tkinter library
import tkinter as tk

# Making a class called animal
class Animal:
    def __init__(self, animal_type, name, color, age, weight, noise):
        # Initializing the Animal object with specified attributes
        self.animal_type = animal_type
        self.name = name
        self.color = color
        self.age = age
        self.weight = weight
        self.noise = noise

# Defining a function for making the animal say hello
    def sayHello(self):
        # Codes to make the animal say hello
        return f"{self.name} says hello!"

    # Defining a function for to make the animal make its noise
    def makeNoise(self):
        # Codes to make the animal produce its characteristic noise
        return f"{self.name} makes the noise: {self.noise}"

    # Defining a function for adding details to the animal
    def animalDetails(self):
        # Codes to get a string representation of all details of the animal
        details = (
            f"Type: {self.animal_type}\n"
            f"Name: {self.name}\n"
            f"Color: {self.color}\n"
            f"Age: {self.age}\n"
            f"Weight: {self.weight} kg\n"
            f"Noise: {self.noise}"
        )
        return details

# Making a class for animal GUI
class AnimalGUI(tk.Tk):
    def __init__(self):
        # Initializing the AnimalGUI window and styling it
        super().__init__()
        self.title("Animal Information")
        self.geometry("400x300")
        self.create_animal_objects()

    # Defining a function for animal objects
    def create_animal_objects(self):
        # Creating instances of the Animal class
        dog = Animal("Dog", "Buddy", "Brown", 3, 10, "Woof")
        cow = Animal("Cow", "MooMoo", "Black and White", 5, 500, "Moo")

        # Creating labels to display information for animal dog
        dog_label = tk.Label(self, text=dog.animalDetails())
        dog_label.pack()
        # Creating labels to display information for animal cow
        cow_label = tk.Label(self, text=cow.animalDetails())
        cow_label.pack()

# Running the AnimalGUI class
app = AnimalGUI()
app.mainloop()
