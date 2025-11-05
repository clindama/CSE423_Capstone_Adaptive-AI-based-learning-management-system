"""
Unified Learning Management System
Main entry point for the Adaptive AI-based Learning Management System
Integrates login, progress tracking, topic selection, and AI-powered problem generation
"""

import tkinter as tk
from tkinter import messagebox, ttk, simpledialog
from login_subsystem import AuthService
import sqlite3
import random
import string
import os

# Try to import AI features (optional)
try:
    import google.genai as genai
    from google.genai import types
    AI_AVAILABLE = True
except ImportError:
    AI_AVAILABLE = False
    print("Warning: google-genai not installed. AI features will be disabled.")

# Configuration
DB_PATH = "learning_platform.db"
API_KEY = "AIzaSyCbaAhYPM6D6C1EonXwxyq49AxlGsvgjIQ"  # Replace with your actual API key

# Initialize services
auth_service = AuthService(db_path=DB_PATH)
if AI_AVAILABLE:
    client = genai.Client(api_key=API_KEY)

# Global state
current_user = None
current_user_id = None


# ==================== DATABASE HELPER FUNCTIONS ====================

def fetch_all_topics():
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()
    cursor.execute("SELECT id, name FROM Topic ORDER BY topic_order ASC")
    topics = cursor.fetchall()
    conn.close()
    return topics


def fetch_random_topic():
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()
    cursor.execute("SELECT id, name FROM Topic ORDER BY RANDOM() LIMIT 1")
    topic = cursor.fetchone()
    conn.close()
    return topic


def fetch_goals_for_topic(topic_name):
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()
    cursor.execute("SELECT id FROM Topic WHERE name = ?", (topic_name,))
    topic = cursor.fetchone()
    if not topic:
        conn.close()
        return []
    topic_id = topic[0]
    cursor.execute("SELECT id, title, description FROM Goal WHERE topic_id = ? ORDER BY goal_order ASC", (topic_id,))
    goals = cursor.fetchall()
    conn.close()
    return goals


def fetch_objectives_for_goal(goal_id):
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()
    cursor.execute("""
        SELECT id, title, description 
        FROM LearningObjective 
        WHERE goal_id = ? 
        ORDER BY obj_order ASC
    """, (goal_id,))
    objectives = cursor.fetchall()
    conn.close()
    return objectives


def fetch_topic_progress(username):
    conn = sqlite3.connect(DB_PATH)
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


def fetch_goal_progress(username, topic_name):
    """Fetch progress for all goals in a topic"""
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()
    
    cursor.execute("SELECT id FROM User WHERE username = ?", (username,))
    user_row = cursor.fetchone()
    if not user_row:
        conn.close()
        return []
    user_id = user_row[0]
    
    cursor.execute("SELECT id FROM Topic WHERE name = ?", (topic_name,))
    topic_row = cursor.fetchone()
    if not topic_row:
        conn.close()
        return []
    topic_id = topic_row[0]
    
    cursor.execute("""
        SELECT Goal.title, GoalProgress.grade, GoalProgress.is_completed
        FROM Goal
        LEFT JOIN GoalProgress ON Goal.id = GoalProgress.goal_id AND GoalProgress.user_id = ?
        WHERE Goal.topic_id = ?
        ORDER BY Goal.goal_order ASC
    """, (user_id, topic_id))
    
    goal_progress = cursor.fetchall()
    conn.close()
    return goal_progress


def update_goal_progress(username, goal_id, problems_correct, problems_total):
    """Update goal progress based on practice problem performance"""
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()
    
    cursor.execute("SELECT id FROM User WHERE username = ?", (username,))
    user_id = cursor.fetchone()[0]
    
    # Calculate grade as percentage
    grade = int((problems_correct / problems_total) * 100) if problems_total > 0 else 0
    is_completed = grade >= 70  # Consider 70% as passing
    
    cursor.execute("""
        INSERT INTO GoalProgress (user_id, goal_id, grade, is_completed)
        VALUES (?, ?, ?, ?)
        ON CONFLICT(user_id, goal_id) DO UPDATE SET 
            grade = MAX(grade, ?),
            is_completed = ?
    """, (user_id, goal_id, grade, is_completed, grade, is_completed))
    
    conn.commit()
    conn.close()
    
    # Update topic progress
    update_topic_progress_from_goals(username, goal_id)


