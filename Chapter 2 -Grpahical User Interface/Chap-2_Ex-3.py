import tkinter as tk

def login_page():
    user_name = entry_user_name.get()
    password = entry_password.get()

    # Basic authentication (replace with your actual authentication logic)
    if user_name == "Admin" and password == "awais4325":
        result_label.config(text="Login Successful", fg="green")
    else:
        result_label.config(text="Login Failed", fg="red")

root = tk.Tk()
root.title("Login Page")

# Set the initial size of the window
root.geometry("250x200")

# Adding descriptive labels above the username and password fields
label_instruction = tk.Label(root, text="Please enter your credentials:\n Username= Admin,  Password= awais4325")
label_user_name = tk.Label(root, text="Username:")
label_password = tk.Label(root, text="Password:")
entry_user_name = tk.Entry(root)
entry_password = tk.Entry(root, show="*")
login_button = tk.Button(root, text="Login", command=login_page)
result_label = tk.Label(root, text="", fg="black")

# Placing widgets in the grid
label_instruction.grid(row=0, column=0, columnspan=2, pady=5)
label_user_name.grid(row=1, column=0, padx=10, pady=5, sticky="e")
entry_user_name.grid(row=1, column=1, padx=10, pady=5)
label_password.grid(row=2, column=0, padx=10, pady=5, sticky="e")
entry_password.grid(row=2, column=1, padx=10, pady=5)
login_button.grid(row=3, column=0, columnspan=2, pady=10)
result_label.grid(row=4, column=0, columnspan=2)

# Running the mainloop
root.mainloop()
