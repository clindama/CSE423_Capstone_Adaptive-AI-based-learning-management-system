import tkinter as tk
from tkinter import messagebox
from login_subsystem import AuthService

auth_service = AuthService()

#MainApp NOTHING HERE YET
def launch_main_app(username):
    main_app = tk.Tk()
    main_app.title("Main Dashboard")
    main_app.geometry("1920x1080")
    main_app.mainloop()

#Login login using login_subsystem
def handle_login():
    username = username_entry.get()
    password = password_entry.get()
    if auth_service.authenticate(username, password):
        messagebox.showinfo("Login Success", f"Welcome, {username}!")
        root.destroy()
        launch_main_app(username)
    else:
        messagebox.showerror("Login Failed", "Invalid username or password.")

#Regristration popup
def show_register_window():
    reg_window = tk.Toplevel(root)
    reg_window.title("Register New Account")
    reg_window.geometry("250x225")

    # Username
    tk.Label(reg_window, text="Username:").grid(row=0, column=0, padx=10, pady=5)
    new_username_entry = tk.Entry(reg_window)
    new_username_entry.grid(row=0, column=1)

    # Password
    tk.Label(reg_window, text="Password:").grid(row=1, column=0, padx=10, pady=5)
    new_password_entry = tk.Entry(reg_window, show="*")
    new_password_entry.grid(row=1, column=1)

    #First name
    tk.Label(reg_window, text="First Name:").grid(row=2, column=0, padx=10, pady=5)
    new_first_name_entry = tk.Entry(reg_window)
    new_first_name_entry.grid(row=2, column=1)

    # Last Name
    tk.Label(reg_window, text="Last Name:").grid(row=3, column=0, padx=10, pady=5)
    new_last_name_entry = tk.Entry(reg_window)
    new_last_name_entry.grid(row=3, column=1)

    # Email
    tk.Label(reg_window, text="Email:").grid(row=4, column=0, padx=10, pady=5)
    new_email_entry = tk.Entry(reg_window)
    new_email_entry.grid(row=4, column=1)

    def register_user():
        username = new_username_entry.get()
        password = new_password_entry.get()
        first_name = new_first_name_entry.get()
        last_name = new_last_name_entry.get()
        email = new_email_entry.get()

        if auth_service.register(username, password, email, first_name, last_name):
            messagebox.showinfo("Success", "Registration successful!")
            reg_window.destroy()
        else:
            messagebox.showerror("Error", "Registration failed. Username may already exist.")

    tk.Button(reg_window, text="Register", command=register_user).grid(row=5, column=1, pady=20)


#Login window
root = tk.Tk()
root.title("Login Page")
root.geometry("275x175")

tk.Label(root, text="Username:").grid(row=0, column=0, padx=10, pady=10)
username_entry = tk.Entry(root)
username_entry.grid(row=0, column=1)

tk.Label(root, text="Password:").grid(row=1, column=0, padx=10, pady=10)
password_entry = tk.Entry(root, show="*")
password_entry.grid(row=1, column=1)

tk.Button(root, text="Login", command=handle_login).grid(row=2, column=1, pady=10)
tk.Button(root, text="Register", command=show_register_window).grid(row=3, column=1)

root.mainloop()