def update_topic_progress_from_goals(username, goal_id):
    """Update topic progress based on goal completion"""
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()
    
    cursor.execute("SELECT id FROM User WHERE username = ?", (username,))
    user_id = cursor.fetchone()[0]
    
    # Get topic_id from goal_id
    cursor.execute("SELECT topic_id FROM Goal WHERE id = ?", (goal_id,))
    topic_id = cursor.fetchone()[0]
    
    # Calculate topic progress as average of all goal grades
    cursor.execute("""
        SELECT AVG(gp.grade)
        FROM Goal g
        LEFT JOIN GoalProgress gp ON g.id = gp.goal_id AND gp.user_id = ?
        WHERE g.topic_id = ?
    """, (user_id, topic_id))
    
    avg_grade = cursor.fetchone()[0]
    progress = int(avg_grade) if avg_grade else 0
    
    cursor.execute("""
        INSERT INTO TopicProgress (user_id, topic_id, progress)
        VALUES (?, ?, ?)
        ON CONFLICT(user_id, topic_id) DO UPDATE SET progress = ?
    """, (user_id, topic_id, progress, progress))
    
    conn.commit()
    conn.close()


def mark_topic_complete(username, topic_name):
    conn = sqlite3.connect(DB_PATH)
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


# ==================== AI PROBLEM GENERATION ====================

def generate_ai_problem(objective_id, category='factual'):
    """Generate an AI problem for a given learning objective"""
    if not AI_AVAILABLE:
        return None, None
    
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()
    
    cursor.execute("""
        SELECT lo.title, lo.description, g.title, t.name
        FROM LearningObjective lo
        JOIN Goal g ON lo.goal_id = g.id
        JOIN Topic t ON g.topic_id = t.id
        WHERE lo.id = ?
    """, (objective_id,))
    
    result = cursor.fetchone()
    conn.close()
    
    if not result:
        return None, None
    
    obj_title, obj_desc, goal_title, topic_name = result
    
    prompt = f"""You are an educational AI tutor. Generate a {category} knowledge question.

Topic: {topic_name}
Goal: {goal_title}
Learning Objective: {obj_title}
Description: {obj_desc}

Knowledge Type: {category}
- Factual: Basic facts and definitions
- Procedural: Step-by-step problem solving
- Strategic: Multi-step complex problems
- Rational: Explanations and reasoning

Generate a clear, concise problem and its answer. Format:
PROBLEM: [your problem here]
ANSWER: [correct answer here]"""
    
    try:
        response = client.models.generate_content(
            model='gemini-2.0-flash-exp',
            contents=prompt
        )
        
        text = response.text
        if "PROBLEM:" in text and "ANSWER:" in text:
            problem = text.split("PROBLEM:")[1].split("ANSWER:")[0].strip()
            answer = text.split("ANSWER:")[1].strip()
            return problem, answer
    except Exception as e:
        print(f"AI generation error: {e}")
    
    return None, None


def save_generated_problem(user_id, topic_id, goal_id, objective_id, problem, answer, category):
    """Save AI-generated problem to database"""
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()

    cursor.execute("""
        INSERT INTO GenProblem (user_id, topic_id, goal_id, objective_id, prompt, correct_answer, category)
        VALUES (?, ?, ?, ?, ?, ?, ?)
    """, (user_id, topic_id, goal_id, objective_id, problem, answer, category))

    problem_id = cursor.lastrowid
    conn.commit()
    conn.close()
    return problem_id


def record_practice_attempt(user_id, goal_id, problem_id, student_answer, is_correct):
    """Record a practice problem attempt"""
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()

    # Create or get practice set
    cursor.execute("""
        INSERT INTO PracticeProblemSet (user_id, goal_id)
        VALUES (?, ?)
    """, (user_id, goal_id))
    set_id = cursor.lastrowid

    # Record the attempt
    cursor.execute("""
        INSERT INTO PracticeProblem (set_id, genProblem_id, student_answer, is_correct, is_completed)
        VALUES (?, ?, ?, ?, TRUE)
    """, (set_id, problem_id, student_answer, is_correct))

    conn.commit()
    conn.close()


