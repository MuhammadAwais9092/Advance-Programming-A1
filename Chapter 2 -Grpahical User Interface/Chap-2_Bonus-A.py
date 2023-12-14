# Chapter 2 Bonus A: Temperature Converter

# Importing tkinter library
import tkinter as tk

# Defining function for converting temperature
def temperature_converter():
    try:
        # Trying to convert input temperature to a float and getting the user selected temperature unit
        temp = float(entered_temperature.get())  # Getting temperature from the entry widget and convert it to a float
        temp_type = temperature_var.get()  # Getting selected temperature unit

        # Checking the selected unit and perform the corresponding temperature conversion
        if temp_type == "Celsius":
            # Converting Celsius to Fahrenheit and setting the result string with 2 decimal places
            result.set(f"{temp} °C is {((temp * 9 / 5) + 32):.2f} °F")
        elif temp_type == "Fahrenheit":
            # Converting Fahrenheit to Celsius and setting the result string with 2 decimal places
            result.set(f"{temp} °F is {((temp - 32) * 5 / 9):.2f} °C")

    except ValueError:
        # Handling the case where the input cannot be converted to a float and output "invalid input"
        result.set("Invalid Input")

# Creating the main window
root = tk.Tk()
root.title("Temperature Converter")

# Variables for user input, unit, and result
entered_temperature = tk.Entry(root, width=20)
temperature_var = tk.StringVar(value="Celsius")
result = tk.StringVar()

# Styling and writing Widgets
tk.OptionMenu(root, temperature_var, "Celsius", "Fahrenheit").grid(row=1, column=0, columnspan=2, padx=10, pady=10)
tk.Button(root, text="Convert", command=temperature_converter).grid(row=2, column=0, columnspan=2, padx=10, pady=10)
tk.Label(root, textvariable=result).grid(row=3, column=0, columnspan=2, padx=10, pady=10)

# Arrange entry widget
entered_temperature.grid(row=0, column=0, padx=10, pady=10)

# Running the main loop
root.mainloop()