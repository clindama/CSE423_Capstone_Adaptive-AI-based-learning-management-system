import tkinter as tk
from tkinter import messagebox, simpledialog, ttk
import sqlite3
import os
import random
import string

import google.genai as genai
from google.genai import types

# CONFIG
DB_PATH = "advanceDemo.db"
API_KEY = "REPLACE"  # Replace with your actual key

# --- USER SETUP --- #
USERS = {
    1: "Alice",
    2: "Bob",
    3: "Charlie",
    4: "Diana"
}
current_user_id = 1  # default user

# Initialize Google Generative AI client
client = genai.Client(api_key=API_KEY)

# --- SESSION MEMORY (In-Memory Cache) --- #
class UserLMSProfile:
    def __init__(self, name):
        self.name = name
        self.performance = {
            "factual": {"correct": 0, "wrong": 0},
            "procedural": {"correct": 0, "wrong": 0},
            "strategic": {"correct": 0, "wrong": 0},
            "rational": {"correct": 0, "wrong": 0},
        }
        self.preferred_styles = []   # e.g., ['visual', 'logical']
        self.ai_goal = "teach new"
        self.extra_notes = "No personalization yet."

    def update(self, category, correct):
        if category in self.performance:
            if correct:
                self.performance[category]["correct"] += 1
            else:
                self.performance[category]["wrong"] += 1

    def describe(self):
        summary = f"User: {self.name}\nAI Goal: {self.ai_goal}\nPreferred Styles: {', '.join(self.preferred_styles) or 'None'}\n\nPerformance:"
        for k, v in self.performance.items():
            total = v['correct'] + v['wrong']
            acc = f"{v['correct']}/{total}" if total > 0 else "0/0"
            summary += f"\n  - {k.capitalize()}: {acc}"
        summary += f"\n\nNotes: {self.extra_notes}"
        return summary


# --- SESSION MEMORY (In-Memory Cache) --- #
USER_PROFILES = {
    1: UserLMSProfile("Alice"),  # new user, no profile
    2: UserLMSProfile("Bob"),
    3: UserLMSProfile("Charlie"),
    4: UserLMSProfile("Diana"),
}

# Extra details per user
USER_PROFILES[1].preferred_styles = ["visual", "logical"]
USER_PROFILES[1].extra_notes = "New user, profile will be learned over first 10 questions."

USER_PROFILES[2].preferred_styles = ["procedural"]
USER_PROFILES[2].extra_notes = "Likes sports-themed problems. Struggles with rational questions."

USER_PROFILES[3].preferred_styles = ["rational", "strategic"]
USER_PROFILES[3].extra_notes = "Enjoys complex/sophisticated wording. Very smart."

USER_PROFILES[4].preferred_styles = ["factual", "visual"]
USER_PROFILES[4].extra_notes = "Struggles with strategic problems. Prefers simple wording and visuals."

# --- DATABASE --- #
def reset_database():
    """Delete the DB and reload schema + seed data."""
    if os.path.exists(DB_PATH):
        os.remove(DB_PATH)
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()

    with open("tables.sql", "r") as f:
        cursor.executescript(f.read())
    for sql_file in ["toplist.sql", "seed_methods.sql", "seed_objectives.sql", "seed_problems.sql"]:
        with open(sql_file, "r") as f:
            cursor.executescript(f.read())

    conn.commit()
    conn.close()
    refresh_objectives()
    messagebox.showinfo("Database Reset", "Database has been reset and seeded.")


def fetch_objectives():
    conn = sqlite3.connect(DB_PATH)
    cur = conn.cursor()
    cur.execute("""
        SELECT lo.id, lo.title, lo.description, lo.goal_id, g.topic_id, g.title, t.name
        FROM LearningObjective lo
        JOIN Goal g ON lo.goal_id = g.id
        JOIN Topic t ON g.topic_id = t.id
        ORDER BY lo.id
    """)
    data = cur.fetchall()
    conn.close()
    return data



def create_practice_set(user_id, goal_id, problem_id, student_answer, is_correct):
    conn = sqlite3.connect(DB_PATH)
    cur = conn.cursor()
    cur.execute("INSERT INTO PracticeProblemSet (user_id, goal_id) VALUES (?, ?)", (user_id, goal_id))
    set_id = cur.lastrowid
    cur.execute("""
        INSERT INTO PracticeProblem (set_id, genProblem_id, student_answer, is_correct)
        VALUES (?, ?, ?, ?)
    """, (set_id, problem_id, student_answer, is_correct))
    conn.commit()
    conn.close()