# ==================== UI HELPER FUNCTIONS ====================

def build_table(parent, columns, heading_map, rows, stretch_last=True, height=8):
    """Utility to create a styled ttk.Treeview table with a vertical scrollbar."""
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
        width = 140 if i < len(columns) - 1 or not stretch_last else 220
        tree.column(key, width=width, anchor="w", stretch=True if (stretch_last and i == len(columns) - 1) else False)

    # Insert rows
    for r in rows:
        tree.insert("", "end", values=r)

    return tree


# ==================== MAIN APPLICATION SCREENS ====================

def show_login_screen():
    """Display the login/register screen"""
    global current_user, current_user_id

    root = tk.Tk()
    root.title("Learning Management System - Login")
    root.geometry("400x250")

    tk.Label(root, text="Adaptive Learning System", font=("Helvetica", 18, "bold")).pack(pady=20)

    # Login frame
    login_frame = tk.Frame(root)
    login_frame.pack(pady=10)

    tk.Label(login_frame, text="Username:", font=("Helvetica", 12)).grid(row=0, column=0, padx=10, pady=10, sticky="e")
    username_entry = tk.Entry(login_frame, font=("Helvetica", 12))
    username_entry.grid(row=0, column=1, padx=10, pady=10)

    tk.Label(login_frame, text="Password:", font=("Helvetica", 12)).grid(row=1, column=0, padx=10, pady=10, sticky="e")
    password_entry = tk.Entry(login_frame, show="*", font=("Helvetica", 12))
    password_entry.grid(row=1, column=1, padx=10, pady=10)

    def handle_login():
        global current_user, current_user_id
        username = username_entry.get()
        password = password_entry.get()

        if auth_service.authenticate(username, password):
            current_user = username
            # Get user ID
            conn = sqlite3.connect(DB_PATH)
            cursor = conn.cursor()
            cursor.execute("SELECT id FROM User WHERE username = ?", (username,))
            current_user_id = cursor.fetchone()[0]
            conn.close()

            messagebox.showinfo("Login Success", f"Welcome, {username}!")
            root.destroy()
            show_main_dashboard()
        else:
            messagebox.showerror("Login Failed", "Invalid username or password.")

    def show_register_window():
        reg_window = tk.Toplevel(root)
        reg_window.title("Register")
        reg_window.geometry("400x350")

        tk.Label(reg_window, text="Register New Account", font=("Helvetica", 14, "bold")).pack(pady=10)

        fields_frame = tk.Frame(reg_window)
        fields_frame.pack(pady=10)

        tk.Label(fields_frame, text="Username:").grid(row=0, column=0, padx=10, pady=5, sticky="e")
        new_username_entry = tk.Entry(fields_frame)
        new_username_entry.grid(row=0, column=1, padx=10, pady=5)

        tk.Label(fields_frame, text="Password:").grid(row=1, column=0, padx=10, pady=5, sticky="e")
        new_password_entry = tk.Entry(fields_frame, show="*")
        new_password_entry.grid(row=1, column=1, padx=10, pady=5)

        tk.Label(fields_frame, text="First Name:").grid(row=2, column=0, padx=10, pady=5, sticky="e")
        new_first_name_entry = tk.Entry(fields_frame)
        new_first_name_entry.grid(row=2, column=1, padx=10, pady=5)

        tk.Label(fields_frame, text="Last Name:").grid(row=3, column=0, padx=10, pady=5, sticky="e")
        new_last_name_entry = tk.Entry(fields_frame)
        new_last_name_entry.grid(row=3, column=1, padx=10, pady=5)

        tk.Label(fields_frame, text="Email:").grid(row=4, column=0, padx=10, pady=5, sticky="e")
        new_email_entry = tk.Entry(fields_frame)
        new_email_entry.grid(row=4, column=1, padx=10, pady=5)

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

        tk.Button(reg_window, text="Register", command=register_user, font=("Helvetica", 12)).pack(pady=20)

    # Buttons
    btn_frame = tk.Frame(root)
    btn_frame.pack(pady=10)

    tk.Button(btn_frame, text="Login", command=handle_login, font=("Helvetica", 12), width=12).grid(row=0, column=0, padx=5)
    tk.Button(btn_frame, text="Register", command=show_register_window, font=("Helvetica", 12), width=12).grid(row=0, column=1, padx=5)

    root.mainloop()


