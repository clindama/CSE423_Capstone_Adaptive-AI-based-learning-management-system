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
    try:
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
    except sqlite3.OperationalError as e:
        if "no such table" in str(e):
            print(f"ERROR: {e}")
            print("Please run: python add_ai_tables.py")
            messagebox.showerror("Database Error",
                "Missing AI tables in database.\n\n"
                "Please run this command first:\n"
                "python add_ai_tables.py")
        raise


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

    # Record the attempt - use problem_id column (not genProblem_id)
    cursor.execute("""
        INSERT INTO PracticeProblem (set_id, problem_id, student_answer, is_correct, is_completed)
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


def get_ai_feedback(problem_text, student_answer, correct_answer, is_correct):
    """Generate AI feedback for a student's answer"""
    if not AI_AVAILABLE:
        return "AI feedback not available. Please install google-genai package."

    try:
        prompt = f"""You are a helpful math tutor. A student attempted this problem:

Problem: {problem_text}

Student's Answer: {student_answer}
Correct Answer: {correct_answer}
Result: {"Correct" if is_correct else "Incorrect"}

Provide constructive feedback:
1. If correct: Praise the student and explain why the answer is right
2. If incorrect: Gently explain the mistake and guide them to the correct solution
3. Provide tips or insights to help them understand the concept better

Keep the feedback encouraging, clear, and educational. Use simple language."""

        response = client.models.generate_content(
            model='gemini-1.5-flash',
            contents=prompt
        )
        return response.text
    except Exception as e:
        return f"Could not generate AI feedback: {str(e)}"


def show_ai_feedback_dialog(problem_text, student_answer, correct_answer, is_correct):
    """Show AI feedback in a dialog window"""
    feedback_window = tk.Toplevel()
    feedback_window.title("AI Feedback")
    feedback_window.geometry("700x600")

    # Header
    header_frame = tk.Frame(feedback_window, bg="#4CAF50" if is_correct else "#f44336", height=60)
    header_frame.pack(fill="x")
    header_frame.pack_propagate(False)

    result_text = "✓ Correct Answer" if is_correct else "✗ Incorrect Answer"
    tk.Label(header_frame, text=result_text, font=("Helvetica", 16, "bold"),
             bg="#4CAF50" if is_correct else "#f44336", fg="white").pack(pady=15)

    # Content area with scrollbar
    content_frame = tk.Frame(feedback_window)
    content_frame.pack(fill="both", expand=True, padx=20, pady=20)

    # Problem section
    tk.Label(content_frame, text="Problem:", font=("Helvetica", 12, "bold")).pack(anchor="w", pady=(0, 5))
    problem_label = tk.Label(content_frame, text=problem_text, font=("Helvetica", 10),
                             wraplength=650, justify="left", bg="#f0f0f0", padx=10, pady=10)
    problem_label.pack(fill="x", pady=(0, 15))

    # Answers section
    answers_frame = tk.Frame(content_frame)
    answers_frame.pack(fill="x", pady=(0, 15))

    tk.Label(answers_frame, text="Your Answer:", font=("Helvetica", 11, "bold")).grid(row=0, column=0, sticky="w", pady=5)
    tk.Label(answers_frame, text=student_answer, font=("Helvetica", 10)).grid(row=0, column=1, sticky="w", padx=10)

    tk.Label(answers_frame, text="Correct Answer:", font=("Helvetica", 11, "bold")).grid(row=1, column=0, sticky="w", pady=5)
    tk.Label(answers_frame, text=correct_answer, font=("Helvetica", 10)).grid(row=1, column=1, sticky="w", padx=10)

    # AI Feedback section
    tk.Label(content_frame, text="AI Tutor Feedback:", font=("Helvetica", 12, "bold")).pack(anchor="w", pady=(10, 5))

    feedback_text = tk.Text(content_frame, height=15, width=70, font=("Helvetica", 10),
                           wrap="word", bg="#fffef0", padx=10, pady=10)
    feedback_text.pack(fill="both", expand=True)

    scrollbar = tk.Scrollbar(feedback_text)
    scrollbar.pack(side="right", fill="y")
    feedback_text.config(yscrollcommand=scrollbar.set)
    scrollbar.config(command=feedback_text.yview)

    # Show loading message
    feedback_text.insert(1.0, "Generating AI feedback... Please wait...")
    feedback_text.config(state="disabled")
    feedback_window.update()

    # Generate feedback
    feedback = get_ai_feedback(problem_text, student_answer, correct_answer, is_correct)

    feedback_text.config(state="normal")
    feedback_text.delete(1.0, tk.END)
    feedback_text.insert(1.0, feedback)
    feedback_text.config(state="disabled")

    # Close button
    tk.Button(feedback_window, text="Close", command=feedback_window.destroy,
             font=("Helvetica", 11), width=15, bg="#2196F3", fg="white").pack(pady=15)


def fetch_practice_history(username):
    """Fetch detailed practice history for a user"""
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()

    # Get user_id
    cursor.execute("SELECT id FROM User WHERE username = ?", (username,))
    result = cursor.fetchone()
    if not result:
        conn.close()
        return []

    user_id = result[0]

    # Fetch practice history with all details
    cursor.execute("""
        SELECT
            t.name as topic_name,
            g.title as goal_title,
            lo.title as objective_title,
            gp.prompt as problem_text,
            pp.student_answer,
            gp.correct_answer,
            pp.is_correct,
            gp.category,
            ps.start_time,
            gp.id as problem_id
        FROM PracticeProblem pp
        JOIN PracticeProblemSet ps ON pp.set_id = ps.id
        JOIN GenProblem gp ON pp.problem_id = gp.id
        JOIN Goal g ON gp.goal_id = g.id
        JOIN Topic t ON gp.topic_id = t.id
        JOIN LearningObjective lo ON gp.objective_id = lo.id
        WHERE ps.user_id = ?
        ORDER BY ps.start_time DESC
    """, (user_id,))

    history = cursor.fetchall()
    conn.close()
    return history


def show_progress_dashboard(window):
    """Display enhanced progress tracking dashboard with detailed history"""
    for widget in window.winfo_children():
        widget.destroy()

    # Create main container with scrollbar
    main_canvas = tk.Canvas(window)
    scrollbar = tk.Scrollbar(window, orient="vertical", command=main_canvas.yview)
    scrollable_frame = tk.Frame(main_canvas)

    def configure_main_scroll(event):
        main_canvas.configure(scrollregion=main_canvas.bbox("all"))

    scrollable_frame.bind("<Configure>", configure_main_scroll)

    main_canvas.create_window((0, 0), window=scrollable_frame, anchor="nw")
    main_canvas.configure(yscrollcommand=scrollbar.set)

    # Enable mouse wheel scrolling for main canvas
    def on_main_mousewheel(event):
        main_canvas.yview_scroll(int(-1*(event.delta/120)), "units")

    def bind_mousewheel(event):
        main_canvas.bind_all("<MouseWheel>", on_main_mousewheel)

    def unbind_mousewheel(event):
        main_canvas.unbind_all("<MouseWheel>")

    main_canvas.bind("<Enter>", bind_mousewheel)
    main_canvas.bind("<Leave>", unbind_mousewheel)

    # Header
    header = tk.Label(scrollable_frame, text="📊 Your Learning Progress", font=("Helvetica", 20, "bold"))
    header.pack(pady=20)

    # ==================== SECTION 1: TOPIC PROGRESS ====================
    topic_section = tk.LabelFrame(scrollable_frame, text="📚 Topic Progress Overview",
                                  font=("Helvetica", 14, "bold"), padx=20, pady=15)
    topic_section.pack(fill="x", padx=20, pady=10)

    progress_data = fetch_topic_progress(current_user)

    if progress_data:
        for topic, progress in progress_data:
            pct = 0 if progress is None else progress

            topic_frame = tk.Frame(topic_section)
            topic_frame.pack(fill="x", pady=8)

            tk.Label(topic_frame, text=topic, font=("Helvetica", 11, "bold"), width=30, anchor="w").pack(side="left")

            # Progress bar
            progress_canvas = tk.Canvas(topic_frame, width=300, height=25, bg="white", highlightthickness=1)
            progress_canvas.pack(side="left", padx=10)

            # Draw progress bar
            if pct > 0:
                bar_width = int(300 * pct / 100)
                color = "#4CAF50" if pct >= 70 else "#FFC107" if pct >= 40 else "#f44336"
                progress_canvas.create_rectangle(0, 0, bar_width, 25, fill=color, outline="")

            progress_canvas.create_text(150, 12, text=f"{pct}%", font=("Helvetica", 10, "bold"))

            # Status badge
            if pct == 100:
                tk.Label(topic_frame, text="✓ Complete", font=("Helvetica", 9),
                        bg="#4CAF50", fg="white", padx=8, pady=2).pack(side="left")
            elif pct >= 70:
                tk.Label(topic_frame, text="⚡ Almost There", font=("Helvetica", 9),
                        bg="#FFC107", fg="black", padx=8, pady=2).pack(side="left")
            elif pct > 0:
                tk.Label(topic_frame, text="📝 In Progress", font=("Helvetica", 9),
                        bg="#2196F3", fg="white", padx=8, pady=2).pack(side="left")
    else:
        tk.Label(topic_section, text="No progress yet. Start practicing to see your progress!",
                font=("Helvetica", 10, "italic")).pack(pady=10)

    # ==================== SECTION 2: PRACTICE HISTORY ====================
    history_section = tk.LabelFrame(scrollable_frame, text="📝 Detailed Practice History",
                                    font=("Helvetica", 14, "bold"), padx=20, pady=15)
    history_section.pack(fill="both", expand=True, padx=20, pady=10)

    practice_history = fetch_practice_history(current_user)

    if practice_history:
        # Group by topic
        topics_dict = {}
        for record in practice_history:
            topic_name = record[0]
            if topic_name not in topics_dict:
                topics_dict[topic_name] = []
            topics_dict[topic_name].append(record)

        # Create notebook (tabs) for each topic
        notebook = ttk.Notebook(history_section)
        notebook.pack(fill="both", expand=True)

        for topic_name, records in topics_dict.items():
            # Create tab for each topic
            topic_tab = tk.Frame(notebook)
            notebook.add(topic_tab, text=f"📚 {topic_name} ({len(records)})")

            # Create canvas with scrollbar for this topic
            topic_canvas = tk.Canvas(topic_tab)
            topic_scrollbar = tk.Scrollbar(topic_tab, orient="vertical", command=topic_canvas.yview)
            topic_scrollable = tk.Frame(topic_canvas)

            # Use a function to capture the canvas correctly
            def configure_scroll_region(event, canvas=topic_canvas):
                canvas.configure(scrollregion=canvas.bbox("all"))

            topic_scrollable.bind("<Configure>", configure_scroll_region)

            topic_canvas.create_window((0, 0), window=topic_scrollable, anchor="nw", width=window.winfo_width()-50)
            topic_canvas.configure(yscrollcommand=topic_scrollbar.set)

            # Enable mouse wheel scrolling
            def on_tab_mousewheel(event, canvas=topic_canvas):
                canvas.yview_scroll(int(-1*(event.delta/120)), "units")

            def bind_tab_mousewheel(event, canvas=topic_canvas):
                canvas.bind_all("<MouseWheel>", lambda e: on_tab_mousewheel(e, canvas))

            def unbind_tab_mousewheel(event, canvas=topic_canvas):
                canvas.unbind_all("<MouseWheel>")

            topic_canvas.bind("<Enter>", bind_tab_mousewheel)
            topic_canvas.bind("<Leave>", unbind_tab_mousewheel)

            topic_canvas.pack(side="left", fill="both", expand=True)
            topic_scrollbar.pack(side="right", fill="y")

            # Display each practice attempt
            for idx, record in enumerate(records, 1):
                (topic_name, goal_title, objective_title, problem_text,
                 student_answer, correct_answer, is_correct, category,
                 start_time, problem_id) = record

                # Create card for each attempt
                card = tk.Frame(topic_scrollable, relief="raised", borderwidth=2, bg="#f9f9f9")
                card.pack(fill="x", padx=10, pady=8)

                # Header row with result indicator
                header_frame = tk.Frame(card, bg="#4CAF50" if is_correct else "#f44336", height=35)
                header_frame.pack(fill="x")
                header_frame.pack_propagate(False)

                result_icon = "✓" if is_correct else "✗"
                result_text = "CORRECT" if is_correct else "INCORRECT"
                tk.Label(header_frame, text=f"{result_icon} {result_text}",
                        font=("Helvetica", 11, "bold"),
                        bg="#4CAF50" if is_correct else "#f44336",
                        fg="white").pack(side="left", padx=15, pady=5)

                tk.Label(header_frame, text=f"Attempt #{idx}",
                        font=("Helvetica", 9),
                        bg="#4CAF50" if is_correct else "#f44336",
                        fg="white").pack(side="left")

                tk.Label(header_frame, text=f"📅 {start_time}",
                        font=("Helvetica", 9),
                        bg="#4CAF50" if is_correct else "#f44336",
                        fg="white").pack(side="right", padx=15)

                # Content area
                content = tk.Frame(card, bg="#f9f9f9", padx=15, pady=10)
                content.pack(fill="x")

                # Goal and Objective
                info_frame = tk.Frame(content, bg="#f9f9f9")
                info_frame.pack(fill="x", pady=(0, 10))

                tk.Label(info_frame, text="🎯 Goal:", font=("Helvetica", 9, "bold"),
                        bg="#f9f9f9").grid(row=0, column=0, sticky="w", padx=(0, 5))
                tk.Label(info_frame, text=goal_title, font=("Helvetica", 9),
                        bg="#f9f9f9").grid(row=0, column=1, sticky="w")

                tk.Label(info_frame, text="📌 Objective:", font=("Helvetica", 9, "bold"),
                        bg="#f9f9f9").grid(row=1, column=0, sticky="w", padx=(0, 5), pady=(3, 0))
                tk.Label(info_frame, text=objective_title, font=("Helvetica", 9),
                        bg="#f9f9f9").grid(row=1, column=1, sticky="w", pady=(3, 0))

                tk.Label(info_frame, text="🏷️ Type:", font=("Helvetica", 9, "bold"),
                        bg="#f9f9f9").grid(row=2, column=0, sticky="w", padx=(0, 5), pady=(3, 0))
                tk.Label(info_frame, text=category.capitalize(), font=("Helvetica", 9),
                        bg="#f9f9f9").grid(row=2, column=1, sticky="w", pady=(3, 0))

                # Problem
                tk.Label(content, text="❓ Problem:", font=("Helvetica", 10, "bold"),
                        bg="#f9f9f9").pack(anchor="w", pady=(5, 3))
                problem_label = tk.Label(content, text=problem_text, font=("Helvetica", 9),
                                        wraplength=700, justify="left", bg="white",
                                        padx=10, pady=8, relief="solid", borderwidth=1)
                problem_label.pack(fill="x", pady=(0, 10))

                # Answers
                answers_frame = tk.Frame(content, bg="#f9f9f9")
                answers_frame.pack(fill="x", pady=(0, 10))

                tk.Label(answers_frame, text="Your Answer:", font=("Helvetica", 9, "bold"),
                        bg="#f9f9f9", width=15, anchor="w").grid(row=0, column=0, sticky="w", pady=3)
                tk.Label(answers_frame, text=student_answer, font=("Helvetica", 9),
                        bg="#ffe6e6" if not is_correct else "#e6ffe6",
                        padx=8, pady=4, relief="solid", borderwidth=1).grid(row=0, column=1, sticky="w", padx=5)

                tk.Label(answers_frame, text="Correct Answer:", font=("Helvetica", 9, "bold"),
                        bg="#f9f9f9", width=15, anchor="w").grid(row=1, column=0, sticky="w", pady=3)
                tk.Label(answers_frame, text=correct_answer, font=("Helvetica", 9),
                        bg="#e6ffe6", padx=8, pady=4, relief="solid", borderwidth=1).grid(row=1, column=1, sticky="w", padx=5)

                # AI Feedback Button
                feedback_btn = tk.Button(content, text="🤖 Get AI Feedback",
                                        font=("Helvetica", 10, "bold"),
                                        bg="#2196F3", fg="white", padx=20, pady=8,
                                        cursor="hand2",
                                        command=lambda p=problem_text, s=student_answer, c=correct_answer, i=is_correct:
                                        show_ai_feedback_dialog(p, s, c, i))
                feedback_btn.pack(pady=(5, 0))

    else:
        tk.Label(history_section, text="No practice history yet. Start solving problems to see your history!",
                font=("Helvetica", 11, "italic"), fg="#666").pack(pady=30)

    # Pack canvas and scrollbar
    main_canvas.pack(side="left", fill="both", expand=True)
    scrollbar.pack(side="right", fill="y")

    # Back button
    back_btn = tk.Button(window, text="← Back to Dashboard",
                        command=lambda: relaunch_dashboard(window),
                        font=("Helvetica", 12, "bold"), bg="#607D8B", fg="white",
                        padx=20, pady=10)
    back_btn.pack(side="bottom", pady=15)


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



