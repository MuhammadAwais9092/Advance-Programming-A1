# Chapter 5 Exercise 2: Student Class

# Importing the tkinter library
import tkinter as tk

# Making a class called students
class Students:
    def __init__(self, name, mark1, mark2, mark3):
        # Making a constructor to initialize student attributes
        self.name = name
        self.mark1 = mark1
        self.mark2 = mark2
        self.mark3 = mark3

# Defining function to calculate the grade
    def calc_Grade(self):
        # Codes for calculating the average grade
        return (self.mark1 + self.mark2 + self.mark3) / 3
# Defining function for displaying the information
    def display(self):
        # Codes for displaying student information
        average = self.calc_Grade()
        return f"Student Name: {self.name}\nAverage Grade: {average:.2f}"

# Making a clas for students GUI
class StudentsGUI(tk.Tk):
    def __init__(self):
        # Using GUI constructor for styling
        super().__init__()
        self.title("Students Information")
        self.geometry("300x200")
        self.create_student_objects()

# Defining a function for creating student objects
    def create_student_objects(self):
        # Method to create GUI components
        self.label = tk.Label(self, text="The Information about the student will be displayed here.")
        self.label.pack()

       # Using input to store student information
        input_button = tk.Button(self, text="Enter Student Information", command=self.get_student_info)
        input_button.pack()

    def get_student_info(self):
        # Codes to get student information and display it
        try:
            name = input("Enter Student Name: ")
            mark1 = int(input("Enter Mark 1: "))
            mark2 = int(input("Enter Mark 2: "))
            mark3 = int(input("Enter Mark 3: "))

            student = Students(name, mark1, mark2, mark3)

            self.label.config(text=student.display())
        except ValueError:
            print("Invalid input for marks. Please enter numerical values.")

# Running the StudentsGUI class
app = StudentsGUI()
app.mainloop()