def show_main_dashboard():
    """Display the main dashboard with navigation options"""
    main_app = tk.Tk()
    main_app.title("Learning Management System - Dashboard")
    main_app.geometry("900x650")

    welcome_label = tk.Label(main_app, text=f"Welcome, {current_user}!", font=("Helvetica", 18, "bold"))
    welcome_label.pack(pady=20)

    # Navigation buttons
    nav_frame = tk.Frame(main_app)
    nav_frame.pack(pady=15)

    tk.Button(nav_frame, text="📚 Student Pick Topic", font=("Helvetica", 14), width=22, height=2,
              bg="#4CAF50", fg="white", command=lambda: show_student_pick(main_app)).grid(row=0, column=0, padx=10, pady=5)

    tk.Button(nav_frame, text="🎲 Computer Pick Topic", font=("Helvetica", 14), width=22, height=2,
              bg="#2196F3", fg="white", command=lambda: handle_computer_pick(main_app)).grid(row=0, column=1, padx=10, pady=5)

    tk.Button(nav_frame, text="📊 View Progress", font=("Helvetica", 14), width=22, height=2,
              bg="#FF9800", fg="white", command=lambda: show_progress_dashboard(main_app)).grid(row=0, column=2, padx=10, pady=5)

    if AI_AVAILABLE:
        tk.Button(nav_frame, text="🤖 AI Practice Problems", font=("Helvetica", 14), width=22, height=2,
                  bg="#9C27B0", fg="white", command=lambda: show_ai_practice(main_app)).grid(row=1, column=0, padx=10, pady=5)

    tk.Button(nav_frame, text="🚪 Logout", font=("Helvetica", 12), width=15,
              command=lambda: logout(main_app)).grid(row=2, column=1, pady=20)

    main_app.mainloop()


def logout(window):
    """Logout and return to login screen"""
    global current_user, current_user_id
    current_user = None
    current_user_id = None
    window.destroy()
    show_login_screen()


def relaunch_dashboard(window):
    """Return to main dashboard"""
    window.destroy()
    show_main_dashboard()


def show_student_pick(window):
    """Show topic selection screen"""
    for widget in window.winfo_children():
        widget.destroy()

    tk.Label(window, text="Choose a Topic", font=("Helvetica", 16, "bold")).pack(pady=20)

    topics = fetch_all_topics()
    if not topics:
        messagebox.showinfo("No Topics", "No topics found in the database.")
        relaunch_dashboard(window)
        return

    for topic_id, topic_name in topics:
        tk.Button(
            window, text=topic_name, font=("Helvetica", 13), width=40, height=2,
            command=lambda t=topic_name: show_goals_for_topic(window, t)
        ).pack(pady=5)

    tk.Button(window, text="← Back to Dashboard", command=lambda: relaunch_dashboard(window),
              font=("Helvetica", 11)).pack(pady=20)


def handle_computer_pick(window):
    """Randomly select a topic"""
    topic = fetch_random_topic()
    if topic:
        topic_id, topic_name = topic
        show_goals_for_topic(window, topic_name)
    else:
        messagebox.showinfo("No Topics", "No topics available to choose from.")


