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
API_KEY = "AIzaSyDlIbDoYs5yqCTpyf-FPXuwRIWvecl5Lc0"  # Your Gemini API key

# Initialize services
auth_service = AuthService(db_path=DB_PATH)
if AI_AVAILABLE:
    client = genai.Client(api_key=API_KEY)

# Global state
current_user = None
current_user_id = None

# ==================== MODERN UI THEME ====================

# Color Palette - Modern, Professional
COLORS = {
    'primary': '#2563eb',      # Blue
    'primary_dark': '#1e40af',
    'primary_light': '#3b82f6',
    'success': '#10b981',      # Green
    'success_dark': '#059669',
    'warning': '#f59e0b',      # Orange
    'warning_dark': '#d97706',
    'danger': '#ef4444',       # Red
    'danger_dark': '#dc2626',
    'purple': '#8b5cf6',
    'purple_dark': '#7c3aed',
    'bg_primary': '#ffffff',   # White
    'bg_secondary': '#f8fafc', # Light gray
    'bg_tertiary': '#f1f5f9',
    'text_primary': '#1e293b',
    'text_secondary': '#64748b',
    'border': '#e2e8f0',
    'shadow': '#94a3b8'
}

# Fonts
FONTS = {
    'title': ('Segoe UI', 24, 'bold'),
    'heading': ('Segoe UI', 18, 'bold'),
    'subheading': ('Segoe UI', 14, 'bold'),
    'body': ('Segoe UI', 11),
    'body_bold': ('Segoe UI', 11, 'bold'),
    'small': ('Segoe UI', 9),
    'button': ('Segoe UI', 11, 'bold'),
    'button_large': ('Segoe UI', 13, 'bold')
}

def create_modern_button(parent, text, command, bg_color, width=20, height=2, icon=""):
    """Create a modern styled button with hover effects"""
    btn_frame = tk.Frame(parent, bg=parent['bg'])

    button_text = f"{icon} {text}" if icon else text

    btn = tk.Button(
        btn_frame,
        text=button_text,
        command=command,
        font=FONTS['button'],
        bg=bg_color,
        fg='white',
        activebackground=bg_color,
        activeforeground='white',
        relief='flat',
        cursor='hand2',
        width=width,
        height=height,
        borderwidth=0
    )
    btn.pack(padx=2, pady=2)

    # Hover effects
    def on_enter(e):
        btn.config(bg=COLORS.get(bg_color + '_dark', bg_color))

    def on_leave(e):
        btn.config(bg=bg_color)

    btn.bind("<Enter>", on_enter)
    btn.bind("<Leave>", on_leave)

    return btn_frame

