import tkinter as tk
from tkinter import messagebox, simpledialog, ttk
import sqlite3
import os
import random
import string

import google.genai as genai
from google.genai import types

# CONFIG
DB_PATH = "learning_platform.db"
API_KEY = "key" # Replace with your actual API key

# Users
USERS = {
    1: "Alice",
    2: "Bob",
    3: "Charlie",
    4: "Diana",
    5: "Eve"
}
current_user_id = 1  # default user

# Initialize Google Generative AI client
client = genai.Client(api_key=API_KEY)

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

# --- HELPERS --- #
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
    cur.execute("""
        INSERT INTO PracticeProblemSet (user_id, goal_id) VALUES (?, ?)
    """, (user_id, goal_id))
    set_id = cur.lastrowid
    cur.execute("""
        INSERT INTO PracticeProblem (set_id, genProblem_id, student_answer, is_correct)
        VALUES (?, ?, ?, ?)
    """, (set_id, problem_id, student_answer, is_correct))
    conn.commit()
    conn.close()

# --- PINNED AI CONTEXT --- #
def load_pinned_context():
    """Load AI tutor identity, knowledge types, and template problems."""
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

    knowledge_types = """
Knowledge Types:
- Factual: General info/facts about the topic/goal.
- Procedural: Specific steps to solve a problem (like a room in a house).
- Strategic: Multi-step problems; culmination of procedural steps (like the entire house).
- Rational: Explanations behind concepts; the "why".
"""

    tutor_identity = "You are a helpful, personalized AI math tutor. Generate practice problems tailored to the learning objective and category provided."

    template_text = "Example problem templates:\n"
    for t in templates:
        template_text += f"- Category: {t[4]}, Prompt: {t[3]}\n"

    pinned_context = f"{tutor_identity}\n{knowledge_types}\n{template_text}"
    return pinned_context

# --- AI PROBLEM GENERATION --- #
def generate_problem_gen(obj_title, obj_desc, category):
    """Generate a new problem for GenProblem using pinned context."""
    noise = ''.join(random.choices(string.ascii_lowercase, k=4))
    pinned_context = load_pinned_context()

    prompt = f"""
{pinned_context}

Generate ONE NEW math problem for this objective.
Learning Objective: {obj_title}
Description: {obj_desc}
Category: {category}
Provide the correct answer.
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

        print(f"Generated GenProblem: {problem}\nAnswer: {answer}\n---")
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
    current_user_id = user_var.get()

def show_problem_gen():
    selection = listbox.curselection()
    if not selection:
        messagebox.showwarning("No Selection", "Pick a learning objective first")
        return
    idx = selection[0]
    obj_id, lo_title, lo_desc, goal_id, topic_id, goal_title, topic_title = objectives[idx]

    category_num = simpledialog.askstring(
        "Problem Category", "Enter category [factual (1), procedural (2), strategic (3), rational (4)]:"
    )
    if not category_num or category_num not in ["1", "2", "3", "4"]:
        messagebox.showerror("Invalid", "Must enter one of: 1, 2, 3, 4.")
        return
    category_map = {"1": "factual", "2": "procedural", "3": "strategic", "4": "rational"}
    category = category_map[category_num]

    # Generate problem
    problem, answer = generate_problem_gen(lo_title, lo_desc, category)
    if problem is None:
        messagebox.showerror("Failed", "AI problem generation failed.")
        return

    # Save to GenProblem
    gen_problem_id = insert_gen_problem(current_user_id, topic_id, goal_id, obj_id, problem, answer, category)

    # Ask user if they got it right
    choice = messagebox.askquestion(
        "Answer Simulation",
        f"Topic: {topic_title}\nGoal: {goal_title}\nObjective: {lo_title}\n\n"
        f"Problem:\n{problem}\n\nDid {USERS[current_user_id]} answer correctly?"
    )
    if choice == 'yes':
        student_answer = answer
        is_correct = 1
    else:
        student_answer = ''.join(random.choices(string.ascii_letters + string.digits, k=5))
        is_correct = 0

    create_practice_set(current_user_id, goal_id, gen_problem_id, student_answer, is_correct)

    messagebox.showinfo(
        "Saved",
        f"Generated problem saved for {USERS[current_user_id]}.\n"
        f"Marked as {'Correct' if is_correct else 'Wrong'}.\n\n"
        f"Correct Answer: {answer}\nStudent Answer: {student_answer}"
    )

def view_results():
    conn = sqlite3.connect(DB_PATH)
    cur = conn.cursor()
    results = {}
    for user_id, username in USERS.items():
        results[username] = {'factual': 0, 'procedural': 0, 'strategic': 0, 'rational': 0,
                             'factual_wrong': 0, 'procedural_wrong': 0, 'strategic_wrong': 0, 'rational_wrong': 0}
        cur.execute("""
            SELECT p.category, pp.is_correct
            FROM PracticeProblem pp
            JOIN GenProblem p ON pp.genProblem_id = p.id
            JOIN PracticeProblemSet ps ON pp.set_id = ps.id
            WHERE ps.user_id = ?
        """, (user_id,))
        for category, is_correct in cur.fetchall():
            if is_correct:
                results[username][category] += 1
            else:
                results[username][f"{category}_wrong"] += 1
    conn.close()

    win = tk.Toplevel(root)
    win.title("Results Summary")
    tree = ttk.Treeview(win, columns=('Category', 'Correct', 'Wrong'), show='headings')
    tree.heading('Category', text='Category')
    tree.heading('Correct', text='Correct')
    tree.heading('Wrong', text='Wrong')
    tree.pack(fill=tk.BOTH, expand=True)
    for username, res in results.items():
        for cat in ['factual', 'procedural', 'strategic', 'rational']:
            tree.insert('', tk.END, values=(f"{username} - {cat}", res[cat], res[f"{cat}_wrong"]))

def refresh_objectives():
    global objectives
    objectives = fetch_objectives()
    listbox.delete(0, tk.END)
    for obj_id, lo_title, lo_desc, goal_id, topic_id, goal_title, topic_title in objectives:
        listbox.insert(tk.END, f"Topic: {topic_title} | Goal: {goal_title} | Objective: {lo_title}")

# --- MAIN GUI --- #
# clean_start()
root = tk.Tk()
root.title("AI Problem Generator with Pinned Context")
tk.Button(root, text="Reset Database", command=reset_database).pack(pady=5)
tk.Label(root, text="Select User:", font=("Arial", 12)).pack(pady=5)
user_var = tk.IntVar(value=current_user_id)
user_menu = ttk.Combobox(root, values=list(USERS.keys()), textvariable=user_var)
user_menu.pack(pady=5)
user_menu.bind("<<ComboboxSelected>>", change_user)

tk.Label(root, text="Select Learning Objective:", font=("Arial", 12)).pack(pady=5)
listbox = tk.Listbox(root, width=100, height=20)
listbox.pack(padx=10, pady=5)

refresh_objectives()

tk.Button(root, text="Generate & Answer Problem", command=show_problem_gen).pack(pady=5)
tk.Button(root, text="View Results", command=view_results).pack(pady=5)

root.mainloop()