def show_goals_for_topic(window, topic_name):
    """Show goals for selected topic"""
    for widget in window.winfo_children():
        widget.destroy()

    tk.Label(window, text=f"Topic: {topic_name}", font=("Helvetica", 16, "bold")).pack(pady=20)
    tk.Label(window, text="Learning Goals", font=("Helvetica", 14)).pack(pady=10)

    goals = fetch_goals_for_topic(topic_name)
    if not goals:
        messagebox.showinfo("No Goals", f"No goals found for topic '{topic_name}'.")
        relaunch_dashboard(window)
        return

    goal_index = [0]

    goal_label = tk.Label(window, text="", font=("Helvetica", 13), wraplength=700, justify="left")
    goal_label.pack(pady=20, padx=30)

    desc_label = tk.Label(window, text="", font=("Helvetica", 11), wraplength=700, justify="left")
    desc_label.pack(pady=10, padx=30)

    objectives_frame = tk.Frame(window)
    objectives_frame.pack(pady=10)

    def update_goal():
        if goal_index[0] < len(goals):
            goal_id, goal_title, goal_desc = goals[goal_index[0]]
            goal_label.config(text=f"Goal {goal_index[0] + 1}: {goal_title}")
            desc_label.config(text=goal_desc)

            # Clear objectives frame
            for widget in objectives_frame.winfo_children():
                widget.destroy()

            # Show objectives
            objectives = fetch_objectives_for_goal(goal_id)
            if objectives:
                tk.Label(objectives_frame, text="Learning Objectives:", font=("Helvetica", 12, "underline")).pack(pady=5)
                for obj_id, obj_title, obj_desc in objectives:
                    obj_text = f"• {obj_title}"
                    tk.Label(objectives_frame, text=obj_text, font=("Helvetica", 10), wraplength=650, justify="left").pack(anchor="w", padx=20)

    def next_goal():
        if goal_index[0] + 1 < len(goals):
            goal_index[0] += 1
            update_goal()
        else:
            mark_topic_complete(current_user, topic_name)
            messagebox.showinfo("Completed", f"You've completed all goals for '{topic_name}'!")
            relaunch_dashboard(window)

    def prev_goal():
        if goal_index[0] > 0:
            goal_index[0] -= 1
            update_goal()

    update_goal()

    btn_frame = tk.Frame(window)
    btn_frame.pack(pady=20)

    tk.Button(btn_frame, text="← Previous", command=prev_goal, font=("Helvetica", 11), width=12).grid(row=0, column=0, padx=10)
    tk.Button(btn_frame, text="Next →", command=next_goal, font=("Helvetica", 11), width=12).grid(row=0, column=1, padx=10)
    tk.Button(btn_frame, text="Practice Problems", command=lambda: show_practice_for_goal(window, topic_name, goals[goal_index[0]][0]),
              font=("Helvetica", 11), width=18, bg="#4CAF50", fg="white").grid(row=0, column=2, padx=10)

    tk.Button(window, text="← Back to Topics", command=lambda: show_student_pick(window),
              font=("Helvetica", 11)).pack(pady=10)


def show_progress_dashboard(window):
    """Display progress tracking dashboard"""
    for widget in window.winfo_children():
        widget.destroy()

    header = tk.Label(window, text="Your Progress", font=("Helvetica", 18, "bold"))
    header.pack(pady=15)

    container = tk.Frame(window)
    container.pack(fill="both", expand=True)

    # Topic Progress
    section1 = tk.Label(container, text="Topic Progress", font=("Helvetica", 14, "underline"))
    section1.pack(anchor="w", padx=10, pady=(10, 5))

    topic_rows = []
    progress_data = fetch_topic_progress(current_user)
    for topic, progress in progress_data:
        pct = 0 if progress is None else progress
        topic_rows.append((topic, f"{pct}%"))

    build_table(
        parent=container,
        columns=["topic", "progress"],
        heading_map={"topic": "Topic", "progress": "Progress"},
        rows=topic_rows,
        stretch_last=True,
        height=10
    )

    def show_completed_topics():
        completed = [topic for topic, prog in progress_data if (prog or 0) == 100]
        if completed:
            messagebox.showinfo("Completed Topics", "\n".join(completed))
        else:
            messagebox.showinfo("Completed Topics", "No topics completed yet.")

    tk.Button(container, text="View Completed Topics", command=show_completed_topics,
              font=("Helvetica", 10)).pack(anchor="e", padx=12, pady=(5, 15))

    tk.Button(window, text="← Back to Dashboard", command=lambda: relaunch_dashboard(window),
              font=("Helvetica", 11)).pack(pady=15)