def create_card(parent, title="", padding=20):
    """Create a modern card container"""
    card = tk.Frame(
        parent,
        bg=COLORS['bg_primary'],
        relief='flat',
        borderwidth=1,
        highlightbackground=COLORS['border'],
        highlightthickness=1
    )

    if title:
        title_label = tk.Label(
            card,
            text=title,
            font=FONTS['subheading'],
            bg=COLORS['bg_primary'],
            fg=COLORS['text_primary']
        )
        title_label.pack(anchor='w', padx=padding, pady=(padding, 10))

    return card


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
            model='gemini-2.5-flash',
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
    """Display the modern login/register screen"""
    global current_user, current_user_id

    root = tk.Tk()
    root.title("Learning Management System")
    root.geometry("520x700")
    root.configure(bg=COLORS['bg_secondary'])

    # Center window
    root.update_idletasks()
    width = root.winfo_width()
    height = root.winfo_height()
    x = (root.winfo_screenwidth() // 2) - (width // 2)
    y = (root.winfo_screenheight() // 2) - (height // 2)
    root.geometry(f'{width}x{height}+{x}+{y}')

    # Main container
    main_frame = tk.Frame(root, bg=COLORS['bg_secondary'])
    main_frame.pack(expand=True, fill='both', padx=40, pady=40)

    # Logo/Title area
    title_frame = tk.Frame(main_frame, bg=COLORS['bg_secondary'])
    title_frame.pack(pady=(0, 30))

    tk.Label(
        title_frame,
        text="🎓",
        font=('Segoe UI', 48),
        bg=COLORS['bg_secondary']
    ).pack()

    tk.Label(
        title_frame,
        text="Learning Management System",
        font=FONTS['title'],
        bg=COLORS['bg_secondary'],
        fg=COLORS['text_primary']
    ).pack(pady=(10, 5))

    tk.Label(
        title_frame,
        text="AI-Powered Adaptive Learning",
        font=FONTS['body'],
        bg=COLORS['bg_secondary'],
        fg=COLORS['text_secondary']
    ).pack()

    # Login card
    login_card = tk.Frame(
        main_frame,
        bg=COLORS['bg_primary'],
        relief='flat',
        highlightbackground=COLORS['border'],
        highlightthickness=1
    )
    login_card.pack(fill='x', pady=20)

    card_content = tk.Frame(login_card, bg=COLORS['bg_primary'])
    card_content.pack(padx=40, pady=40)

    tk.Label(
        card_content,
        text="Sign In",
        font=FONTS['heading'],
        bg=COLORS['bg_primary'],
        fg=COLORS['text_primary']
    ).pack(pady=(0, 25))

    # Username
    tk.Label(
        card_content,
        text="Username",
        font=FONTS['body_bold'],
        bg=COLORS['bg_primary'],
        fg=COLORS['text_primary']
    ).pack(anchor='w', pady=(0, 5))

    username_entry = tk.Entry(
        card_content,
        font=FONTS['body'],
        width=30,
        relief='solid',
        borderwidth=1,
        highlightthickness=2,
        highlightbackground=COLORS['border'],
        highlightcolor=COLORS['primary']
    )
    username_entry.pack(pady=(0, 20), ipady=8)

    # Password
    tk.Label(
        card_content,
        text="Password",
        font=FONTS['body_bold'],
        bg=COLORS['bg_primary'],
        fg=COLORS['text_primary']
    ).pack(anchor='w', pady=(0, 5))

    password_entry = tk.Entry(
        card_content,
        show="●",
        font=FONTS['body'],
        width=30,
        relief='solid',
        borderwidth=1,
        highlightthickness=2,
        highlightbackground=COLORS['border'],
        highlightcolor=COLORS['primary']
    )
    password_entry.pack(pady=(0, 25), ipady=8)

    def handle_login():
        global current_user, current_user_id
        username = username_entry.get()
        password = password_entry.get()

        if auth_service.authenticate(username, password):
            current_user = username
            conn = sqlite3.connect(DB_PATH)
            cursor = conn.cursor()
            cursor.execute("SELECT id FROM User WHERE username = ?", (username,))
            current_user_id = cursor.fetchone()[0]
            conn.close()

            root.destroy()
            show_main_dashboard()
        else:
            messagebox.showerror("Login Failed", "Invalid username or password.")

    # Login button
    login_btn = tk.Button(
        card_content,
        text="Sign In",
        command=handle_login,
        font=FONTS['button_large'],
        bg=COLORS['primary'],
        fg='white',
        activebackground=COLORS['primary_dark'],
        activeforeground='white',
        relief='flat',
        cursor='hand2',
        width=25,
        height=2,
        borderwidth=0
    )
    login_btn.pack()

    def on_enter_login(e):
        login_btn.config(bg=COLORS['primary_dark'])

    def on_leave_login(e):
        login_btn.config(bg=COLORS['primary'])

    login_btn.bind("<Enter>", on_enter_login)
    login_btn.bind("<Leave>", on_leave_login)

    # Register link
    register_frame = tk.Frame(card_content, bg=COLORS['bg_primary'])
    register_frame.pack(pady=(15, 0))

    tk.Label(
        register_frame,
        text="Don't have an account?",
        font=FONTS['body'],
        bg=COLORS['bg_primary'],
        fg=COLORS['text_secondary']
    ).pack(side='left', padx=(0, 5))

    def show_register_window():
        reg_window = tk.Toplevel(root)
        reg_window.title("Create Account")
        reg_window.geometry("500x600")
        reg_window.configure(bg=COLORS['bg_secondary'])

        # Center window
        reg_window.update_idletasks()
        width = reg_window.winfo_width()
        height = reg_window.winfo_height()
        x = (reg_window.winfo_screenwidth() // 2) - (width // 2)
        y = (reg_window.winfo_screenheight() // 2) - (height // 2)
        reg_window.geometry(f'{width}x{height}+{x}+{y}')

        # Main container
        reg_main = tk.Frame(reg_window, bg=COLORS['bg_secondary'])
        reg_main.pack(expand=True, fill='both', padx=40, pady=40)

        # Title
        tk.Label(
            reg_main,
            text="Create Account",
            font=FONTS['heading'],
            bg=COLORS['bg_secondary'],
            fg=COLORS['text_primary']
        ).pack(pady=(0, 20))

        # Form card
        form_card = tk.Frame(
            reg_main,
            bg=COLORS['bg_primary'],
            relief='flat',
            highlightbackground=COLORS['border'],
            highlightthickness=1
        )
        form_card.pack(fill='both', expand=True)

        form_content = tk.Frame(form_card, bg=COLORS['bg_primary'])
        form_content.pack(padx=40, pady=30)

        # Form fields
        fields = [
            ("Username", False),
            ("Password", True),
            ("First Name", False),
            ("Last Name", False),
            ("Email", False)
        ]

        entries = {}

        for field_name, is_password in fields:
            tk.Label(
                form_content,
                text=field_name,
                font=FONTS['body_bold'],
                bg=COLORS['bg_primary'],
                fg=COLORS['text_primary']
            ).pack(anchor='w', pady=(10, 5))

            entry = tk.Entry(
                form_content,
                show="●" if is_password else "",
                font=FONTS['body'],
                width=30,
                relief='solid',
                borderwidth=1,
                highlightthickness=2,
                highlightbackground=COLORS['border'],
                highlightcolor=COLORS['primary']
            )
            entry.pack(pady=(0, 5), ipady=8)
            entries[field_name] = entry

        def register_user():
            username = entries["Username"].get()
            password = entries["Password"].get()
            first_name = entries["First Name"].get()
            last_name = entries["Last Name"].get()
            email = entries["Email"].get()

            if auth_service.register(username, password, email, first_name, last_name):
                messagebox.showinfo("Success", "Registration successful! You can now sign in.")
                reg_window.destroy()
            else:
                messagebox.showerror("Error", "Registration failed. Username may already exist.")

        # Register button
        reg_btn = tk.Button(
            form_content,
            text="Create Account",
            command=register_user,
            font=FONTS['button_large'],
            bg=COLORS['success'],
            fg='white',
            activebackground=COLORS['success_dark'],
            activeforeground='white',
            relief='flat',
            cursor='hand2',
            width=25,
            height=2,
            borderwidth=0
        )
        reg_btn.pack(pady=(20, 0))

        def on_enter_reg(e):
            reg_btn.config(bg=COLORS['success_dark'])

        def on_leave_reg(e):
            reg_btn.config(bg=COLORS['success'])

        reg_btn.bind("<Enter>", on_enter_reg)
        reg_btn.bind("<Leave>", on_leave_reg)

    register_btn = tk.Label(
        register_frame,
        text="Sign up",
        font=FONTS['body_bold'],
        bg=COLORS['bg_primary'],
        fg=COLORS['primary'],
        cursor='hand2'
    )
    register_btn.pack(side='left')
    register_btn.bind("<Button-1>", lambda e: show_register_window())

    # Info text
    info_frame = tk.Frame(main_frame, bg=COLORS['bg_secondary'])
    info_frame.pack(pady=20)

    tk.Label(
        info_frame,
        text="💡 Default credentials: admin / 1234",
        font=FONTS['small'],
        bg=COLORS['bg_secondary'],
        fg=COLORS['text_secondary']
    ).pack()

    # Enter key bindings
    password_entry.bind('<Return>', lambda e: handle_login())
    username_entry.bind('<Return>', lambda e: password_entry.focus())

    # Focus username
    username_entry.focus()

    root.mainloop()


def show_main_dashboard():
    """Display the modern main dashboard"""
    main_app = tk.Tk()
    main_app.title("Learning Management System")
    main_app.geometry("1100x750")
    main_app.configure(bg=COLORS['bg_secondary'])

    # Center window
    main_app.update_idletasks()
    width = main_app.winfo_width()
    height = main_app.winfo_height()
    x = (main_app.winfo_screenwidth() // 2) - (width // 2)
    y = (main_app.winfo_screenheight() // 2) - (height // 2)
    main_app.geometry(f'{width}x{height}+{x}+{y}')

    # Header
    header = tk.Frame(main_app, bg=COLORS['bg_primary'], height=80)
    header.pack(fill='x', side='top')
    header.pack_propagate(False)

    header_content = tk.Frame(header, bg=COLORS['bg_primary'])
    header_content.pack(fill='both', expand=True, padx=40, pady=20)

    tk.Label(
        header_content,
        text=f"Welcome back, {current_user}! 👋",
        font=FONTS['title'],
        bg=COLORS['bg_primary'],
        fg=COLORS['text_primary']
    ).pack(side='left')

    logout_btn = tk.Button(
        header_content,
        text="🚪 Logout",
        command=lambda: logout(main_app),
        font=FONTS['button'],
        bg=COLORS['bg_tertiary'],
        fg=COLORS['text_primary'],
        activebackground=COLORS['border'],
        relief='flat',
        cursor='hand2',
        padx=20,
        pady=10,
        borderwidth=0
    )
    logout_btn.pack(side='right')

    # Main content area
    content = tk.Frame(main_app, bg=COLORS['bg_secondary'])
    content.pack(fill='both', expand=True, padx=40, pady=30)

    # Title
    tk.Label(
        content,
        text="Choose Your Learning Path",
        font=FONTS['heading'],
        bg=COLORS['bg_secondary'],
        fg=COLORS['text_primary']
    ).pack(pady=(0, 10))

    tk.Label(
        content,
        text="Select an option below to start your learning journey",
        font=FONTS['body'],
        bg=COLORS['bg_secondary'],
        fg=COLORS['text_secondary']
    ).pack(pady=(0, 30))

    # Cards grid
    cards_frame = tk.Frame(content, bg=COLORS['bg_secondary'])
    cards_frame.pack(expand=True)

    # Define dashboard cards
    dashboard_cards = [
        {
            'icon': '📚',
            'title': 'Student Pick Topic',
            'description': 'Choose your own learning topic and goals',
            'color': COLORS['success'],
            'command': lambda: show_student_pick(main_app)
        },
        {
            'icon': '🎲',
            'title': 'Computer Pick Topic',
            'description': 'Let AI select a topic for you',
            'color': COLORS['primary'],
            'command': lambda: handle_computer_pick(main_app)
        },
        {
            'icon': '📊',
            'title': 'View Progress',
            'description': 'Track your learning achievements',
            'color': COLORS['warning'],
            'command': lambda: show_progress_dashboard(main_app)
        }
    ]

    if AI_AVAILABLE:
        dashboard_cards.append({
            'icon': '🤖',
            'title': 'AI Practice Problems',
            'description': 'Practice with AI-generated problems',
            'color': COLORS['purple'],
            'command': lambda: show_ai_practice(main_app)
        })

    # Create cards in grid
    row, col = 0, 0
    for card_data in dashboard_cards:
        card = create_dashboard_card(
            cards_frame,
            card_data['icon'],
            card_data['title'],
            card_data['description'],
            card_data['color'],
            card_data['command']
        )
        card.grid(row=row, column=col, padx=15, pady=15, sticky='nsew')

        col += 1
        if col > 1:  # 2 columns
            col = 0
            row += 1

    # Configure grid weights
    for i in range(2):
        cards_frame.grid_columnconfigure(i, weight=1)

    main_app.mainloop()


def create_dashboard_card(parent, icon, title, description, color, command):
    """Create a modern dashboard card"""
    card = tk.Frame(
        parent,
        bg=COLORS['bg_primary'],
        relief='flat',
        highlightbackground=COLORS['border'],
        highlightthickness=1,
        cursor='hand2'
    )

    card_content = tk.Frame(card, bg=COLORS['bg_primary'])
    card_content.pack(padx=30, pady=30, fill='both', expand=True)

    # Icon
    tk.Label(
        card_content,
        text=icon,
        font=('Segoe UI', 48),
        bg=COLORS['bg_primary']
    ).pack(pady=(0, 15))

    # Title
    tk.Label(
        card_content,
        text=title,
        font=FONTS['subheading'],
        bg=COLORS['bg_primary'],
        fg=COLORS['text_primary']
    ).pack(pady=(0, 10))

    # Description
    tk.Label(
        card_content,
        text=description,
        font=FONTS['body'],
        bg=COLORS['bg_primary'],
        fg=COLORS['text_secondary'],
        wraplength=250
    ).pack(pady=(0, 20))

    # Button
    btn = tk.Button(
        card_content,
        text="Get Started →",
        command=command,
        font=FONTS['button'],
        bg=color,
        fg='white',
        activebackground=color,
        activeforeground='white',
        relief='flat',
        cursor='hand2',
        padx=25,
        pady=12,
        borderwidth=0
    )
    btn.pack()

    # Hover effects
    def on_enter(e):
        card.config(highlightbackground=color, highlightthickness=2)
        btn.config(bg=COLORS.get(color + '_dark', color))

    def on_leave(e):
        card.config(highlightbackground=COLORS['border'], highlightthickness=1)
        btn.config(bg=color)

    card.bind("<Enter>", on_enter)
    card.bind("<Leave>", on_leave)
    card_content.bind("<Enter>", on_enter)
    card_content.bind("<Leave>", on_leave)

    # Click on card
    def on_click(e):
        command()

    card.bind("<Button-1>", on_click)
    card_content.bind("<Button-1>", on_click)

    return card


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
    """Show modern topic selection screen"""
    for widget in window.winfo_children():
        widget.destroy()

    window.configure(bg=COLORS['bg_secondary'])

    # Header
    header = tk.Frame(window, bg=COLORS['bg_primary'], height=80)
    header.pack(fill='x', side='top')
    header.pack_propagate(False)

    header_content = tk.Frame(header, bg=COLORS['bg_primary'])
    header_content.pack(fill='both', expand=True, padx=40, pady=20)

    tk.Label(
        header_content,
        text="📚 Choose Your Topic",
        font=FONTS['title'],
        bg=COLORS['bg_primary'],
        fg=COLORS['text_primary']
    ).pack(side='left')

    back_btn = tk.Button(
        header_content,
        text="← Back",
        command=lambda: relaunch_dashboard(window),
        font=FONTS['button'],
        bg=COLORS['bg_tertiary'],
        fg=COLORS['text_primary'],
        activebackground=COLORS['border'],
        relief='flat',
        cursor='hand2',
        padx=20,
        pady=10,
        borderwidth=0
    )
    back_btn.pack(side='right')

    # Content
    content = tk.Frame(window, bg=COLORS['bg_secondary'])
    content.pack(fill='both', expand=True, padx=40, pady=30)

    tk.Label(
        content,
        text="Select a topic to explore learning goals",
        font=FONTS['body'],
        bg=COLORS['bg_secondary'],
        fg=COLORS['text_secondary']
    ).pack(pady=(0, 20))

    topics = fetch_all_topics()
    if not topics:
        messagebox.showinfo("No Topics", "No topics found in the database.")
        relaunch_dashboard(window)
        return

    # Topics list
    topics_frame = tk.Frame(content, bg=COLORS['bg_secondary'])
    topics_frame.pack(fill='both', expand=True)

    for _, topic_name in topics:
        topic_card = tk.Frame(
            topics_frame,
            bg=COLORS['bg_primary'],
            relief='flat',
            highlightbackground=COLORS['border'],
            highlightthickness=1,
            cursor='hand2'
        )
        topic_card.pack(fill='x', pady=8)

        topic_btn = tk.Button(
            topic_card,
            text=f"  {topic_name}",
            command=lambda t=topic_name: show_goals_for_topic(window, t),
            font=FONTS['subheading'],
            bg=COLORS['bg_primary'],
            fg=COLORS['text_primary'],
            activebackground=COLORS['bg_tertiary'],
            activeforeground=COLORS['text_primary'],
            relief='flat',
            cursor='hand2',
            anchor='w',
            padx=30,
            pady=20,
            borderwidth=0
        )
        topic_btn.pack(fill='x')

        # Hover effect
        def make_hover(card, btn, t_name):
            def on_enter(e):
                card.config(highlightbackground=COLORS['primary'], highlightthickness=2)
                btn.config(bg=COLORS['bg_tertiary'])

            def on_leave(e):
                card.config(highlightbackground=COLORS['border'], highlightthickness=1)
                btn.config(bg=COLORS['bg_primary'])

            card.bind("<Enter>", on_enter)
            card.bind("<Leave>", on_leave)
            btn.bind("<Enter>", on_enter)
            btn.bind("<Leave>", on_leave)

        make_hover(topic_card, topic_btn, topic_name)


def handle_computer_pick(window):
    """Randomly select a topic"""
    topic = fetch_random_topic()
    if topic:
        topic_id, topic_name = topic
        show_goals_for_topic(window, topic_name)
    else:
        messagebox.showinfo("No Topics", "No topics available to choose from.")


def show_goals_for_topic(window, topic_name):
    """Show modern goals screen for selected topic"""
    for widget in window.winfo_children():
        widget.destroy()

    window.configure(bg=COLORS['bg_secondary'])

    # Header
    header = tk.Frame(window, bg=COLORS['bg_primary'], height=80)
    header.pack(fill='x', side='top')
    header.pack_propagate(False)

    header_content = tk.Frame(header, bg=COLORS['bg_primary'])
    header_content.pack(fill='both', expand=True, padx=40, pady=20)

    tk.Label(
        header_content,
        text=f"📖 {topic_name}",
        font=FONTS['title'],
        bg=COLORS['bg_primary'],
        fg=COLORS['text_primary']
    ).pack(side='left')

    back_btn = tk.Button(
        header_content,
        text="← Back",
        command=lambda: show_student_pick(window),
        font=FONTS['button'],
        bg=COLORS['bg_tertiary'],
        fg=COLORS['text_primary'],
        activebackground=COLORS['border'],
        relief='flat',
        cursor='hand2',
        padx=20,
        pady=10,
        borderwidth=0
    )
    back_btn.pack(side='right')

    goals = fetch_goals_for_topic(topic_name)
    if not goals:
        messagebox.showinfo("No Goals", f"No goals found for topic '{topic_name}'.")
        relaunch_dashboard(window)
        return

    goal_index = [0]

    # Content area
    content = tk.Frame(window, bg=COLORS['bg_secondary'])
    content.pack(fill='both', expand=True, padx=40, pady=30)

    # Goal card
    goal_card = tk.Frame(
        content,
        bg=COLORS['bg_primary'],
        relief='flat',
        highlightbackground=COLORS['border'],
        highlightthickness=1
    )
    goal_card.pack(fill='both', expand=True)

    card_content = tk.Frame(goal_card, bg=COLORS['bg_primary'])
    card_content.pack(padx=40, pady=40, fill='both', expand=True)

    # Goal counter
    goal_counter = tk.Label(
        card_content,
        text="",
        font=FONTS['body'],
        bg=COLORS['bg_primary'],
        fg=COLORS['text_secondary']
    )
    goal_counter.pack(anchor='w', pady=(0, 10))

    # Goal title
    goal_title_label = tk.Label(
        card_content,
        text="",
        font=FONTS['heading'],
        bg=COLORS['bg_primary'],
        fg=COLORS['text_primary'],
        wraplength=900,
        justify='left'
    )
    goal_title_label.pack(anchor='w', pady=(0, 15))

    # Goal description
    goal_desc_label = tk.Label(
        card_content,
        text="",
        font=FONTS['body'],
        bg=COLORS['bg_primary'],
        fg=COLORS['text_secondary'],
        wraplength=900,
        justify='left'
    )
    goal_desc_label.pack(anchor='w', pady=(0, 25))

    # Objectives section
    objectives_container = tk.Frame(card_content, bg=COLORS['bg_tertiary'])
    objectives_container.pack(fill='both', expand=True, pady=(10, 0))

    objectives_frame = tk.Frame(objectives_container, bg=COLORS['bg_tertiary'])
    objectives_frame.pack(padx=25, pady=25, fill='both', expand=True)

    def update_goal():
        if goal_index[0] < len(goals):
            goal_id, goal_title, goal_desc = goals[goal_index[0]]

            goal_counter.config(text=f"Goal {goal_index[0] + 1} of {len(goals)}")
            goal_title_label.config(text=goal_title)
            goal_desc_label.config(text=goal_desc)

            # Clear objectives
            for widget in objectives_frame.winfo_children():
                widget.destroy()

            # Show objectives
            objectives = fetch_objectives_for_goal(goal_id)
            if objectives:
                tk.Label(
                    objectives_frame,
                    text="📋 Learning Objectives",
                    font=FONTS['subheading'],
                    bg=COLORS['bg_tertiary'],
                    fg=COLORS['text_primary']
                ).pack(anchor='w', pady=(0, 15))

                for _, obj_title, _ in objectives:
                    obj_frame = tk.Frame(objectives_frame, bg=COLORS['bg_tertiary'])
                    obj_frame.pack(fill='x', pady=5)

                    tk.Label(
                        obj_frame,
                        text="✓",
                        font=FONTS['body_bold'],
                        bg=COLORS['bg_tertiary'],
                        fg=COLORS['success']
                    ).pack(side='left', padx=(0, 10))

                    tk.Label(
                        obj_frame,
                        text=obj_title,
                        font=FONTS['body'],
                        bg=COLORS['bg_tertiary'],
                        fg=COLORS['text_primary'],
                        wraplength=800,
                        justify='left'
                    ).pack(side='left', anchor='w')

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

    # Navigation buttons
    nav_frame = tk.Frame(content, bg=COLORS['bg_secondary'])
    nav_frame.pack(pady=(20, 0))

    # Previous button
    prev_btn = tk.Button(
        nav_frame,
        text="← Previous",
        command=prev_goal,
        font=FONTS['button'],
        bg=COLORS['bg_tertiary'],
        fg=COLORS['text_primary'],
        activebackground=COLORS['border'],
        relief='flat',
        cursor='hand2',
        padx=20,
        pady=12,
        borderwidth=0
    )
    prev_btn.grid(row=0, column=0, padx=10)

    # Practice button
    practice_btn = tk.Button(
        nav_frame,
        text="📝 Practice Problems",
        command=lambda: show_practice_for_goal(window, topic_name, goals[goal_index[0]][0]),
        font=FONTS['button'],
        bg=COLORS['success'],
        fg='white',
        activebackground=COLORS['success_dark'],
        activeforeground='white',
        relief='flat',
        cursor='hand2',
        padx=25,
        pady=12,
        borderwidth=0
    )
    practice_btn.grid(row=0, column=1, padx=10)

    # Next button
    next_btn = tk.Button(
        nav_frame,
        text="Next →",
        command=next_goal,
        font=FONTS['button'],
        bg=COLORS['primary'],
        fg='white',
        activebackground=COLORS['primary_dark'],
        activeforeground='white',
        relief='flat',
        cursor='hand2',
        padx=20,
        pady=12,
        borderwidth=0
    )
    next_btn.grid(row=0, column=2, padx=10)


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
            model='gemini-2.5-flash',
            contents=prompt
        )
        return response.text
    except Exception as e:
        error_msg = str(e)

        # Check for specific error types
        if "429" in error_msg or "RESOURCE_EXHAUSTED" in error_msg:
            return """⚠️ API Rate Limit Reached

The AI service has reached its usage limit. This can happen when:
• Too many requests are made in a short time
• Daily/monthly quota has been exhausted

💡 Solutions:
1. Wait a few minutes and try again
2. Get a new API key from: https://aistudio.google.com/app/apikey
3. Update the API key in unified_app.py (line 26)

📝 Manual Feedback:
In the meantime, here's what you should focus on:
• Review the correct answer: """ + str(correct_answer) + """
• Compare it with your answer: """ + str(student_answer) + """
• """ + ("Great job! You got it right! ✓" if is_correct else "Try to understand where the difference is and why the correct answer works.") + """

For detailed help, consult your textbook or ask your instructor."""

        return f"Could not generate AI feedback: {error_msg}"


def show_ai_feedback_dialog(problem_text, student_answer, correct_answer, is_correct):
    """Show modern AI feedback dialog"""
    feedback_window = tk.Toplevel()
    feedback_window.title("AI Tutor Feedback")
    feedback_window.geometry("800x700")
    feedback_window.configure(bg=COLORS['bg_secondary'])

    # Center window
    feedback_window.update_idletasks()
    width = feedback_window.winfo_width()
    height = feedback_window.winfo_height()
    x = (feedback_window.winfo_screenwidth() // 2) - (width // 2)
    y = (feedback_window.winfo_screenheight() // 2) - (height // 2)
    feedback_window.geometry(f'{width}x{height}+{x}+{y}')

    # Header with result
    header_color = COLORS['success'] if is_correct else COLORS['danger']
    header = tk.Frame(feedback_window, bg=header_color, height=80)
    header.pack(fill='x')
    header.pack_propagate(False)

    header_content = tk.Frame(header, bg=header_color)
    header_content.pack(expand=True, fill='both', padx=40, pady=20)

    result_icon = "✓" if is_correct else "✗"
    result_text = "Correct Answer!" if is_correct else "Incorrect Answer"

    tk.Label(
        header_content,
        text=f"{result_icon} {result_text}",
        font=FONTS['title'],
        bg=header_color,
        fg='white'
    ).pack()

    # Content area
    content = tk.Frame(feedback_window, bg=COLORS['bg_secondary'])
    content.pack(fill='both', expand=True, padx=40, pady=30)

    # Problem card
    problem_card = tk.Frame(
        content,
        bg=COLORS['bg_primary'],
        relief='flat',
        highlightbackground=COLORS['border'],
        highlightthickness=1
    )
    problem_card.pack(fill='x', pady=(0, 15))

    problem_content = tk.Frame(problem_card, bg=COLORS['bg_primary'])
    problem_content.pack(padx=25, pady=20)

    tk.Label(
        problem_content,
        text="📝 Problem",
        font=FONTS['subheading'],
        bg=COLORS['bg_primary'],
        fg=COLORS['text_primary']
    ).pack(anchor='w', pady=(0, 10))

    tk.Label(
        problem_content,
        text=problem_text,
        font=FONTS['body'],
        bg=COLORS['bg_tertiary'],
        fg=COLORS['text_primary'],
        wraplength=700,
        justify='left',
        padx=15,
        pady=15
    ).pack(fill='x')

    # Answers card
    answers_card = tk.Frame(
        content,
        bg=COLORS['bg_primary'],
        relief='flat',
        highlightbackground=COLORS['border'],
        highlightthickness=1
    )
    answers_card.pack(fill='x', pady=(0, 15))

    answers_content = tk.Frame(answers_card, bg=COLORS['bg_primary'])
    answers_content.pack(padx=25, pady=20)

    # Your answer
    tk.Label(
        answers_content,
        text="Your Answer:",
        font=FONTS['body_bold'],
        bg=COLORS['bg_primary'],
        fg=COLORS['text_primary']
    ).pack(anchor='w', pady=(0, 5))

    tk.Label(
        answers_content,
        text=student_answer,
        font=FONTS['body'],
        bg=COLORS['bg_tertiary'],
        fg=COLORS['text_primary'],
        wraplength=700,
        justify='left',
        padx=15,
        pady=10
    ).pack(fill='x', pady=(0, 15))

    # Correct answer
    tk.Label(
        answers_content,
        text="Correct Answer:",
        font=FONTS['body_bold'],
        bg=COLORS['bg_primary'],
        fg=COLORS['text_primary']
    ).pack(anchor='w', pady=(0, 5))

    tk.Label(
        answers_content,
        text=correct_answer,
        font=FONTS['body'],
        bg=COLORS['success'] if is_correct else COLORS['bg_tertiary'],
        fg='white' if is_correct else COLORS['text_primary'],
        wraplength=700,
        justify='left',
        padx=15,
        pady=10
    ).pack(fill='x')

    # AI Feedback card
    feedback_card = tk.Frame(
        content,
        bg=COLORS['bg_primary'],
        relief='flat',
        highlightbackground=COLORS['border'],
        highlightthickness=1
    )
    feedback_card.pack(fill='both', expand=True)

    feedback_content = tk.Frame(feedback_card, bg=COLORS['bg_primary'])
    feedback_content.pack(padx=25, pady=20, fill='both', expand=True)

    tk.Label(
        feedback_content,
        text="🤖 AI Tutor Feedback",
        font=FONTS['subheading'],
        bg=COLORS['bg_primary'],
        fg=COLORS['text_primary']
    ).pack(anchor='w', pady=(0, 10))

    # Feedback text area with scrollbar
    text_frame = tk.Frame(feedback_content, bg=COLORS['bg_primary'])
    text_frame.pack(fill='both', expand=True)

    scrollbar = tk.Scrollbar(text_frame)
    scrollbar.pack(side='right', fill='y')

    feedback_text = tk.Text(
        text_frame,
        font=FONTS['body'],
        wrap='word',
        bg=COLORS['bg_tertiary'],
        fg=COLORS['text_primary'],
        padx=15,
        pady=15,
        relief='flat',
        yscrollcommand=scrollbar.set,
        borderwidth=0
    )
    feedback_text.pack(side='left', fill='both', expand=True)
    scrollbar.config(command=feedback_text.yview)

    # Show loading
    feedback_text.insert(1.0, "⏳ Generating AI feedback... Please wait...")
    feedback_text.config(state='disabled')
    feedback_window.update()

    # Generate feedback
    feedback = get_ai_feedback(problem_text, student_answer, correct_answer, is_correct)

    feedback_text.config(state='normal')
    feedback_text.delete(1.0, tk.END)
    feedback_text.insert(1.0, feedback)
    feedback_text.config(state='disabled')

    # Close button
    button_frame = tk.Frame(content, bg=COLORS['bg_secondary'])
    button_frame.pack(pady=(15, 0))

    close_btn = tk.Button(
        button_frame,
        text="Close",
        command=feedback_window.destroy,
        font=FONTS['button_large'],
        bg=COLORS['primary'],
        fg='white',
        activebackground=COLORS['primary_dark'],
        activeforeground='white',
        relief='flat',
        cursor='hand2',
        padx=40,
        pady=12,
        borderwidth=0
    )
    close_btn.pack()

    def on_enter(e):
        close_btn.config(bg=COLORS['primary_dark'])

    def on_leave(e):
        close_btn.config(bg=COLORS['primary'])

    close_btn.bind("<Enter>", on_enter)
    close_btn.bind("<Leave>", on_leave)


def show_ai_feedback_dialog_with_next(problem_text, student_answer, correct_answer, is_correct, next_callback):
    """Show modern AI feedback dialog with Next Problem button"""
    feedback_window = tk.Toplevel()
    feedback_window.title("AI Tutor Feedback")
    feedback_window.geometry("800x700")
    feedback_window.configure(bg=COLORS['bg_secondary'])

    # Center window
    feedback_window.update_idletasks()
    width = feedback_window.winfo_width()
    height = feedback_window.winfo_height()
    x = (feedback_window.winfo_screenwidth() // 2) - (width // 2)
    y = (feedback_window.winfo_screenheight() // 2) - (height // 2)
    feedback_window.geometry(f'{width}x{height}+{x}+{y}')

    # Header with result
    header_color = COLORS['success'] if is_correct else COLORS['danger']
    header = tk.Frame(feedback_window, bg=header_color, height=80)
    header.pack(fill='x')
    header.pack_propagate(False)

    header_content = tk.Frame(header, bg=header_color)
    header_content.pack(expand=True, fill='both', padx=40, pady=20)

    result_icon = "✓" if is_correct else "✗"
    result_text = "Correct Answer!" if is_correct else "Incorrect Answer"

    tk.Label(
        header_content,
        text=f"{result_icon} {result_text}",
        font=FONTS['title'],
        bg=header_color,
        fg='white'
    ).pack()

    # Content area
    content = tk.Frame(feedback_window, bg=COLORS['bg_secondary'])
    content.pack(fill='both', expand=True, padx=40, pady=30)

    # Problem card
    problem_card = tk.Frame(
        content,
        bg=COLORS['bg_primary'],
        relief='flat',
        highlightbackground=COLORS['border'],
        highlightthickness=1
    )
    problem_card.pack(fill='x', pady=(0, 15))

    problem_content = tk.Frame(problem_card, bg=COLORS['bg_primary'])
    problem_content.pack(padx=25, pady=20)

    tk.Label(
        problem_content,
        text="📝 Problem",
        font=FONTS['subheading'],
        bg=COLORS['bg_primary'],
        fg=COLORS['text_primary']
    ).pack(anchor='w', pady=(0, 10))

    tk.Label(
        problem_content,
        text=problem_text,
        font=FONTS['body'],
        bg=COLORS['bg_tertiary'],
        fg=COLORS['text_primary'],
        wraplength=700,
        justify='left',
        padx=15,
        pady=15
    ).pack(fill='x')

    # Answers card
    answers_card = tk.Frame(
        content,
        bg=COLORS['bg_primary'],
        relief='flat',
        highlightbackground=COLORS['border'],
        highlightthickness=1
    )
    answers_card.pack(fill='x', pady=(0, 15))

    answers_content = tk.Frame(answers_card, bg=COLORS['bg_primary'])
    answers_content.pack(padx=25, pady=20)

    # Your answer
    tk.Label(
        answers_content,
        text="Your Answer:",
        font=FONTS['body_bold'],
        bg=COLORS['bg_primary'],
        fg=COLORS['text_primary']
    ).pack(anchor='w', pady=(0, 5))

    tk.Label(
        answers_content,
        text=student_answer,
        font=FONTS['body'],
        bg=COLORS['bg_tertiary'],
        fg=COLORS['text_primary'],
        wraplength=700,
        justify='left',
        padx=15,
        pady=10
    ).pack(fill='x', pady=(0, 15))

    # Correct answer
    tk.Label(
        answers_content,
        text="Correct Answer:",
        font=FONTS['body_bold'],
        bg=COLORS['bg_primary'],
        fg=COLORS['text_primary']
    ).pack(anchor='w', pady=(0, 5))

    tk.Label(
        answers_content,
        text=correct_answer,
        font=FONTS['body'],
        bg=COLORS['success'] if is_correct else COLORS['bg_tertiary'],
        fg='white' if is_correct else COLORS['text_primary'],
        wraplength=700,
        justify='left',
        padx=15,
        pady=10
    ).pack(fill='x')

    # AI Feedback card
    feedback_card = tk.Frame(
        content,
        bg=COLORS['bg_primary'],
        relief='flat',
        highlightbackground=COLORS['border'],
        highlightthickness=1
    )
    feedback_card.pack(fill='both', expand=True)

    feedback_content = tk.Frame(feedback_card, bg=COLORS['bg_primary'])
    feedback_content.pack(padx=25, pady=20, fill='both', expand=True)

    tk.Label(
        feedback_content,
        text="🤖 AI Tutor Feedback",
        font=FONTS['subheading'],
        bg=COLORS['bg_primary'],
        fg=COLORS['text_primary']
    ).pack(anchor='w', pady=(0, 10))

    # Feedback text area with scrollbar
    text_frame = tk.Frame(feedback_content, bg=COLORS['bg_primary'])
    text_frame.pack(fill='both', expand=True)

    scrollbar = tk.Scrollbar(text_frame)
    scrollbar.pack(side='right', fill='y')

    feedback_text = tk.Text(
        text_frame,
        font=FONTS['body'],
        wrap='word',
        bg=COLORS['bg_tertiary'],
        fg=COLORS['text_primary'],
        padx=15,
        pady=15,
        relief='flat',
        yscrollcommand=scrollbar.set,
        borderwidth=0
    )
    feedback_text.pack(side='left', fill='both', expand=True)
    scrollbar.config(command=feedback_text.yview)

    # Show loading
    feedback_text.insert(1.0, "⏳ Generating AI feedback... Please wait...")
    feedback_text.config(state='disabled')
    feedback_window.update()

    # Generate feedback
    feedback = get_ai_feedback(problem_text, student_answer, correct_answer, is_correct)

    feedback_text.config(state='normal')
    feedback_text.delete(1.0, tk.END)
    feedback_text.insert(1.0, feedback)
    feedback_text.config(state='disabled')

    # Buttons
    button_frame = tk.Frame(content, bg=COLORS['bg_secondary'])
    button_frame.pack(pady=(15, 0))

    def close_and_next():
        feedback_window.destroy()
        next_callback()

    next_btn = tk.Button(
        button_frame,
        text="→ Next Problem",
        command=close_and_next,
        font=FONTS['button_large'],
        bg=COLORS['success'],
        fg='white',
        activebackground=COLORS['success_dark'],
        activeforeground='white',
        relief='flat',
        cursor='hand2',
        padx=40,
        pady=12,
        borderwidth=0
    )
    next_btn.grid(row=0, column=0, padx=10)

    close_btn = tk.Button(
        button_frame,
        text="Close",
        command=feedback_window.destroy,
        font=FONTS['button_large'],
        bg=COLORS['primary'],
        fg='white',
        activebackground=COLORS['primary_dark'],
        activeforeground='white',
        relief='flat',
        cursor='hand2',
        padx=40,
        pady=12,
        borderwidth=0
    )
    close_btn.grid(row=0, column=1, padx=10)

    def make_hover(btn, normal_color, hover_color):
        def on_enter(e):
            btn.config(bg=hover_color)
        def on_leave(e):
            btn.config(bg=normal_color)
        btn.bind("<Enter>", on_enter)
        btn.bind("<Leave>", on_leave)

    make_hover(next_btn, COLORS['success'], COLORS['success_dark'])
    make_hover(close_btn, COLORS['primary'], COLORS['primary_dark'])


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


def show_practice_for_goal(window, topic_name, goal_id, start_objective_index=0, mode='choice'):
    """Show practice problems for a specific goal - BRD compliant with objective progression

    Args:
        mode: 'choice' = show tutoring vs practice choice
              'tutoring' = full instruction sequence
              'practice' = skip to practice problems
    """
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

    # Get all objectives for this goal
    objectives = fetch_objectives_for_goal(goal_id)
    if not objectives:
        messagebox.showinfo("No Objectives", "No learning objectives found for this goal.")
        show_goals_for_topic(window, topic_name)
        return

    # Start with the specified objective (default is first one)
    if start_objective_index >= len(objectives):
        # All objectives completed - show completion message
        messagebox.showinfo(
            "Goal Complete!",
            f"Congratulations! You've completed all learning objectives for '{goal_title}'!\n\n"
            f"You practiced {len(objectives)} objectives."
        )
        show_goals_for_topic(window, topic_name)
        return

    # Get current objective
    obj_id, obj_title, obj_desc = objectives[start_objective_index]

    # BRD Requirement: Student Pick mode - give choice between tutoring or practice
    if mode == 'choice':
        show_tutoring_choice(window, topic_name, topic_id, goal_id, goal_title, objectives, start_objective_index)
    elif mode == 'tutoring':
        # Full tutoring sequence: Direct Instruction → Walkthrough → Practice
        show_direct_instruction(window, topic_name, topic_id, goal_id, goal_title, objectives, start_objective_index)
    elif mode == 'practice':
        # Skip to practice problems
        start_objective_practice_session(
            window,
            topic_name,
            topic_id,
            goal_id,
            goal_title,
            objectives,
            start_objective_index
        )


def show_tutoring_choice(window, topic_name, topic_id, goal_id, goal_title, objectives, objective_index):
    """BRD Requirement: Give student choice between full tutoring or skip to practice"""
    for widget in window.winfo_children():
        widget.destroy()

    window.configure(bg=COLORS['bg_secondary'])

    obj_id, obj_title, obj_desc = objectives[objective_index]

    # Header
    header = tk.Frame(window, bg=COLORS['bg_primary'], height=100)
    header.pack(fill='x', side='top')
    header.pack_propagate(False)

    header_content = tk.Frame(header, bg=COLORS['bg_primary'])
    header_content.pack(fill='both', expand=True, padx=40, pady=20)

    tk.Label(
        header_content,
        text=f"📖 {goal_title}",
        font=FONTS['title'],
        bg=COLORS['bg_primary'],
        fg=COLORS['text_primary']
    ).pack(side='left')

    tk.Button(
        header_content,
        text="← Back",
        command=lambda: show_goals_for_topic(window, topic_name),
        font=FONTS['button'],
        bg=COLORS['bg_tertiary'],
        fg=COLORS['text_primary'],
        activebackground=COLORS['border'],
        relief='flat',
        cursor='hand2',
        padx=20,
        pady=10
    ).pack(side='right')

    # Content
    content = tk.Frame(window, bg=COLORS['bg_secondary'])
    content.pack(fill='both', expand=True, padx=60, pady=40)

    # Objective info
    tk.Label(
        content,
        text=f"Learning Objective {objective_index + 1} of {len(objectives)}",
        font=FONTS['body'],
        bg=COLORS['bg_secondary'],
        fg=COLORS['text_secondary']
    ).pack(pady=(0, 10))

    tk.Label(
        content,
        text=obj_title,
        font=FONTS['heading'],
        bg=COLORS['bg_secondary'],
        fg=COLORS['text_primary'],
        wraplength=700
    ).pack(pady=(0, 30))

    # Choice message
    tk.Label(
        content,
        text="How would you like to learn this objective?",
        font=FONTS['subheading'],
        bg=COLORS['bg_secondary'],
        fg=COLORS['text_primary']
    ).pack(pady=(20, 40))

    # Choice cards
    cards_frame = tk.Frame(content, bg=COLORS['bg_secondary'])
    cards_frame.pack(expand=True)

    # Tutoring card (full instruction)
    tutoring_card = create_card(cards_frame)
    tutoring_card.pack(side='left', padx=20)

    tk.Label(
        tutoring_card,
        text="📚",
        font=('Segoe UI', 48),
        bg=COLORS['bg_primary']
    ).pack(pady=(20, 10))

    tk.Label(
        tutoring_card,
        text="Full Tutoring",
        font=FONTS['heading'],
        bg=COLORS['bg_primary'],
        fg=COLORS['text_primary']
    ).pack(pady=(0, 10))

    tk.Label(
        tutoring_card,
        text="Learn with:\n• Direct Instruction\n• Walkthrough Examples\n• Practice Problems",
        font=FONTS['body'],
        bg=COLORS['bg_primary'],
        fg=COLORS['text_secondary'],
        justify='left'
    ).pack(pady=(0, 20))

    tk.Button(
        tutoring_card,
        text="Start Tutoring",
        command=lambda: show_practice_for_goal(window, topic_name, goal_id, objective_index, 'tutoring'),
        font=FONTS['button_large'],
        bg=COLORS['primary'],
        fg='white',
        activebackground=COLORS['primary_dark'],
        relief='flat',
        cursor='hand2',
        padx=30,
        pady=15
    ).pack(pady=(0, 20))

    # Practice card (skip to practice)
    practice_card = create_card(cards_frame)
    practice_card.pack(side='left', padx=20)

    tk.Label(
        practice_card,
        text="🎯",
        font=('Segoe UI', 48),
        bg=COLORS['bg_primary']
    ).pack(pady=(20, 10))

    tk.Label(
        practice_card,
        text="Practice Only",
        font=FONTS['heading'],
        bg=COLORS['bg_primary'],
        fg=COLORS['text_primary']
    ).pack(pady=(0, 10))

    tk.Label(
        practice_card,
        text="Skip instruction and:\n• Go straight to practice\n• Minimum 20 problems\n• Achieve 90% mastery",
        font=FONTS['body'],
        bg=COLORS['bg_primary'],
        fg=COLORS['text_secondary'],
        justify='left'
    ).pack(pady=(0, 20))

    tk.Button(
        practice_card,
        text="Start Practice",
        command=lambda: show_practice_for_goal(window, topic_name, goal_id, objective_index, 'practice'),
        font=FONTS['button_large'],
        bg=COLORS['success'],
        fg='white',
        activebackground=COLORS['success_dark'],
        relief='flat',
        cursor='hand2',
        padx=30,
        pady=15
    ).pack(pady=(0, 20))


def show_direct_instruction(window, topic_name, topic_id, goal_id, goal_title, objectives, objective_index):
    """BRD Section 4: Direct Instruction - Show learning material with graphics and text"""
    for widget in window.winfo_children():
        widget.destroy()

    window.configure(bg=COLORS['bg_secondary'])

    obj_id, obj_title, obj_desc = objectives[objective_index]

    # Header
    header = tk.Frame(window, bg=COLORS['primary'], height=100)
    header.pack(fill='x', side='top')
    header.pack_propagate(False)

    header_content = tk.Frame(header, bg=COLORS['primary'])
    header_content.pack(fill='both', expand=True, padx=40, pady=20)

    tk.Label(
        header_content,
        text=f"📖 Direct Instruction",
        font=FONTS['title'],
        bg=COLORS['primary'],
        fg='white'
    ).pack(side='left')

    tk.Label(
        header_content,
        text=f"Objective {objective_index + 1} of {len(objectives)}",
        font=FONTS['body'],
        bg=COLORS['primary'],
        fg='white'
    ).pack(side='right')

    # Content area with scrollbar
    content_frame = tk.Frame(window, bg=COLORS['bg_secondary'])
    content_frame.pack(fill='both', expand=True)

    canvas = tk.Canvas(content_frame, bg=COLORS['bg_secondary'], highlightthickness=0)
    scrollbar = tk.Scrollbar(content_frame, orient='vertical', command=canvas.yview)
    scrollable_frame = tk.Frame(canvas, bg=COLORS['bg_secondary'])

    scrollable_frame.bind(
        "<Configure>",
        lambda e: canvas.configure(scrollregion=canvas.bbox("all"))
    )

    canvas.create_window((0, 0), window=scrollable_frame, anchor='nw')
    canvas.configure(yscrollcommand=scrollbar.set)

    canvas.pack(side='left', fill='both', expand=True, padx=40, pady=30)
    scrollbar.pack(side='right', fill='y')

    # Objective title
    tk.Label(
        scrollable_frame,
        text=obj_title,
        font=FONTS['heading'],
        bg=COLORS['bg_secondary'],
        fg=COLORS['text_primary'],
        wraplength=700
    ).pack(pady=(0, 20), anchor='w')

    # Instruction content card
    instruction_card = create_card(scrollable_frame)
    instruction_card.pack(fill='both', pady=(0, 30))

    # AI-generated instruction content
    instruction_text = tk.Text(
        instruction_card,
        font=FONTS['body'],
        wrap='word',
        bg=COLORS['bg_primary'],
        fg=COLORS['text_primary'],
        padx=30,
        pady=25,
        relief='flat',
        height=15,
        borderwidth=0
    )
    instruction_text.pack(fill='both', expand=True)

    # Generate AI instruction content
    if AI_AVAILABLE:
        instruction_text.insert(1.0, "⏳ Generating instructional content... Please wait...")
        window.update()

        instruction_content = generate_instruction_content(obj_title, obj_desc)
        instruction_text.delete(1.0, tk.END)
        instruction_text.insert(1.0, instruction_content)
    else:
        instruction_text.insert(1.0, f"Learning Objective: {obj_title}\n\n{obj_desc}\n\n"
                                     "This section would contain detailed instructional content explaining the concept.")

    instruction_text.config(state='disabled')

    # Navigation buttons
    button_frame = tk.Frame(window, bg=COLORS['bg_secondary'])
    button_frame.pack(fill='x', padx=40, pady=(0, 30))

    tk.Button(
        button_frame,
        text="← Back",
        command=lambda: show_practice_for_goal(window, topic_name, goal_id, objective_index, 'choice'),
        font=FONTS['button_large'],
        bg=COLORS['bg_tertiary'],
        fg=COLORS['text_primary'],
        activebackground=COLORS['border'],
        relief='flat',
        cursor='hand2',
        padx=25,
        pady=15
    ).pack(side='left')

    tk.Button(
        button_frame,
        text="Next: Walkthrough Example →",
        command=lambda: show_walkthrough(window, topic_name, topic_id, goal_id, goal_title, objectives, objective_index),
        font=FONTS['button_large'],
        bg=COLORS['primary'],
        fg='white',
        activebackground=COLORS['primary_dark'],
        relief='flat',
        cursor='hand2',
        padx=30,
        pady=15
    ).pack(side='right')


def show_walkthrough(window, topic_name, topic_id, goal_id, goal_title, objectives, objective_index):
    """BRD Section 5: Walkthrough Problem Solving - Show step-by-step example"""
    for widget in window.winfo_children():
        widget.destroy()

    window.configure(bg=COLORS['bg_secondary'])

    obj_id, obj_title, obj_desc = objectives[objective_index]

    # Header
    header = tk.Frame(window, bg=COLORS['warning'], height=100)
    header.pack(fill='x', side='top')
    header.pack_propagate(False)

    header_content = tk.Frame(header, bg=COLORS['warning'])
    header_content.pack(fill='both', expand=True, padx=40, pady=20)

    tk.Label(
        header_content,
        text=f"🔧 Walkthrough Example",
        font=FONTS['title'],
        bg=COLORS['warning'],
        fg='white'
    ).pack(side='left')

    tk.Label(
        header_content,
        text=f"Objective {objective_index + 1} of {len(objectives)}",
        font=FONTS['body'],
        bg=COLORS['warning'],
        fg='white'
    ).pack(side='right')

    # Content area with scrollbar
    content_frame = tk.Frame(window, bg=COLORS['bg_secondary'])
    content_frame.pack(fill='both', expand=True)

    canvas = tk.Canvas(content_frame, bg=COLORS['bg_secondary'], highlightthickness=0)
    scrollbar = tk.Scrollbar(content_frame, orient='vertical', command=canvas.yview)
    scrollable_frame = tk.Frame(canvas, bg=COLORS['bg_secondary'])

    scrollable_frame.bind(
        "<Configure>",
        lambda e: canvas.configure(scrollregion=canvas.bbox("all"))
    )

    canvas.create_window((0, 0), window=scrollable_frame, anchor='nw')
    canvas.configure(yscrollcommand=scrollbar.set)

    canvas.pack(side='left', fill='both', expand=True, padx=40, pady=30)
    scrollbar.pack(side='right', fill='y')

    # Objective title
    tk.Label(
        scrollable_frame,
        text=obj_title,
        font=FONTS['heading'],
        bg=COLORS['bg_secondary'],
        fg=COLORS['text_primary'],
        wraplength=700
    ).pack(pady=(0, 20), anchor='w')

    # Walkthrough content card
    walkthrough_card = create_card(scrollable_frame)
    walkthrough_card.pack(fill='both', pady=(0, 30))

    # AI-generated walkthrough content
    walkthrough_text = tk.Text(
        walkthrough_card,
        font=FONTS['body'],
        wrap='word',
        bg=COLORS['bg_primary'],
        fg=COLORS['text_primary'],
        padx=30,
        pady=25,
        relief='flat',
        height=20,
        borderwidth=0
    )
    walkthrough_text.pack(fill='both', expand=True)

    # Generate AI walkthrough content
    if AI_AVAILABLE:
        walkthrough_text.insert(1.0, "⏳ Generating walkthrough example... Please wait...")
        window.update()

        walkthrough_content = generate_walkthrough_content(obj_title, obj_desc)
        walkthrough_text.delete(1.0, tk.END)
        walkthrough_text.insert(1.0, walkthrough_content)
    else:
        walkthrough_text.insert(1.0, f"Walkthrough Example for: {obj_title}\n\n"
                                      "This section would contain a step-by-step example problem with detailed solution.")

    walkthrough_text.config(state='disabled')

    # Navigation buttons
    button_frame = tk.Frame(window, bg=COLORS['bg_secondary'])
    button_frame.pack(fill='x', padx=40, pady=(0, 30))

    tk.Button(
        button_frame,
        text="← Back to Instruction",
        command=lambda: show_direct_instruction(window, topic_name, topic_id, goal_id, goal_title, objectives, objective_index),
        font=FONTS['button_large'],
        bg=COLORS['bg_tertiary'],
        fg=COLORS['text_primary'],
        activebackground=COLORS['border'],
        relief='flat',
        cursor='hand2',
        padx=25,
        pady=15
    ).pack(side='left')

    tk.Button(
        button_frame,
        text="Next: Practice Problems →",
        command=lambda: start_objective_practice_session(window, topic_name, topic_id, goal_id, goal_title, objectives, objective_index),
        font=FONTS['button_large'],
        bg=COLORS['success'],
        fg='white',
        activebackground=COLORS['success_dark'],
        relief='flat',
        cursor='hand2',
        padx=30,
        pady=15
    ).pack(side='right')


def generate_instruction_content(objective_title, objective_desc):
    """Generate AI instructional content for direct instruction"""
    if not AI_AVAILABLE:
        return f"Instructional content for: {objective_title}\n\n{objective_desc}"

    prompt = f"""You are an educational AI tutor. Create detailed instructional content for teaching this learning objective:

Learning Objective: {objective_title}
Description: {objective_desc}

Provide clear, comprehensive instruction that includes:
1. Introduction to the concept
2. Key definitions and terminology
3. Important principles or rules
4. Visual descriptions (describe what graphics would show)
5. Real-world applications or examples

Make it engaging, clear, and appropriate for students learning this topic for the first time.
Use simple language and break down complex ideas into understandable parts."""

    try:
        response = client.models.generate_content(
            model='gemini-2.5-flash',
            contents=prompt
        )
        return response.text
    except Exception as e:
        return f"Instructional content for: {objective_title}\n\n{objective_desc}\n\n(AI generation temporarily unavailable)"


def generate_walkthrough_content(objective_title, objective_desc):
    """Generate AI walkthrough example for problem solving"""
    if not AI_AVAILABLE:
        return f"Walkthrough example for: {objective_title}\n\n{objective_desc}"

    prompt = f"""You are an educational AI tutor. Create a detailed step-by-step walkthrough example for this learning objective:

Learning Objective: {objective_title}
Description: {objective_desc}

Provide a complete walkthrough that includes:
1. A sample problem statement
2. Step-by-step solution with clear explanations for each step
3. Why each step is necessary
4. Common mistakes to avoid
5. Final answer with verification

Format it clearly with numbered steps. Make it detailed enough that a student can follow along and understand the complete problem-solving process."""

    try:
        response = client.models.generate_content(
            model='gemini-2.5-flash',
            contents=prompt
        )
        return response.text
    except Exception as e:
        return f"Walkthrough example for: {objective_title}\n\n{objective_desc}\n\n(AI generation temporarily unavailable)"


def start_objective_practice_session(window, topic_name, topic_id, goal_id, goal_title, objectives, objective_index):
    """Start a practice session for a specific learning objective - BRD compliant"""
    obj_id, obj_title, obj_desc = objectives[objective_index]

    # Track session state
    session_state = {
        'problems_attempted': 0,
        'problems_correct': 0,
        'min_problems': 20,  # BRD requirement
        'mastery_threshold': 0.90,  # BRD requirement: 90%
        'can_exit': False
    }

    def check_mastery():
        """Check if student has achieved 90% mastery"""
        if session_state['problems_attempted'] == 0:
            return False
        accuracy = session_state['problems_correct'] / session_state['problems_attempted']
        return accuracy >= session_state['mastery_threshold']

    def can_complete_objective():
        """Check if student can complete this objective (BRD: min 20 problems AND 90% mastery)"""
        return (session_state['problems_attempted'] >= session_state['min_problems'] and
                check_mastery())

    def on_problem_completed(is_correct):
        """Called when a problem is completed"""
        session_state['problems_attempted'] += 1
        if is_correct:
            session_state['problems_correct'] += 1

        # Update can_exit flag
        session_state['can_exit'] = can_complete_objective()

    def move_to_next_objective():
        """Move to next objective in the goal"""
        next_index = objective_index + 1

        if next_index < len(objectives):
            # More objectives to practice
            messagebox.showinfo(
                "Objective Complete!",
                f"Great job! You've mastered '{obj_title}'!\n\n"
                f"Moving to next objective: {objectives[next_index][1]}"
            )
            show_practice_for_goal(window, topic_name, goal_id, next_index)
        else:
            # All objectives completed
            messagebox.showinfo(
                "Goal Complete!",
                f"Congratulations! You've completed all objectives for '{goal_title}'!\n\n"
                f"Total objectives mastered: {len(objectives)}"
            )
            show_goals_for_topic(window, topic_name)

    # Generate the practice problem interface
    generate_practice_problem_with_session(
        window,
        topic_name,
        topic_id,
        goal_id,
        obj_id,
        obj_title,
        session_state,
        on_problem_completed,
        move_to_next_objective,
        objective_index,
        len(objectives)
    )


def generate_practice_problem_with_session(window, topic_name, topic_id, goal_id, objective_id, objective_title,
                                          session_state, on_problem_completed, move_to_next_objective,
                                          current_obj_index, total_objectives):
    """Generate and display practice problems with session tracking - BRD compliant"""
    if not AI_AVAILABLE:
        messagebox.showerror("AI Not Available", "AI features require google-genai package to be installed.")
        return

    # Create modern practice window
    problem_window = tk.Toplevel(window)
    problem_window.title("Practice Problems")
    problem_window.geometry("950x850")
    problem_window.configure(bg=COLORS['bg_secondary'])

    # Center window
    problem_window.update_idletasks()
    width = problem_window.winfo_width()
    height = problem_window.winfo_height()
    x = (problem_window.winfo_screenwidth() // 2) - (width // 2)
    y = (problem_window.winfo_screenheight() // 2) - (height // 2)
    problem_window.geometry(f'{width}x{height}+{x}+{y}')

    # Header
    header = tk.Frame(problem_window, bg=COLORS['primary'], height=100)
    header.pack(fill='x')
    header.pack_propagate(False)

    header_content = tk.Frame(header, bg=COLORS['primary'])
    header_content.pack(fill='both', expand=True, padx=40, pady=20)

    # Title and objective info
    title_frame = tk.Frame(header_content, bg=COLORS['primary'])
    title_frame.pack(side='left', fill='both', expand=True)

    tk.Label(
        title_frame,
        text=f"📝 {objective_title}",
        font=FONTS['heading'],
        bg=COLORS['primary'],
        fg='white',
        wraplength=600,
        justify='left'
    ).pack(anchor='w')

    tk.Label(
        title_frame,
        text=f"Objective {current_obj_index + 1} of {total_objectives}",
        font=FONTS['body'],
        bg=COLORS['primary'],
        fg='white'
    ).pack(anchor='w', pady=(5, 0))

    close_btn = tk.Button(
        header_content,
        text="✕ Close",
        command=problem_window.destroy,
        font=FONTS['button'],
        bg=COLORS['primary_dark'],
        fg='white',
        activebackground=COLORS['primary'],
        relief='flat',
        cursor='hand2',
        padx=20,
        pady=10,
        borderwidth=0
    )
    close_btn.pack(side='right')

    # Progress bar frame
    progress_frame = tk.Frame(problem_window, bg=COLORS['bg_secondary'])
    progress_frame.pack(fill='x', padx=40, pady=(20, 10))

    # Progress labels
    progress_label = tk.Label(
        progress_frame,
        text=f"Problems: 0 / {session_state['min_problems']} minimum | Accuracy: 0% | Target: 90%",
        font=FONTS['body_bold'],
        bg=COLORS['bg_secondary'],
        fg=COLORS['text_primary']
    )
    progress_label.pack()

    def update_progress_display():
        """Update the progress display"""
        attempted = session_state['problems_attempted']
        correct = session_state['problems_correct']
        accuracy = (correct / attempted * 100) if attempted > 0 else 0

        # Color code based on progress
        if attempted >= session_state['min_problems'] and accuracy >= 90:
            color = COLORS['success']
            status = "✓ Mastery Achieved!"
        elif attempted >= session_state['min_problems']:
            color = COLORS['warning']
            status = "Continue practicing to reach 90%"
        else:
            color = COLORS['text_primary']
            status = f"{session_state['min_problems'] - attempted} more required"

        progress_label.config(
            text=f"Problems: {attempted} / {session_state['min_problems']} minimum | "
                 f"Accuracy: {accuracy:.0f}% | Target: 90% | {status}",
            fg=color
        )

    # Content area
    content = tk.Frame(problem_window, bg=COLORS['bg_secondary'])
    content.pack(fill='both', expand=True, padx=40, pady=(10, 30))

    # Problem type selection card
    type_card = tk.Frame(
        content,
        bg=COLORS['bg_primary'],
        relief='flat',
        highlightbackground=COLORS['border'],
        highlightthickness=1
    )
    type_card.pack(fill='x', pady=(0, 20))

    type_content = tk.Frame(type_card, bg=COLORS['bg_primary'])
    type_content.pack(padx=30, pady=20)

    tk.Label(
        type_content,
        text="Select Problem Type",
        font=FONTS['subheading'],
        bg=COLORS['bg_primary'],
        fg=COLORS['text_primary']
    ).pack(anchor='w', pady=(0, 15))

    category_var = tk.StringVar(value="factual")

    categories = [
        ("📚 Factual", "factual", "Basic facts and definitions"),
        ("🔧 Procedural", "procedural", "Step-by-step problem solving"),
        ("🎯 Strategic", "strategic", "Multi-step complex problems"),
        ("💡 Rational", "rational", "Explanations and reasoning")
    ]

    radio_frame = tk.Frame(type_content, bg=COLORS['bg_primary'])
    radio_frame.pack(fill='x')

    for icon_text, value, description in categories:
        radio_container = tk.Frame(radio_frame, bg=COLORS['bg_primary'])
        radio_container.pack(fill='x', pady=5)

        tk.Radiobutton(
            radio_container,
            text=f"{icon_text} - {description}",
            variable=category_var,
            value=value,
            font=FONTS['body'],
            bg=COLORS['bg_primary'],
            activebackground=COLORS['bg_primary'],
            selectcolor=COLORS['bg_tertiary']
        ).pack(anchor='w')

    # Problem display card
    problem_card = tk.Frame(
        content,
        bg=COLORS['bg_primary'],
        relief='flat',
        highlightbackground=COLORS['border'],
        highlightthickness=1
    )
    problem_card.pack(fill='both', expand=True, pady=(0, 20))

    problem_content = tk.Frame(problem_card, bg=COLORS['bg_primary'])
    problem_content.pack(padx=30, pady=25, fill='both', expand=True)

    tk.Label(
        problem_content,
        text="Problem",
        font=FONTS['subheading'],
        bg=COLORS['bg_primary'],
        fg=COLORS['text_primary']
    ).pack(anchor='w', pady=(0, 10))

    # Problem text area
    text_frame = tk.Frame(problem_content, bg=COLORS['bg_primary'])
    text_frame.pack(fill='both', expand=True, pady=(0, 20))

    scrollbar = tk.Scrollbar(text_frame)
    scrollbar.pack(side='right', fill='y')

    problem_text = tk.Text(
        text_frame,
        height=6,
        font=FONTS['body'],
        wrap='word',
        bg=COLORS['bg_tertiary'],
        fg=COLORS['text_primary'],
        padx=15,
        pady=15,
        relief='flat',
        state='disabled',
        yscrollcommand=scrollbar.set,
        borderwidth=0
    )
    problem_text.pack(side='left', fill='both', expand=True)
    scrollbar.config(command=problem_text.yview)

    # Answer input section
    answer_section = tk.Frame(problem_content, bg=COLORS['bg_primary'])
    answer_section.pack(fill='x')

    tk.Label(
        answer_section,
        text="Your Answer",
        font=FONTS['body_bold'],
        bg=COLORS['bg_primary'],
        fg=COLORS['text_primary']
    ).pack(anchor='w', pady=(0, 8))

    answer_entry = tk.Entry(
        answer_section,
        font=FONTS['body'],
        relief='solid',
        borderwidth=1,
        highlightthickness=2,
        highlightbackground=COLORS['border'],
        highlightcolor=COLORS['primary']
    )
    answer_entry.pack(fill='x', ipady=10)

    # Initially hide answer section
    answer_section.pack_forget()

    # State variables
    correct_answer = [None]
    generated_problem_id = [None]

    def generate():
        """Generate a new problem"""
        category = category_var.get()

        # Show loading
        problem_text.config(state='normal')
        problem_text.delete(1.0, tk.END)
        problem_text.insert(1.0, "⏳ Generating problem... Please wait...")
        problem_text.config(state='disabled')
        problem_window.update()

        # Generate problem
        problem, answer = generate_ai_problem(objective_id, category)

        if problem and answer:
            problem_text.config(state='normal')
            problem_text.delete(1.0, tk.END)
            problem_text.insert(1.0, problem)
            problem_text.config(state='disabled')

            correct_answer[0] = answer

            # Save to database
            problem_id = save_generated_problem(current_user_id, topic_id, goal_id, objective_id, problem, answer, category)
            generated_problem_id[0] = problem_id

            # Show answer input
            answer_section.pack(fill='x')
            answer_entry.delete(0, tk.END)
            answer_entry.focus()

            # Update button states
            submit_btn.config(state='normal')
        else:
            problem_text.config(state='normal')
            problem_text.delete(1.0, tk.END)
            problem_text.insert(1.0, "❌ Failed to generate problem. Please try again.")
            problem_text.config(state='disabled')
            answer_section.pack_forget()
            submit_btn.config(state='disabled')

    def submit_answer():
        """Submit answer and show feedback"""
        if correct_answer[0] is None:
            messagebox.showwarning("No Problem", "Please generate a problem first.")
            return

        student_answer = answer_entry.get().strip()
        if not student_answer:
            messagebox.showwarning("No Answer", "Please enter your answer.")
            return

        # Get problem text
        problem_text_content = problem_text.get(1.0, tk.END).strip()

        # Check answer
        is_correct = student_answer.lower() == correct_answer[0].lower()

        # Record attempt
        record_practice_attempt(current_user_id, goal_id, generated_problem_id[0], student_answer, is_correct)
        update_goal_progress(current_user, goal_id, 1 if is_correct else 0, 1)

        # Update session state
        on_problem_completed(is_correct)
        update_progress_display()

        # Show AI feedback dialog (non-blocking)
        if AI_AVAILABLE:
            show_ai_feedback_dialog_with_next(
                problem_text_content,
                student_answer,
                correct_answer[0],
                is_correct,
                lambda: next_problem()
            )
        else:
            result = "Correct! ✓" if is_correct else "Incorrect ✗"
            msg = f"{result}\n\nYour Answer: {student_answer}\nCorrect Answer: {correct_answer[0]}\n\nGenerate another problem?"
            if messagebox.askyesno("Result", msg):
                next_problem()

    def next_problem():
        """Prepare for next problem"""
        # Clear current problem
        problem_text.config(state='normal')
        problem_text.delete(1.0, tk.END)
        problem_text.insert(1.0, "Click 'Generate Problem' to start a new problem")
        problem_text.config(state='disabled')

        # Clear answer
        answer_entry.delete(0, tk.END)
        answer_section.pack_forget()

        # Reset state
        correct_answer[0] = None
        generated_problem_id[0] = None
        submit_btn.config(state='disabled')

        # Check if can complete objective
        if session_state['can_exit']:
            complete_btn.config(state='normal', bg=COLORS['success'])

    def complete_objective():
        """Complete the current objective and move to next"""
        if not session_state['can_exit']:
            messagebox.showwarning(
                "Not Ready",
                f"You need to complete at least {session_state['min_problems']} problems "
                f"with 90% accuracy to complete this objective.\n\n"
                f"Current: {session_state['problems_attempted']} problems, "
                f"{(session_state['problems_correct']/max(1,session_state['problems_attempted'])*100):.0f}% accuracy"
            )
            return

        problem_window.destroy()
        move_to_next_objective()

    # Action buttons
    button_frame = tk.Frame(content, bg=COLORS['bg_secondary'])
    button_frame.pack(pady=(0, 0))

    # Generate button
    generate_btn = tk.Button(
        button_frame,
        text="🎲 Generate Problem",
        command=generate,
        font=FONTS['button_large'],
        bg=COLORS['success'],
        fg='white',
        activebackground=COLORS['success_dark'],
        activeforeground='white',
        relief='flat',
        cursor='hand2',
        padx=25,
        pady=15,
        borderwidth=0
    )
    generate_btn.grid(row=0, column=0, padx=8)

    # Submit button
    submit_btn = tk.Button(
        button_frame,
        text="✓ Submit Answer",
        command=submit_answer,
        font=FONTS['button_large'],
        bg=COLORS['primary'],
        fg='white',
        activebackground=COLORS['primary_dark'],
        activeforeground='white',
        relief='flat',
        cursor='hand2',
        padx=25,
        pady=15,
        borderwidth=0,
        state='disabled'
    )
    submit_btn.grid(row=0, column=1, padx=8)

    # Next problem button
    next_btn = tk.Button(
        button_frame,
        text="→ Next Problem",
        command=next_problem,
        font=FONTS['button_large'],
        bg=COLORS['warning'],
        fg='white',
        activebackground=COLORS['warning_dark'],
        activeforeground='white',
        relief='flat',
        cursor='hand2',
        padx=25,
        pady=15,
        borderwidth=0
    )
    next_btn.grid(row=0, column=2, padx=8)

    # Complete objective button (initially disabled)
    complete_btn = tk.Button(
        button_frame,
        text="✓ Complete Objective",
        command=complete_objective,
        font=FONTS['button_large'],
        bg=COLORS['bg_tertiary'],
        fg=COLORS['text_secondary'],
        activebackground=COLORS['success_dark'],
        activeforeground='white',
        relief='flat',
        cursor='hand2',
        padx=25,
        pady=15,
        borderwidth=0,
        state='disabled'
    )
    complete_btn.grid(row=0, column=3, padx=8)

    # Hover effects
    def make_hover(btn, normal_color, hover_color):
        def on_enter(e):
            if btn['state'] != 'disabled':
                btn.config(bg=hover_color)
        def on_leave(e):
            if btn['state'] != 'disabled':
                btn.config(bg=normal_color)
        btn.bind("<Enter>", on_enter)
        btn.bind("<Leave>", on_leave)

    make_hover(generate_btn, COLORS['success'], COLORS['success_dark'])
    make_hover(submit_btn, COLORS['primary'], COLORS['primary_dark'])
    make_hover(next_btn, COLORS['warning'], COLORS['warning_dark'])

    # Enter key to submit
    answer_entry.bind('<Return>', lambda e: submit_answer())

    # Show initial message
    problem_text.config(state='normal')
    problem_text.insert(1.0, "👋 Welcome! Select a problem type above and click 'Generate Problem' to begin.")
    problem_text.config(state='disabled')


def generate_practice_problem(window, topic_name, topic_id, goal_id, objective_id, objective_title):
    """Legacy wrapper - redirects to BRD-compliant session-based practice"""
    # This is a wrapper for backward compatibility
    # Create a single-objective session
    objectives = [(objective_id, objective_title, "")]
    start_objective_practice_session(window, topic_name, topic_id, goal_id, "", objectives, 0)


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