def load_pinned_context(user_id):
    """Load tutor identity, knowledge types, sample problems, plus user profile memory."""
    conn = sqlite3.connect(DB_PATH)
    cur = conn.cursor()
    cur.execute("""
        SELECT topic_id, goal_id, objective_id, prompt, category
        FROM Problem
        ORDER BY id
        LIMIT 20
    """)
    templates = cur.fetchall()
    conn.close()

    profile = USER_PROFILES.get(user_id)
    memory_summary = profile.describe() if profile else "No memory yet."

    knowledge_types = """
Knowledge Types:
- Factual: General info/facts about the topic/goal.
- Procedural: Specific steps to solve a problem.
- Strategic: Multi-step or applied reasoning problems.
- Rational: Conceptual explanations behind why things work.
"""

    tutor_identity = "You are a helpful, personalized AI math tutor that adjusts problems based on performance memory and preferences."

    template_text = "Example problem templates:\n"
    for t in templates:
        template_text += f"- Category: {t[4]}, Prompt: {t[3]}\n"

    pinned_context = f"{tutor_identity}\n{knowledge_types}\n{template_text}\n\nCurrent Student Memory:\n{memory_summary}"
    return pinned_context

# --- USER LMS PROFILE HANDLING ---
def load_user_profile(user_id):
    """Load existing profile or create default if none exists."""
    conn = sqlite3.connect(DB_PATH)
    cur = conn.cursor()
    cur.execute("SELECT * FROM UserLMSProfile WHERE user_id=?", (user_id,))
    row = cur.fetchone()
    
    if row is None:
        # If first-time user, create minimal default profile
        cur.execute("""
            INSERT INTO UserLMSProfile (
                user_id, preferred_learner_style, target_difficulty, 
                preferred_length, preferred_numeric_complexity, focus_category, 
                performance_score, ai_goal, notes
            ) VALUES (?, 'visual', 2, 'medium', 'integers_only', 'procedural', 0, 'teach_new', '{}')
        """, (user_id,))
        conn.commit()
        cur.execute("SELECT * FROM UserLMSProfile WHERE user_id=?", (user_id,))
        row = cur.fetchone()
    
    columns = [col[0] for col in cur.description]
    profile = dict(zip(columns, row))
    conn.close()
    return profile

def update_user_profile_after_attempt(user_id):
    """Recalculate profile metrics from past attempts."""
    conn = sqlite3.connect(DB_PATH)
    cur = conn.cursor()
    
    # Count correct/wrong per category
    cur.execute("""
        SELECT p.category, SUM(pp.is_correct), COUNT(*)
        FROM PracticeProblem pp
        JOIN GenProblem p ON pp.genProblem_id = p.id
        JOIN PracticeProblemSet ps ON pp.set_id = ps.id
        WHERE ps.user_id = ?
        GROUP BY p.category
    """, (user_id,))
    data = cur.fetchall()
    
    if not data:
        conn.close()
        return  # no attempts yet
    
    # Compute rolling accuracy & weakest category
    total_correct, total_attempts = 0, 0
    category_perf = {}
    for category, correct_sum, count in data:
        category_perf[category] = correct_sum / count if count else 0
        total_correct += correct_sum
        total_attempts += count
    overall_score = (total_correct / total_attempts) * 100 if total_attempts else 0
    
    # Determine focus category (lowest accuracy)
    focus_category = min(category_perf, key=category_perf.get)
    
    # Adjust target difficulty slightly based on overall performance
    cur.execute("SELECT target_difficulty FROM UserLMSProfile WHERE user_id=?", (user_id,))
    current_diff = cur.fetchone()[0]
    new_diff = current_diff
    if overall_score > 80 and current_diff < 5:
        new_diff += 1
    elif overall_score < 50 and current_diff > 1:
        new_diff -= 1
    
    # Update profile
    cur.execute("""
        UPDATE UserLMSProfile
        SET focus_category=?, target_difficulty=?, performance_score=?, last_updated=CURRENT_TIMESTAMP
        WHERE user_id=?
    """, (focus_category, new_diff, overall_score, user_id))
    
    conn.commit()
    conn.close()