def show_practice_for_goal(window, topic_name, goal_id):
    """Show practice problems for a specific goal"""
    for widget in window.winfo_children():
        widget.destroy()

    # Get goal info
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()
    cursor.execute("SELECT title, topic_id FROM Goal WHERE id = ?", (goal_id,))
    result = cursor.fetchone()
    conn.close()

    if not result:
        messagebox.showerror("Error", "Goal not found.")
        relaunch_dashboard(window)
        return

    goal_title, topic_id = result

    tk.Label(window, text=f"Practice: {goal_title}", font=("Helvetica", 16, "bold")).pack(pady=20)

    objectives = fetch_objectives_for_goal(goal_id)
    if not objectives:
        messagebox.showinfo("No Objectives", "No learning objectives found for this goal.")
        show_goals_for_topic(window, topic_name)
        return

    tk.Label(window, text="Select a Learning Objective:", font=("Helvetica", 13)).pack(pady=10)

    for obj_id, obj_title, obj_desc in objectives:
        btn = tk.Button(
            window,
            text=f"{obj_title}",
            font=("Helvetica", 11),
            width=60,
            height=2,
            command=lambda oid=obj_id, tid=topic_id, gid=goal_id, ot=obj_title: generate_practice_problem(window, topic_name, tid, gid, oid, ot)
        )
        btn.pack(pady=5)

    tk.Button(window, text="← Back to Goals", command=lambda: show_goals_for_topic(window, topic_name),
              font=("Helvetica", 11)).pack(pady=20)


def generate_practice_problem(window, topic_name, topic_id, goal_id, objective_id, objective_title):
    """Generate and display a practice problem"""
    if not AI_AVAILABLE:
        messagebox.showerror("AI Not Available", "AI features require google-genai package to be installed.")
        return

    # Ask for problem type
    problem_window = tk.Toplevel(window)
    problem_window.title("Practice Problem")
    problem_window.geometry("700x600")

    tk.Label(problem_window, text=f"Generating problem for:", font=("Helvetica", 12, "bold")).pack(pady=10)
    tk.Label(problem_window, text=objective_title, font=("Helvetica", 11), wraplength=650).pack(pady=5)

    tk.Label(problem_window, text="Select Problem Type:", font=("Helvetica", 12)).pack(pady=15)

    category_var = tk.StringVar(value="factual")

    categories = [
        ("Factual - Basic facts and definitions", "factual"),
        ("Procedural - Step-by-step problem solving", "procedural"),
        ("Strategic - Multi-step complex problems", "strategic"),
        ("Rational - Explanations and reasoning", "rational")
    ]

    for text, value in categories:
        tk.Radiobutton(problem_window, text=text, variable=category_var, value=value,
                      font=("Helvetica", 10)).pack(anchor="w", padx=50)

    problem_text = tk.Text(problem_window, height=10, width=70, font=("Helvetica", 10), wrap="word", state="disabled")
    problem_text.pack(pady=15, padx=20)

    # Answer input section - create a frame for it
    answer_frame = tk.Frame(problem_window)
    answer_frame.pack(pady=10)

    answer_label = tk.Label(answer_frame, text="Your Answer:", font=("Helvetica", 11))
    answer_label.grid(row=0, column=0, padx=5, pady=5)

    answer_entry = tk.Entry(answer_frame, font=("Helvetica", 11), width=50)
    answer_entry.grid(row=0, column=1, padx=5, pady=5)

    # Initially hide the answer frame
    answer_frame.pack_forget()

    correct_answer = [None]
    generated_problem_id = [None]

    def generate():
        category = category_var.get()
        problem_text.config(state="normal")
        problem_text.delete(1.0, tk.END)
        problem_text.insert(1.0, "Generating problem... Please wait...")
        problem_text.config(state="disabled")
        problem_window.update()

        problem, answer = generate_ai_problem(objective_id, category)

        if problem and answer:
            problem_text.config(state="normal")
            problem_text.delete(1.0, tk.END)
            problem_text.insert(1.0, problem)
            problem_text.config(state="disabled")

            correct_answer[0] = answer

            # Save to database
            problem_id = save_generated_problem(current_user_id, topic_id, goal_id, objective_id, problem, answer, category)
            generated_problem_id[0] = problem_id

            # Show answer input frame
            answer_frame.pack(pady=10)
            answer_entry.delete(0, tk.END)  # Clear any previous answer
            answer_entry.focus()  # Focus on the entry field
        else:
            problem_text.config(state="normal")
            problem_text.delete(1.0, tk.END)
            problem_text.insert(1.0, "Failed to generate problem. Please try again.")
            problem_text.config(state="disabled")
            answer_frame.pack_forget()  # Hide answer input if generation failed

    def submit_answer():
        if correct_answer[0] is None:
            messagebox.showwarning("No Problem", "Please generate a problem first.")
            return

        student_answer = answer_entry.get().strip()
        if not student_answer:
            messagebox.showwarning("No Answer", "Please enter your answer.")
            return

        # Simple check - could be enhanced with AI evaluation
        is_correct = student_answer.lower() == correct_answer[0].lower()

        # Record the attempt
        record_practice_attempt(current_user_id, goal_id, generated_problem_id[0], student_answer, is_correct)

        # Update progress (simplified - 1 correct out of 1 total)
        update_goal_progress(current_user, goal_id, 1 if is_correct else 0, 1)

        if is_correct:
            messagebox.showinfo("Correct! ✓", f"Great job! Your answer is correct.\n\nCorrect Answer: {correct_answer[0]}")
        else:
            messagebox.showinfo("Incorrect ✗", f"Not quite right. Keep practicing!\n\nYour Answer: {student_answer}\nCorrect Answer: {correct_answer[0]}")

        problem_window.destroy()

    btn_frame = tk.Frame(problem_window)
    btn_frame.pack(pady=15)

    tk.Button(btn_frame, text="Generate Problem", command=generate, font=("Helvetica", 11),
              bg="#4CAF50", fg="white", width=18).grid(row=0, column=0, padx=10)
    tk.Button(btn_frame, text="Submit Answer", command=submit_answer, font=("Helvetica", 11),
              bg="#2196F3", fg="white", width=18).grid(row=0, column=1, padx=10)
    tk.Button(btn_frame, text="Close", command=problem_window.destroy, font=("Helvetica", 11),
              width=18).grid(row=0, column=2, padx=10)


