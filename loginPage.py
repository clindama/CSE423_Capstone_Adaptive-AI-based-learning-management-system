import tkinter as tk
from tkinter import messagebox
from tkinter import ttk
from login_subsystem import AuthService
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

def fetch_topic_progress(username):
    conn = sqlite3.connect("learning_platform.db")
    cursor = conn.cursor()
    cursor.execute("SELECT id FROM User WHERE username = ?", (username,))
    user_id = cursor.fetchone()[0]

    cursor.execute("""
        SELECT Topic.name, TopicProgress.progress
        FROM Topic
        LEFT JOIN TopicProgress ON Topic.id = TopicProgress.topic_id
        AND TopicProgress.user_id = ?
    """, (user_id,))
    progress_data = cursor.fetchall()
    conn.close()
    return progress_data

def mark_topic_complete(username, topic_name):
    conn = sqlite3.connect("learning_platform.db")
    cursor = conn.cursor()

    cursor.execute("SELECT id FROM User WHERE username = ?", (username,))
    user_id = cursor.fetchone()[0]

    cursor.execute("SELECT id FROM Topic WHERE name = ?", (topic_name,))
    topic_id = cursor.fetchone()[0]

    cursor.execute("""
        INSERT INTO TopicProgress (user_id, topic_id, progress)
        VALUES (?, ?, 100)
        ON CONFLICT(user_id, topic_id) DO UPDATE SET progress = 100
    """, (user_id, topic_id))

    conn.commit()
    conn.close()

def launch_main_app(username):
    main_app = tk.Tk()
    main_app.title("Main Dashboard")
    main_app.geometry("800x600")

    welcome_label = tk.Label(main_app, text=f"Welcome, {username}!", font=("Helvetica", 16))
    welcome_label.pack(pady=20)

    # Show Topic Progress
    progress_frame = tk.Frame(main_app)
    progress_frame.pack(pady=10)

    tk.Label(progress_frame, text="Your Topic Progress:", font=("Helvetica", 12, "underline")).pack()

    progress_data = fetch_topic_progress(username)
    for topic, progress in progress_data:
        progress = progress if progress is not None else 0
        tk.Label(progress_frame, text=f"{topic}: {progress}%", font=("Helvetica", 10)).pack(anchor="w", padx=10)

    def show_completed_topics():
        completed = [topic for topic, progress in progress_data if progress == 100]
        if completed:
            messagebox.showinfo("Completed Topics", "\n".join(completed))
        else:
            messagebox.showinfo("Completed Topics", "No topics completed yet.")

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
    tk.Button(main_app, text="Student Pick", font=("Helvetica", 14), width=20, height=2,
              command=handle_student_pick).pack(pady=10)

    tk.Button(main_app, text="Computer Pick", font=("Helvetica", 14), width=20, height=2,
              command=handle_computer_pick).pack(pady=10)

    tk.Button(main_app, text="View Completed Topics", font=("Helvetica", 12),
              command=show_completed_topics).pack(pady=5)

    main_app.mainloop()

def show_goals_for_topic(window, username, topic_name):
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
            mark_topic_complete(username, topic_name)
            messagebox.showinfo("Done", f"You’ve reached the last goal for '{topic_name}'. Topic marked as complete!")
            go_back()

    def go_back():
        window.destroy()
        launch_main_app(username)

    update_goal()

    tk.Button(window, text="Next", command=next_goal).pack(pady=10)
    tk.Button(window, text="Back to Topics", command=go_back).pack(pady=5)

# Login logic using login_subsystem
def handle_login():
    username = username_entry.get()
    password = password_entry.get()
    if auth_service.authenticate(username, password):
        messagebox.showinfo("Login Success", f"Welcome, {username}!")
        root.destroy()
        launch_main_app(username)
    else:
        messagebox.showerror("Login Failed", "Invalid username or password.")

# Registration popup
def show_register_window():
    reg_window = tk.Toplevel(root)
    reg_window.title("Register New Account")
    reg_window.geometry("250x225")

    tk.Label(reg_window, text="Username:").grid(row=0, column=0, padx=10, pady=5)
    new_username_entry = tk.Entry(reg_window)
    new_username_entry.grid(row=0, column=1)

    tk.Label(reg_window, text="Password:").grid(row=1, column=0, padx=10, pady=5)
    new_password_entry = tk.Entry(reg_window, show="*")
    new_password_entry.grid(row=1, column=1)

    tk.Label(reg_window, text="First Name:").grid(row=2, column=0, padx=10, pady=5)
    new_first_name_entry = tk.Entry(reg_window)
    new_first_name_entry.grid(row=2, column=1)

    tk.Label(reg_window, text="Last Name:").grid(row=3, column=0, padx=10, pady=5)
    new_last_name_entry = tk.Entry(reg_window)
    new_last_name_entry.grid(row=3, column=1)

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
