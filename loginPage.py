
import tkinter as tk
from tkinter import messagebox
from login_subsystem import AuthService
from FoundationOfAlgebra import PracticeAI
import sqlite3
import random

auth_service = AuthService()

def fetch_all_topics():
    conn = sqlite3.connect("learning_platform.db")
    cursor = conn.cursor()
    cursor.execute("SELECT id, name FROM Topic")
    topics = cursor.fetchall()
    conn.close()
    return topics

def fetch_random_topic():
    conn = sqlite3.connect("learning_platform.db")
    cursor = conn.cursor()
    cursor.execute("SELECT id, name FROM Topic ORDER BY RANDOM() LIMIT 1")
    topic = cursor.fetchone()
    conn.close()
    return topic

def fetch_goals_for_topic(topic_name):
    conn = sqlite3.connect("learning_platform.db")
    cursor = conn.cursor()
    cursor.execute("SELECT id FROM Topic WHERE name = ?", (topic_name,))
    topic = cursor.fetchone()
    if not topic:
        conn.close()
        return []
    topic_id = topic[0]
    cursor.execute("SELECT title, description FROM Goal WHERE topic_id = ? ORDER BY goal_order ASC", (topic_id,))
    goals = cursor.fetchall()
    conn.close()
    return goals

def launch_main_app(username):
    main_app = tk.Tk()
    main_app.title("Main Dashboard")
    main_app.geometry("800x600")

    welcome_label = tk.Label(main_app, text=f"Welcome, {username}!", font=("Helvetica", 16))
    welcome_label.pack(pady=20)

    def handle_student_pick():
        for widget in main_app.winfo_children():
            widget.destroy()

        tk.Label(main_app, text="Choose a Topic:", font=("Helvetica", 14)).pack(pady=10)
        topics = fetch_all_topics()
        if not topics:
            messagebox.showinfo("No Topics", "No topics found in the database.")
            return

        for topic_id, topic_name in topics:
            tk.Button(main_app, text=topic_name, font=("Helvetica", 12), width=30,
                      command=lambda t=topic_name: show_goals_for_topic(main_app, username, t)).pack(pady=5)

    def handle_computer_pick():
        topic = fetch_random_topic()
        if topic:
            topic_id, topic_name = topic
            show_goals_for_topic(main_app, username, topic_name)
        else:
            messagebox.showinfo("No Topics", "No topics available to choose from.")

    # Buttons
    student_pick_button = tk.Button(main_app, text="Student Pick", font=("Helvetica", 14), width=20, height=2,
                                    command=handle_student_pick)
    student_pick_button.pack(pady=10)

    computer_pick_button = tk.Button(main_app, text="Computer Pick", font=("Helvetica", 14), width=20, height=2,
                                     command=handle_computer_pick)
    computer_pick_button.pack(pady=10)

    main_app.mainloop()

def show_goals_for_topic(window, username, topic_name):
    if topic_name == "Foundations for Algebra":
        window.destroy()
        PracticeAI().run()
        return
    for widget in window.winfo_children():
        widget.destroy()

    goals = fetch_goals_for_topic(topic_name)
    if not goals:
        messagebox.showinfo("No Goals", f"No goals found for {topic_name}.")
        return

    goal_index = [0]

    title_label = tk.Label(window, text="", font=("Helvetica", 14, "bold"))
    title_label.pack(pady=10)

    desc_label = tk.Label(window, text="", font=("Helvetica", 12), wraplength=700, justify="left")
    desc_label.pack(pady=10)

    def update_goal():
        title, desc = goals[goal_index[0]]
        title_label.config(text=f"Goal: {title}")
        desc_label.config(text=desc)

    def next_goal():
        if goal_index[0] + 1 < len(goals):
            goal_index[0] += 1
            update_goal()
        else:
            messagebox.showinfo("Done", "You’ve reached the last goal.")

    def go_back():
        window.destroy()
        launch_main_app(username)

    update_goal()

    tk.Button(window, text="Next", command=next_goal).pack(pady=10)
    tk.Button(window, text="Back to Topics", command=go_back).pack(pady=5)

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

    # First name
    tk.Label(reg_window, text="First Name:").grid(row=2, column=0, padx=10, pady=5)
    new_first_name_entry = tk.Entry(reg_window)
    new_first_name_entry.grid(row=2, column=1)

    # Last name
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

# Login window
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