def show_ai_practice(window):
    """Show AI practice interface"""
    for widget in window.winfo_children():
        widget.destroy()

    tk.Label(window, text="AI Practice Problems", font=("Helvetica", 18, "bold")).pack(pady=20)
    tk.Label(window, text="Select a topic and goal to practice with AI-generated problems",
             font=("Helvetica", 11)).pack(pady=10)

    topics = fetch_all_topics()

    tk.Label(window, text="Choose Topic:", font=("Helvetica", 13)).pack(pady=10)

    for topic_id, topic_name in topics:
        tk.Button(
            window, text=topic_name, font=("Helvetica", 12), width=40, height=2,
            command=lambda tn=topic_name: show_ai_goals(window, tn)
        ).pack(pady=5)

    tk.Button(window, text="← Back to Dashboard", command=lambda: relaunch_dashboard(window),
              font=("Helvetica", 11)).pack(pady=20)


def show_ai_goals(window, topic_name):
    """Show goals for AI practice"""
    for widget in window.winfo_children():
        widget.destroy()

    tk.Label(window, text=f"AI Practice: {topic_name}", font=("Helvetica", 16, "bold")).pack(pady=20)
    tk.Label(window, text="Select a goal to practice:", font=("Helvetica", 12)).pack(pady=10)

    goals = fetch_goals_for_topic(topic_name)

    for goal_id, goal_title, goal_desc in goals:
        tk.Button(
            window, text=goal_title, font=("Helvetica", 11), width=50, height=2,
            command=lambda gid=goal_id, tn=topic_name: show_practice_for_goal(window, tn, gid)
        ).pack(pady=5)

    tk.Button(window, text="← Back", command=lambda: show_ai_practice(window),
              font=("Helvetica", 11)).pack(pady=20)


# ==================== MAIN ENTRY POINT ====================

if __name__ == "__main__":
    print("=" * 60)
    print("Adaptive AI-based Learning Management System")
    print("=" * 60)
    print(f"Database: {DB_PATH}")
    print(f"AI Features: {'Enabled' if AI_AVAILABLE else 'Disabled (install google-genai)'}")
    print("=" * 60)
    print()

    # Check if database exists
    if not os.path.exists(DB_PATH):
        print("WARNING: Database not found. Please run main.py to initialize the database first.")
        response = input("Continue anyway? (y/n): ")
        if response.lower() != 'y':
            exit()

    show_login_screen()



