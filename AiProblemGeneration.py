import tkinter as tk
from tkinter import messagebox
import sqlite3
from groq import Groq

# CONFIG
DB_PATH = "learning_platform.db"
API_KEY = "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"  # replace with your real Groq API key

# Initialize Groq client
client = Groq(api_key=API_KEY)

# DATABASE FUNCTIONS
def fetch_learning_objectives():
    """Fetch all learning objectives from the DB."""
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()
    cursor.execute("SELECT id, description FROM LearningObjective ORDER BY id;")
    results = cursor.fetchall()
    conn.close()
    return results
# AI FUNCTION
def generate_problem(description):
    """Send a description to Groq and get a generated practice problem."""
    prompt = (
        f"Based on this learning objective:\n"
        f"\"{description}\"\n\n"
        "Generate one clear math practice problem with a numeric answer. "
        "Make sure it is appropriate for a student learning this objective. "
        "Do not include explanations, just the problem statement."
    )

    response = client.chat.completions.create(
        model="meta-llama/llama-4-scout-17b-16e-instruct",  # Groq model
        messages=[{"role": "user", "content": prompt}],
        max_tokens=150,
        temperature=0.7,
    )


    return response.choices[0].message.content.strip()

# GUI FUNCTIONS
def show_problem():
    selection = listbox.curselection()
    if not selection:
        messagebox.showwarning("No Selection", "Please select a learning objective.")
        return

    index = selection[0]
    obj_id, description = objectives[index]

    try:
        problem = generate_problem(description)
        messagebox.showinfo("Generated Practice Problem", problem)
    except Exception as e:
        messagebox.showerror("FAILED", str(e))

# MAIN GUI
objectives = fetch_learning_objectives()

root = tk.Tk()
root.title("AI Practice Problem Generator")

tk.Label(root, text="Select a Learning Objective:", font=("Arial", 12)).pack(pady=5)

listbox = tk.Listbox(root, width=100, height=20)
for obj_id, desc in objectives:
    listbox.insert(tk.END, f"{obj_id}: {desc}")
listbox.pack(padx=10, pady=5)

tk.Button(root, text="Generate Practice Problem", command=show_problem).pack(pady=10)

root.mainloop()
