# Chapter 6 Exercise 4: Line graph

# Importing tkinter library
import tkinter as tk

# Defining function for drawing the line using canvas
def line_draw(canvas, start, end, color, width):
    # Drawing a line from start to end
    line = canvas.create_line(start[0], start[1], end[0], end[1], fill=color, width=width)

# Defining function for drawing a dotted line using canvas
def line_draw_dotted(canvas, points, color, width, dash):
    # Draw a dotted line through the specified points
    dotted_line = canvas.create_line(*points, fill=color, width=width, dash=dash)

# Defining the main function
def main():
    root = tk.Tk()
    canvas = tk.Canvas(root, width=500, height=600) # Setting the width and the height
    canvas.pack()

    # Drawing a solid line from (1, 2) to (6, 8)
    line_draw(canvas, (100, 200), (300, 400), "blue", 2)

    # Drawing a dotted line from (1, 3) to (2, 8) then to (6, 1) and finally to (8, 10)
    line_draw_dotted(canvas, [200, 300, 250, 400, 300, 100, 400, 500], "red", 4, (5, 5))

    # Running the main function
    root.mainloop()

if __name__ == "__main__":
    main()
