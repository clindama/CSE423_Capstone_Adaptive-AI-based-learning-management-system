import tkinter as tk
from tkinter import messagebox, simpledialog, ttk
import sqlite3
from groq import Groq
import os
import random
import string

# CONFIG
DB_PATH = "learning_platform.db"
API_KEY = "YOUR_GROQ_API"

# Users
USERS = {
    1: "Alice",
    2: "Bob",
    3: "Charlie",
    4: "Diana",
    5: "Eve"
}
current_user_id = 1  # default user

# Initialize Groq client
client = Groq(api_key=API_KEY)

# --- DATABASE ---
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

# --- HELPERS ---
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

def insert_problem(topic_id, goal_id, objective_id, prompt, answer, category="factual"):
    conn = sqlite3.connect(DB_PATH)
    cur = conn.cursor()
    cur.execute("""
        INSERT INTO Problem (topic_id, goal_id, objective_id, prompt, correct_answer, category)
        VALUES (?, ?, ?, ?, ?, ?)
    """, (topic_id, goal_id, objective_id, prompt, answer, category))
    problem_id = cur.lastrowid
    conn.commit()
    conn.close()
    return problem_id

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

# --- AI ---
def generate_problem(obj_title, obj_desc, category):
    """Generate a problem with slight randomness to avoid duplicates."""
    noise = ''.join(random.choices(string.ascii_lowercase, k=4))
    prompt = (
        f"Learning objective: {obj_title}\n"
        f"Description: {obj_desc}\n"
        f"Category: {category}\n\n"
        "Generate ONE math practice problem for this objective. "
        "Provide the correct numeric answer.\n\n"
        "Format:\nProblem: ...\nAnswer: ...\n"
        f"[variation:{noise}]"
    )
    resp = client.chat.completions.create(
        model="meta-llama/llama-4-scout-17b-16e-instruct",
        messages=[{"role": "user", "content": prompt}],
        max_tokens=200,
        temperature=0.9,
    )
    text = resp.choices[0].message.content.strip()
    problem, answer = "", ""
    if "Answer:" in text:
        parts = text.split("Answer:")
        problem = parts[0].replace("Problem:", "").strip()
        answer = parts[1].strip()
    else:
        problem = text
    return problem, answer

# --- GUI ACTIONS ---
def change_user(event=None):
    global current_user_id
    current_user_id = user_var.get()

def show_problem():
    selection = listbox.curselection()
    if not selection:
        messagebox.showwarning("No Selection", "Pick a learning objective first")
        return
    idx = selection[0]
    obj_id, lo_title, lo_desc, goal_id, topic_id, goal_title, topic_title = objectives[idx]

    # Ask category first
    category = simpledialog.askstring(
        "Problem Category", "Enter category (factual, procedural, strategic, rational):"
    )
    if not category or category not in ["factual", "procedural", "strategic", "rational"]:
        messagebox.showerror("Invalid", "Must enter one of: factual, procedural, strategic, rational.")
        return

    try:
        problem, answer = generate_problem(lo_title, lo_desc, category)
        problem_id = insert_problem(topic_id, goal_id, obj_id, problem, answer, category)

        # Ask if student got it right
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

        create_practice_set(current_user_id, goal_id, problem_id, student_answer, is_correct)

        messagebox.showinfo(
            "Saved",
            f"Problem saved for {USERS[current_user_id]}.\n"
            f"Marked as {'Correct' if is_correct else 'Wrong'}.\n\n"
            f"Correct Answer: {answer}\nStudent Answer: {student_answer}"
        )
    except Exception as e:
        messagebox.showerror("FAILED", str(e))

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
            JOIN Problem p ON pp.genProblem_id = p.id
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

# --- MAIN GUI ---
root = tk.Tk()
root.title("AI Problem Generator with Users & Results")
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

tk.Button(root, text="Generate & Answer Problem", command=show_problem).pack(pady=5)
tk.Button(root, text="View Results", command=view_results).pack(pady=5)

root.mainloop()