# --- AI PROBLEM GENERATION --- #
def generate_problem_gen(obj_title, obj_desc, category, user_profile, mode='auto'):
    """Generate a new problem using pinned context and user profile info."""
    pinned_context = load_pinned_context(user_profile['user_id'])
    noise = ''.join(random.choices(string.ascii_lowercase, k=4))

    # Include profile info in auto mode
    if mode == 'auto':
        profile_text = f"""
Student Profile:
- Preferred Learner Style: {user_profile['preferred_learner_style']}
- Target Difficulty: {user_profile['target_difficulty']}
- Preferred Numeric Complexity: {user_profile['preferred_numeric_complexity']}
- Focus Category: {user_profile['focus_category']}
- AI Goal: {user_profile['ai_goal']}
- Extra Notes: {user_profile.get('extra_notes','')}
"""
        # Determine challenge vs comfort
        if category != user_profile['focus_category']:
            challenge_text = f"Try to challenge the user in the {category} category."
        else:
            challenge_text = f"This problem should be comfortable for the user."
    else:
        profile_text = ""
        challenge_text = ""

    prompt = f"""
{pinned_context}
{profile_text}
{challenge_text}

Generate ONE NEW math problem for this objective.
Learning Objective: {obj_title}
Description: {obj_desc}
Category: {category}  -- MUST MATCH this category exactly
Problems should not be multiple choice.

Format exactly as:
Problem: ...
Answer: ...

[variation:{noise}]
"""

    try:
        generation_config = types.GenerateContentConfig(
            temperature=0.9,
            max_output_tokens=200,
        )
        response = client.models.generate_content(
            model="gemini-2.5-flash-lite",
            contents=[prompt],
            config=generation_config,
        )

        text = response.candidates[0].content.parts[0].text.strip()
        problem, answer = "", ""
        if "Answer:" in text:
            parts = text.split("Answer:")
            problem = parts[0].replace("Problem:", "").strip()
            answer = parts[1].strip()
        else:
            problem = text
            answer = ""

        return problem, answer

    except Exception as e:
        print("Error generating problem:", str(e))
        return None, None


def insert_gen_problem(user_id, topic_id, goal_id, objective_id, prompt, answer, category):
    conn = sqlite3.connect(DB_PATH)
    cur = conn.cursor()
    cur.execute("""
        INSERT INTO GenProblem (user_id, topic_id, goal_id, objective_id, prompt, correct_answer, category)
        VALUES (?, ?, ?, ?, ?, ?, ?)
    """, (user_id, topic_id, goal_id, objective_id, prompt, answer, category))
    gen_problem_id = cur.lastrowid
    conn.commit()
    conn.close()
    return gen_problem_id

# --- GUI ACTIONS --- #
def change_user(event=None):
    global current_user_id
    current_user_id = int(user_var.get())
    refresh_objectives()

def run_problem_set():
    """Generate 20 problems for current user and simulate answers based on demo average."""
    # Demo averages for users
    demo_avg = {1: 80, 2: 80, 3: 90, 4: 60}  # percent correct
    total_questions = 20
    num_correct = int((demo_avg[current_user_id] / 100) * total_questions)
    
    user_profile = load_user_profile(current_user_id)
    
    # Pick random objectives for problems
    objective_ids = [obj[0] for obj in objectives]
    for i in range(total_questions):
        obj_idx = random.randint(0, len(objectives) - 1)
        obj_id, lo_title, lo_desc, goal_id, topic_id, goal_title, topic_title = objectives[obj_idx]

        # Determine category: auto mode uses profile focus for early questions, mix for remaining
        if i < num_correct:
            category = user_profile['focus_category'] or 'procedural'
        else:
            # pick a category user struggles with if available
            struggling = ['factual','procedural','strategic','rational']
            if user_profile['focus_category']:
                struggling.remove(user_profile['focus_category'])
            category = random.choice(struggling)

        # Generate problem
        problem, answer = generate_problem_gen(lo_title, lo_desc, category, user_profile, mode='auto')
        if problem is None:
            continue  # skip if generation fails

        # Save problem
        gen_problem_id = insert_gen_problem(current_user_id, topic_id, goal_id, obj_id, problem, answer, category)

        # Simulate answer
        is_correct = 1 if i < num_correct else 0
        student_answer = answer if is_correct else ''.join(random.choices(string.ascii_letters + string.digits, k=5))
        create_practice_set(current_user_id, goal_id, gen_problem_id, student_answer, is_correct)

        # Update profile after each attempt
        update_user_profile_after_attempt(current_user_id)

    messagebox.showinfo("Problem Set", f"Generated and solved {total_questions} problems for {USERS[current_user_id]}.")

