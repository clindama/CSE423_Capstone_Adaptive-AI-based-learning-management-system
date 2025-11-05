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
    row = cursor.fetchone()
    if not row:
        conn.close()
        return []
    user_id = row[0]

    cursor.execute("""
        SELECT Topic.name, TopicProgress.progress
        FROM Topic
        LEFT JOIN TopicProgress ON Topic.id = TopicProgress.topic_id
        AND TopicProgress.user_id = ?
        ORDER BY Topic.name ASC
    """, (user_id,))
    progress_data = cursor.fetchall()
    conn.close()
    return progress_data

# -------- Placeholder data for UI-only Practice Problems & Tests --------
def fetch_practice_progress(username):
    """
    Placeholder: return deterministic mock progress so the UI looks consistent.
    Replace this with real SELECTs when you add your practice tables.
    """
    random.seed(username)  # deterministic per user
    sets = [
        ("Practice Set A", random.choice([0, 20, 40, 60, 80, 100])),
        ("Practice Set B", random.choice([0, 25, 50, 75, 100])),
        ("Practice Set C", random.choice([10, 30, 50, 70, 90])),
        ("Practice Set D", random.choice([0, 100])),
    ]
    return sets

def fetch_test_progress(username):
    """
    Placeholder: return mock results for tests/quizzes.
    Later, drive from Test and Attempt tables (e.g., latest score, best score, status).
    """
    random.seed(username + "_tests")
    tests = [
        ("Quiz 1", random.choice(["Not started", "In progress", "Complete"]), random.choice([None, 68, 75, 84, 92])),
        ("Quiz 2", random.choice(["Not started", "Complete"]), random.choice([None, 70, 88, 95])),
        ("Unit Test", random.choice(["Not started", "In progress", "Complete"]), random.choice([None, 60, 73, 81, 90])),
    ]
    return tests
# -----------------------------------------------------------------------

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

def build_table(parent, columns, heading_map, rows, stretch_last=True, height=8):
    """
    Utility to create a styled ttk.Treeview table with a vertical scrollbar.
    columns: list of column keys
    heading_map: dict {key: heading label}
    rows: list of tuples/lists to insert
    """
    frame = ttk.Frame(parent)
    frame.pack(fill="x", padx=10, pady=6)

    tree = ttk.Treeview(frame, columns=columns, show="headings", height=height)
    vsb = ttk.Scrollbar(frame, orient="vertical", command=tree.yview)
    tree.configure(yscrollcommand=vsb.set)

    tree.grid(row=0, column=0, sticky="nsew")
    vsb.grid(row=0, column=1, sticky="ns")

    frame.columnconfigure(0, weight=1)

    # Configure columns
    for i, key in enumerate(columns):
        tree.heading(key, text=heading_map.get(key, key))
        # Make the last column stretch if requested
        width = 140 if i < len(columns) - 1 or not stretch_last else 220
        tree.column(key, width=width, anchor="w", stretch=True if (stretch_last and i == len(columns) - 1) else False)

    # Insert rows
    for r in rows:
        tree.insert("", "end", values=r)

    return tree

def launch_main_app(username):
    main_app = tk.Tk()
    main_app.title("Main Dashboard")
    main_app.geometry("800x600")

    welcome_label = tk.Label(main_app, text=f"Welcome, {username}!", font=("Helvetica", 16))
    welcome_label.pack(pady=20)

    # ----- Main action buttons (tabs) -----
    def handle_student_pick():
        for widget in main_app.winfo_children():
            widget.destroy()

        tk.Label(main_app, text="Choose a Topic:", font=("Helvetica", 14)).pack(pady=10)
        topics = fetch_all_topics()
        if not topics:
            messagebox.showinfo("No Topics", "No topics found in the database.")
            return

        for topic_id, topic_name in topics:
            tk.Button(
                main_app, text=topic_name, font=("Helvetica", 12), width=30,
                command=lambda t=topic_name: show_goals_for_topic(main_app, username, t)
            ).pack(pady=5)

        tk.Button(main_app, text="Back", command=lambda: relaunch_main_home(main_app, username)).pack(pady=20)

    def handle_computer_pick():
        topic = fetch_random_topic()
        if topic:
            topic_id, topic_name = topic
            show_goals_for_topic(main_app, username, topic_name)
        else:
            messagebox.showinfo("No Topics", "No topics available to choose from.")

    def show_progress():
        show_progress_dashboard(main_app, username)

    # Buttons that act like "tabs"
    btn_container = tk.Frame(main_app)
    btn_container.pack(pady=10)
    tk.Button(btn_container, text="Student Pick", font=("Helvetica", 14), width=20, height=2,
              command=handle_student_pick).grid(row=0, column=0, padx=8)
    tk.Button(btn_container, text="Computer Pick", font=("Helvetica", 14), width=20, height=2,
              command=handle_computer_pick).grid(row=0, column=1, padx=8)
    tk.Button(btn_container, text="Progress", font=("Helvetica", 14), width=20, height=2,
              command=show_progress).grid(row=0, column=2, padx=8)

    # (Moved progress display into the dedicated Progress view)
    main_app.mainloop()

