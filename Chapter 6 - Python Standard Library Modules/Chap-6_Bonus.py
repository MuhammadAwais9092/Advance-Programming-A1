# Chapter 6 Bonus Exercise: Bar graph

# Importing tkinter library
import tkinter as tk

# Using class function for bar graph and setting the required parameters
class Horizontal_BarGraph(tk.Tk):
    def __init__(self, brands, values):
        super().__init__()
        self.title("Horizontal Bar Graph: Most Valuable Brands Worldwide in 2023")
        self.geometry("800x600")
        self.brands = brands
        self.values = values
        self.drawing_horizontal_bar_graph()

# Defining function for making the graph horizontal
    def drawing_horizontal_bar_graph(self):
        canvas = tk.Canvas(self, width=700, height=600)
        canvas.pack(pady=20)

        # Calculating the maximum value to scale the bar widths
        max_value = max(self.values)
        scale_factor = 650 / max_value

        # Drawing bars for each brand using for loop
        for a in range(len(self.brands)):
            bar_width = self.values[a] * scale_factor
            canvas.create_rectangle(
                50, 50 + a * 40,
                50 + bar_width, 90 + a * 40,
                fill="lightblue",
                outline="black"
            )
            # Displaying brand names in such a way that they are on the left of the bars
            canvas.create_text(
                60, 75 + a * 40,
                text=self.brands[a],
                anchor=tk.W  # Anchor to the west (left) for better visibility
            )

        # Displaying the title
        canvas.create_text(
            350, 20,
            text="Most Valuable Brands Worldwide in 2023",
            font=("Helvetica", 14, "bold")
        )

        # Displaying the horizontal label
        canvas.create_text(
            350, 550,
            text="Value (in billion U.S. dollars)",
            font=("Helvetica", 10, "italic")
        )

# Given Data of brands and values
brands = ["Amazon", "Apple", "Google", "Microsoft", "Walmart", "Samsung Group", "ICBC", "Verizon", "Tesla", "TikTok/Douyin"]
values = [299.28, 297.51, 281.38, 191.57, 113.78, 99.66, 69.55, 67.44, 66.21, 65.67]

# Instantiate the HorizontalBarGraph class with the provided data
app = Horizontal_BarGraph(brands, values)
app.mainloop()