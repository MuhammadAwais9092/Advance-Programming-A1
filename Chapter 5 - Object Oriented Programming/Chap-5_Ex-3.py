# Chapter 5 Exercise 3: Employee Class

# Importing the tkinter library
import tkinter as tk

# Making a class called employee
class Employee:
    def __init__(self):
        # Initializing the attributes for employee
        self.name = ""
        self.position = ""
        self.salary = 0.0
        self.id = ""

# Defining a function for data
    def setData(self, name, position, salary, emp_id):
        # Setting data for the employee
        self.name = name
        self.position = position
        self.salary = salary
        self.id = emp_id

# Defining a function for the the set fata of the employee
    def getData(self):
        # Returning formatted employee data as a string
        return f"{self.name}\t{self.position}\t{self.salary}\t{self.id}"

# Making a class for employee GUI and styling it as well
class EmployeeGUI(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Employee Details")
        self.geometry("400x300")
        self.employees = []

        self.create_employee_data_fields()

        # Creating a button to add employee
        add_button = tk.Button(self, text="Add Employee", command=self.add_employee)
        add_button.pack()

        # Creating a button to display employees
        display_button = tk.Button(self, text="Display Employees", command=self.display_employees)
        display_button.pack()

# Defining function for employees work filed
    def create_employee_data_fields(self):
        # Creating labels and entry fields for employee data

        # Label and entry for employee name
        self.name_label = tk.Label(self, text="Name")
        self.name_label.pack()
        self.name_entry = tk.Entry(self)
        self.name_entry.pack()

        # Label and entry for employee position
        self.position_label = tk.Label(self, text="Position")
        self.position_label.pack()
        self.position_entry = tk.Entry(self)
        self.position_entry.pack()

        # Label and entry for employee salary
        self.salary_label = tk.Label(self, text="Salary")
        self.salary_label.pack()
        self.salary_entry = tk.Entry(self)
        self.salary_entry.pack()

        # Label and entry for employee ID
        self.id_label = tk.Label(self, text="ID")
        self.id_label.pack()
        self.id_entry = tk.Entry(self)
        self.id_entry.pack()

# Defining function for adding employee data to the list
    def add_employee(self):
        # Adding employee to the list

        # Checking if the maximum number of employees (5) has been reached
        if len(self.employees) >= 5:
            print("Maximum number of employees reached: 5 employees.")
        else:
            # Retrieving employee information from entry fields
            name = self.name_entry.get()
            position = self.position_entry.get()
            salary = float(self.salary_entry.get())
            emp_id = self.id_entry.get()

            # Creating a new Employee instance and set its data
            employee = Employee()
            employee.setData(name, position, salary, emp_id)

            # Adding the employee to the list of employees
            self.employees.append(employee)

            # Printing a message indicating the employee has been added
            print("Amount of Employee Added:")
            print(employee.getData())

# Defining a function for displaying employee details
    def display_employees(self):
        # Displaying employee details

        # Checking if there are no employees in the list
        if not self.employees:
            print("No employees to display.")
        else:
            # Printing headers for employee details
            print("Employee Details:")
            print("Name\tPosition\tSalary\tID")

            # Iterating through the list of employees and print their details
            for employee in self.employees:
                print(employee.getData())

# Running the EmployeeGUI class
app = EmployeeGUI()
app.mainloop()