def relaunch_main_home(window, username):
    """Reset the main dashboard after child screens."""
    window.destroy()
    launch_main_app(username)

def show_progress_dashboard(window, username):
    for widget in window.winfo_children():
        widget.destroy()

    header = tk.Label(window, text="Your Progress", font=("Helvetica", 16, "bold"))
    header.pack(pady=12)

    container = tk.Frame(window)
    container.pack(fill="both", expand=True)

    # ----- Topic Progress (REAL DATA) -----
    section1 = tk.Label(container, text="Topic Progress", font=("Helvetica", 13, "underline"))
    section1.pack(anchor="w", padx=10, pady=(8, 2))

    topic_rows = []
    progress_data = fetch_topic_progress(username)  # [(topic, progress_or_None), ...]
    for topic, progress in progress_data:
        pct = 0 if progress is None else progress
        topic_rows.append((topic, f"{pct}%"))

    build_table(
        parent=container,
        columns=["topic", "progress"],
        heading_map={"topic": "Topic", "progress": "Progress"},
        rows=topic_rows,
        stretch_last=True,
        height=8
    )

    # Completed topics button (same behavior, placed here):
    def show_completed_topics():
        completed = [topic for topic, prog in progress_data if (prog or 0) == 100]
        if completed:
            messagebox.showinfo("Completed Topics", "\n".join(completed))
        else:
            messagebox.showinfo("Completed Topics", "No topics completed yet.")

    tk.Button(container, text="View Completed Topics", command=show_completed_topics).pack(anchor="e", padx=12, pady=(0, 10))

    # ----- Practice Problems (MOCK / UI ONLY) -----
    section2 = tk.Label(container, text="Practice Problems", font=("Helvetica", 13, "underline"))
    section2.pack(anchor="w", padx=10, pady=(8, 2))

    practice_rows = []
    for name, pct in fetch_practice_progress(username):
        practice_rows.append((name, f"{pct}%"))

    build_table(
        parent=container,
        columns=["set", "progress"],
        heading_map={"set": "Problem Set", "progress": "Progress"},
        rows=practice_rows,
        stretch_last=True,
        height=6
    )

    # ----- Tests (MOCK / UI ONLY) -----
    section3 = tk.Label(container, text="Tests", font=("Helvetica", 13, "underline"))
    section3.pack(anchor="w", padx=10, pady=(8, 2))

    test_rows = []
    for name, status, score in fetch_test_progress(username):
        score_display = "-" if score is None else f"{score}%"
        test_rows.append((name, status, score_display))

    build_table(
        parent=container,
        columns=["test", "status", "score"],
        heading_map={"test": "Test", "status": "Status", "score": "Score"},
        rows=test_rows,
        stretch_last=True,
        height=6
    )

    # Back button
    tk.Button(window, text="Back to Main", command=lambda: relaunch_main_home(window, username)).pack(pady=16)

def show_goals_for_topic(window, username, topic_name):
    for widget in window.winfo_children():
        widget.destroy()

    goals = fetch_goals_for_topic(topic_name)
    if not goals:
        messagebox.showinfo("No Goals", f"No goals found for {topic_name}.")
        relaunch_main_home(window, username)
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
        relaunch_main_home(window, username)

    update_goal()

    tk.Button(window, text="Next", command=next_goal).pack(pady=10)
    tk.Button(window, text="Back to Topics", command=go_back).pack(pady=5)

# ---------------- Login logic using login_subsystem ----------------
def handle_login():
    username = username_entry.get()
    password = password_entry.get()
    if auth_service.authenticate(username, password):
        messagebox.showinfo("Login Success", f"Welcome, {username}!")
        root.destroy()
        launch_main_app(username)
    else:
        messagebox.showerror("Login Failed", "Invalid username or password.")

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

# ---------------- Login window ----------------
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
