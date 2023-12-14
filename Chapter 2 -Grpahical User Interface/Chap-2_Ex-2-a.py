# Chapter 2 Exercise 2a: Using pack

# using the tkinter library
from tkinter import *

# Creating the main window
root = Tk()

# Setting the title of the window
root.title("Four Labels Example")

# Creating Label 1 with style
label1 = Label(root, text="A", bg="red", width=10, bd=5, relief="groove")
label1.pack(side=TOP, fill=X, expand=1)  # Using pack to display and arrange Label 1 at the top

# Creating Label 2 with style
label2 = Label(root, text="B", bg="yellow", width=10)
label2.pack(side=BOTTOM)  # Using pack to display and arrange Label 2 at the bottom

# Creating Label 3 with style
label3 = Label(root, text="C", bg="blue", width=10)
label3.pack(side=LEFT, fill=Y, expand=1)  # Using pack to display and arrange Label 3 on the left

# Creating Label 4 with style
label4 = Label(root, text="D", bg="white", width=10)
label4.pack(side=RIGHT)  #  Using pack to display and arrange Label 4 on the right

# Starting the Tkinter window
root.mainloop()

# End marker