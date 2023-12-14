# Chapter 4 Bonus Exercise: Petrol Price

# Importing tkinter library
from tkinter import *

# Defining a function to analyze petrol data
def analyze_petrol_data():
    try:
        # The File path for petrol data
        petrol_data_file_path = 'petrolPrice.txt'

        # Initializing the variables for calculations
        total_liters = 0
        total_cost = 0
        under_3_5_liters = 0

        # Reading the data from the file and processing each line
        with open(petrol_data_file_path, 'r') as file:
            # Skipping the header line
            next(file)

            for line in file:
                # Splitting the line into columns
                columns = line.strip().split('\t')

                # Extracting liters and cost from the columns
                liters, cost = float(columns[0]), float(columns[1])

                # Adding to totals
                total_liters += liters
                total_cost += cost

                # Checking if the cost per liter is under 3.5 AED
                if liters > 0 and cost / liters < 3.5:
                    under_3_5_liters += liters

        # Calculating average cost per liter
        if total_liters > 0:
            average_cost_per_liter = total_cost / total_liters
        else:
            average_cost_per_liter = 0

        # Displaying statistics
        result_text = f"Statistics:\nTotal Liters: {total_liters}\nTotal Cost: {total_cost}\n"
        result_text += f"Average Cost per Liter: {average_cost_per_liter:.2f}\n"
        result_text += f"Liters bought at under 3.5 AED per liter: {under_3_5_liters}"
        result_label.config(text=result_text)

    except FileNotFoundError:
        result_label.config(text="File not found. Please make sure the file exists.")


# Creating the main window
root = Tk()

# Creating a title for the page
root.title("Petrol Data Analyzer")

# Setting the window size
root.geometry('300x200')

# Using Label for displaying the result with updated design
result_label = Label(
    root,
    text="",
    font=("Arial", 12),
    bg="#f0f0f0",  # Background color
    pady=10,
    padx=20,
    borderwidth=2,
    relief="groove"
)
result_label.pack(pady=10)

# The Button for analyzing the petrol data with a blue color
analyze_button = Button(
    root,
    text="Analyze Petrol Data",
    command=analyze_petrol_data,
    bg="#007acc",  # Blue color
    fg="white",
    font=("Arial", 12),
    pady=10
)
analyze_button.pack(pady=10)

# Running the main event loop
root.mainloop()