def show_problem_gen():
    selection = listbox.curselection()
    if not selection:
        messagebox.showwarning("No Selection", "Pick a learning objective first")
        return
    idx = selection[0]
    obj_id, lo_title, lo_desc, goal_id, topic_id, goal_title, topic_title = objectives[idx]

    user_profile = load_user_profile(current_user_id)

    # Ask Auto or Manual
    mode_choice = simpledialog.askstring(
        "Mode", "Select mode: auto or manual"
    )
    if mode_choice not in ["auto", "manual"]:
        messagebox.showerror("Invalid", "Must enter 'auto' or 'manual'.")
        return

    # In Manual mode, only select knowledge type
    if mode_choice == "manual":
        category_num = simpledialog.askstring(
            "Problem Category", "Enter category [factual (1), procedural (2), strategic (3), rational (4)]:"
        )
        if not category_num or category_num not in ["1", "2", "3", "4"]:
            messagebox.showerror("Invalid", "Must enter one of: 1, 2, 3, 4.")
            return
        category_map = {"1": "factual", "2": "procedural", "3": "strategic", "4": "rational"}
        category = category_map[category_num]
    else:
        # Auto mode uses profile focus category as default category if available
        category = user_profile['focus_category'] or 'procedural'

    # Generate problem
    problem, answer = generate_problem_gen(lo_title, lo_desc, category, user_profile, mode=mode_choice)
    if problem is None:
        messagebox.showerror("Failed", "AI problem generation failed.")
        return

    # Save to GenProblem
    gen_problem_id = insert_gen_problem(current_user_id, topic_id, goal_id, obj_id, problem, answer, category)

    # Simulate student attempt
    choice = messagebox.askquestion(
        "Answer Simulation",
        f"Problem:\n{problem}\n\nDid {USERS[current_user_id]} answer correctly?"
    )
    student_answer = answer if choice == 'yes' else ''.join(random.choices(string.ascii_letters + string.digits, k=5))
    is_correct = 1 if choice == 'yes' else 0

    create_practice_set(current_user_id, goal_id, gen_problem_id, student_answer, is_correct)

    # Update profile after this attempt
    update_user_profile_after_attempt(current_user_id)

    messagebox.showinfo(
        "Saved",
        f"Generated problem saved for {USERS[current_user_id]}.\n"
        f"Marked as {'Correct' if is_correct else 'Wrong'}.\n\n"
        f"Correct Answer: {answer}\nStudent Answer: {student_answer}"
    )

def view_profile():
    """Show current user's results + LMS profile."""
    user_profile = load_user_profile(current_user_id)

    # Fetch per-category performance
    conn = sqlite3.connect(DB_PATH)
    cur = conn.cursor()
    cur.execute("""
        SELECT p.category, SUM(pp.is_correct), COUNT(*)
        FROM PracticeProblem pp
        JOIN GenProblem p ON pp.genProblem_id = p.id
        JOIN PracticeProblemSet ps ON pp.set_id = ps.id
        WHERE ps.user_id = ?
        GROUP BY p.category
    """, (current_user_id,))
    data = cur.fetchall()
    conn.close()

    results = {cat: {'correct': 0, 'wrong': 0} for cat in ['factual','procedural','strategic','rational']}
    for category, correct_sum, total_count in data:
        results[category]['correct'] = correct_sum
        results[category]['wrong'] = total_count - correct_sum

    # GUI window
    win = tk.Toplevel(root)
    win.title(f"{USERS[current_user_id]} - Profile & Performance")
    tree = ttk.Treeview(win, columns=('Metric','Value'), show='headings')
    tree.heading('Metric', text='Metric')
    tree.heading('Value', text='Value')
    tree.pack(fill=tk.BOTH, expand=True)

    # Performance
    for cat, vals in results.items():
        tree.insert('', tk.END, values=(f"{cat} correct", vals['correct']))
        tree.insert('', tk.END, values=(f"{cat} wrong", vals['wrong']))

    # LMS Profile
    for key in ['preferred_learner_style','target_difficulty','preferred_length',
                'preferred_numeric_complexity','focus_category','performance_score',
                'ai_goal','notes']:
        tree.insert('', tk.END, values=(key, user_profile[key]))


def refresh_objectives():
    global objectives
    objectives = fetch_objectives()
    listbox.delete(0, tk.END)
    for obj_id, lo_title, lo_desc, goal_id, topic_id, goal_title, topic_title in objectives:
        listbox.insert(tk.END, f"Topic: {topic_title} | Goal: {goal_title} | Objective: {lo_title}")


# --- MAIN GUI --- #
root = tk.Tk()
root.title("Memory-Aware AI Problem Generator")

tk.Button(root, text="Reset Database", command=reset_database).pack(pady=5)
tk.Label(root, text="Select User:", font=("Arial", 12)).pack(pady=5)

user_var = tk.StringVar(value=current_user_id)
user_menu = ttk.Combobox(root, values=list(USERS.keys()), textvariable=user_var)
user_menu.pack(pady=5)
user_menu.bind("<<ComboboxSelected>>", change_user)

tk.Label(root, text="Select Learning Objective:", font=("Arial", 12)).pack(pady=5)
listbox = tk.Listbox(root, width=100, height=20)
listbox.pack(padx=10, pady=5)

refresh_objectives()

tk.Button(root, text="Generate & Answer Problem", command=show_problem_gen).pack(pady=5)
tk.Button(root, text="View Profile", command=view_profile).pack(pady=5)

tk.Button(root, text="Run Problem Set", command=run_problem_set).pack(pady=5)


root.mainloop()