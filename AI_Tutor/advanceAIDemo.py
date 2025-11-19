import tkinter as tk
from tkinter import messagebox, ttk
import sqlite3
import os
import random
import string

import google.genai as genai
from google.genai import types

DB_PATH = "advanceDemo.db"
API_KEY = "AIzaSyCbaAhYPM6D6C1EonXwxyq49AxlGsvgjIQ"
client = genai.Client(api_key=API_KEY)

USERS = {1: "Alice", 2: "Bob", 3: "Charlie", 4: "Diana"}
current_user_id = 2

# Resets Database for clean testing
def reset_database():
    if os.path.exists(DB_PATH):
        os.remove(DB_PATH)

    conn = sqlite3.connect(DB_PATH)
    cur = conn.cursor()

    with open("tables.sql", "r") as f:
        cur.executescript(f.read())

    for sql_file in ["toplist.sql", "seed_methods.sql", "seed_objectives.sql", "seed_problems.sql"]:
        with open(sql_file, "r") as f:
            cur.executescript(f.read())

    conn.commit()
    conn.close()

    refresh_objectives()
    messagebox.showinfo("Database Reset", "Database has been reset and seeded.")


# Load user profile (Or create an empty profile)
def load_user_profile(user_id):
    conn = sqlite3.connect(DB_PATH)
    cur = conn.cursor()

    cur.execute("SELECT * FROM UserLMSProfile WHERE user_id=?", (user_id,))
    row = cur.fetchone()

    # Create default profile if none exists
    if row is None:
        cur.execute("""
            INSERT INTO UserLMSProfile (
                user_id, preferred_learner_style, target_difficulty,
                preferred_length, preferred_numeric_complexity,
                focus_category, performance_score, ai_goal, notes
            ) VALUES (?, 'visual', 2, 'medium', 'integers_only',
                    'procedural', 0, 'teach_new', 'No notes')
        """, (user_id,))
        conn.commit()
        cur.execute("SELECT * FROM UserLMSProfile WHERE user_id=?", (user_id,))
        row = cur.fetchone()

    columns = [c[0] for c in cur.description]
    profile = dict(zip(columns, row))

    conn.close()
    return profile

# Constant context for AI
def load_context(user_id):
    profile = load_user_profile(user_id)

    conn = sqlite3.connect(DB_PATH)
    cur = conn.cursor()

    # Fetch last 20 attempts for context
    cur.execute("""
    SELECT pp.id, p.category, p.prompt, pp.student_answer, pp.is_correct
    FROM PracticeProblem pp
    JOIN GenProblem p ON p.id = pp.genProblem_id
    JOIN PracticeProblemSet ps ON ps.id = pp.set_id
    WHERE ps.user_id=?
    ORDER BY pp.id ASC
    LIMIT 20
    """, (user_id,))

    attempts = cur.fetchall()

    attempts_summary = "\n".join(
        [f"ID: {pid}, Category: {c}, Problem: {q}, Student Answer: {a}, Correct: {bool(s)}"
        for pid, c, q, a, s in attempts]
    )
    conn.close()

    perf_summary, overall_score = get_full_performance(user_id)
    perf_text = "\n".join([f"{cat}: {score}%" for cat, score in perf_summary.items()])
    cat_summary = f"\nOverall Performance Score: {overall_score}%\nCategory Performance:\n{perf_text}"

    return f"""
        <identity>
        You are a math tutor who creates personalized learning experiences for your students. You adapt your teaching methods based on each student's unique profile and learning history.

        You know your students by using their Student Profile that you maintain and update over time. Refer to <profile_structure> for details on each field.
        Here is the current profile for the student you are tutoring:
        Preferred Style: {profile['preferred_learner_style']}
        Difficulty: {profile['target_difficulty']}
        Numeric Pref: {profile['preferred_numeric_complexity']}
        Focus Category: {profile['focus_category']}
        Notes: {profile['notes']}

        Knowledge Types are the key categories of problems or content you create. These are the most important variables in tailoring learning experiences:
        - Factual: General info/facts about the topic/goal.
        - Procedural: Specific steps to solve a problem (like a room in a house).
        - Strategic: Multi-step problems; culmination of procedural steps (The entire house).
        - Rational: Explanations behind concepts; the "why".

        ALWAYS Be unique and creative in your generation, avoiding repetition, while not overcomplicating. This applies to both problems and answers.

        You will analyze the student's most recent problems (Up to 20 problem attempts) to inform your decisions about their profile and future problem generation.
        Here are their recent attempts (oldest first):
        {attempts_summary}
        Here is a summary of their performance across all attempts:
        {cat_summary}
        </identity>

        
        <profile_structure>
        - Preferred Style: ('visual', 'Learns best with diagrams, charts, and images'), ('auditory', 'Learns best with listening and discussion'), ('reading_writing', 'Learns best with text and notes'),
        ('kinesthetic', 'Learns best with hands-on activities'), ('logical', 'Learns best with reasoning and systems'), ('social', 'Learns best in group settings'),
        ('solitary', 'Learns best independently'), ('nature', 'Learns best through real-world and environmental examples')
        **Be aware that preferred style may not always be represented in problem generation, but should influence your approach when possible.**
        **Nature in this interpretation means real-world examples, not just outdoors or plants**
        - Difficulty: (1, 'Intro', 'Entry-level, simple problems'), (2, 'Core', 'Typical grade-level problems'), (3, 'Challenge', 'Challenging but solvable'),
        (4, 'Advanced', 'Above grade-level complexity'), (5, 'Expert', 'Very difficult, enrichment');
        - Numeric Pref: ('integers_only', 'Whole numbers only'), ('simple_fractions', 'Simple fractions included'), ('decimals', 'Decimals included'),
        ('negatives', 'Negative numbers included'), ('mixed', 'Combination of multiple number types'), ('radicals', 'Square roots or higher roots included');
        - Focus Category: (factual, procedural, strategic, rational); Should be the category the student has most difficulty with or categories the student has little exposure to yet.
            * Focus Category should not be the only category used, but should be an emphasized area where the student needs more practice.
        - Notes: Key insights about the student's interests, challenges, and preferences. 
        ** Use notes to store information you as the tutor have observed about the student that you will want to remember for future problem generation. **
        ** The notes section is your memory of the student, so include anything you think is relevant to help you tutor them better. **
        ** Notes are not only used to keep track of student informaion, but also allow you to make notes to yourself. If you notice question generation is failing to meet constraints, or
        if you believe the questions or answers could be improved, include that in notes for your future reference. **
        ** Still mainain conciseness and relevance. Avoid overly long notes. **
        - AI Goal: ('teach_new', 'Focus on teaching new concepts'), ('challenge', 'Focus on challenging the student'), ('review', 'Focus on reviewing known concepts').
        The student should be in a 'teach_new' mode if they are first learning a topic, haven't performed much across all categories, or have a low performance score.
        They should be in 'challenge' mode if they are doing well (80+ score) and their specific knowledge category they struggle with needs extra focus (70- in that category).
        They should be in 'review' mode if they are consistently performing well (80+ score) or need reinforcement of concepts.
        The student should only rarely be in 'challenge' mode for extended periods; rotate between 'teach_new' and 'review' more often. 
        - Performance Score: A numeric value (0-100) representing overall performance. A student is passing if score >= 70. Though 80+ is ideal.
        </profile_structure>
    """

# AI Algorithm for updating student profile
def Profile_Alg(user_id):

    profile = load_user_profile(user_id)
    context = load_context(profile["user_id"])
    noise = ''.join(random.choices(string.ascii_lowercase, k=4))

    prompt = f"""
        {context}

        <task>
        Analyze student learning patterns and continuously refine an internal learning profile to optimize future problem generation. 
        You do not invent information; you infer patterns only from data provided.
        Analyze the student's last 20 problem attempts and produce a concise, updated student profile.
        The goal is to maintain accurate reflection of the student's learning progress, preferred style,
        and focus areas while adjusting only when justified by clear evidence.
        </task>

       <constraints>
        - ALWAYS use evidence-based reasoning only.
        - ALWAYS keep tone neutral, factual, and analytic (no motivation, emotion, or praise).
        - ALWAYS update 'focus_category' based on weakest category performance.
            * Categories with no attempts should be prioritized
        - ALWAYS Compute Performance Score as the accuracy percentage across the last 20 attempts (or all attempts if fewer than 20).
        - ALWAYS output <Format> exactly as specified. Use <profile_strucure> for context on fields.
        - ALWAYS review your output for consistency and accuracy.
        - NEVER fabricate interests or traits.
        - NEVER modify fields not listed in <format>.  
        - Notes should summarize observed learning behavior and suggest strategies.
            * Include relevant observations on category performance. 
            * Ensure the category balance rules are followed. If not, mention that adjustments are needed.
            (Ex. Out of 20 problems, generally aim for 5 factual, 5 procedural, 5 strategic, 5 rational. If focus_category performance < 70%, aim for ~7 in that category and ~4 in others.
            ONLY exception to this rule set is if overall attempts of any category is 10 + the next highest category. In this case, prioritize the underrepresented category.
            (Ex. If factual=15, procedural=4, strategic=3, rational=2, choose procedural/strategic/rational until factual evens out (<=5 attempts difference next highest))
            * If interest are implemented within problems to frequently, suggest reducing their use in notes.
        - If adjusting difficulty, do so by +/- 1 at most.
        </constraints>

        <Format>
        Preferred Learner Style: ...
        Target Difficulty: ...
        Preferred Length: ...
        Preferred Numeric Complexity: ...
        Focus Category: ...
        Performance Score: ...
        AI Goal: ...
        Notes: ...
        </Format>

        [variation:{noise}]
    """

    try:
        resp = client.models.generate_content(
            model="gemini-2.5-flash-lite",
            contents=[prompt],
            config=types.GenerateContentConfig(
                temperature=0.7,
                max_output_tokens=300
            )
        )
        text = resp.candidates[0].content.parts[0].text.strip()

        # Parse AI output
        updates = {}
        for line in text.splitlines():
            if ":" in line:
                key, value = line.split(":", 1)
                updates[key.strip().lower().replace(" ", "_")] = value.strip()

        # Allowed columns in UserLMSProfile
        allowed_cols = ["preferred_learner_style", "target_difficulty", "preferred_length",
                        "preferred_numeric_complexity", "focus_category", 
                        "performance_score", "ai_goal", "notes"]

        numeric_fields = ["target_difficulty", "performance_score"]

        updates_filtered = {}
        for k, v in updates.items():
            if k in allowed_cols:
                if k in numeric_fields:
                    try:
                        # Keep digits and decimal point
                        num_str = ''.join(c for c in v if c.isdigit() or c == '.')
                        num_val = float(num_str)

                        # Clamp values
                        if k == "performance_score":
                            num_val = max(0, min(100, num_val))   # Performance 0–100%
                        elif k == "target_difficulty":
                            num_val = max(1, min(5, num_val))     # Difficulty 1–5

                        updates_filtered[k] = num_val
                    except:
                        updates_filtered[k] = None  # fallback if parsing fails
                else:
                    updates_filtered[k] = v

        if updates_filtered:
            conn = sqlite3.connect(DB_PATH)
            cur = conn.cursor()

            set_clause = ", ".join([f"{k}=?" for k in updates_filtered.keys()])
            values = list(updates_filtered.values()) + [user_id]

            cur.execute(f"""
                UPDATE UserLMSProfile
                SET {set_clause}
                WHERE user_id=?
            """, values)

            conn.commit()
            conn.close()

    except Exception as e:
        print("Error updating profile:", e)

# Generate a problem using AI
def generate_problem(obj_title, obj_desc, profile):
    context = load_context(profile["user_id"])
    noise = ''.join(random.choices(string.ascii_lowercase, k=4))

    categories = ["factual", "procedural", "strategic", "rational"]
    bias = random.choice(categories)

    prompt = f"""
        {context}

        <task>
        Generate one (1) math problem tailored to the student's profile and learning history.
        You will create a problem for the following Learning Objective:
        Title: {obj_title}
        Description: {obj_desc}
        The problem must be clear, concise, and appropriately challenging.
        </task>

        <constraints>
        - ALWAYS be concise (max 4 sentences for question).
        - ALWAYS include a correct answer.
        - ALWAYS base the output on the following categories: factual, procedural, strategic, rational.
        - ALWAYS output <format> exactly as specified.
        - ALWAYS ensure long-term category balance across multiple generations. This rule supersedes all other constraints:
            * If the student recently had too many of one category, choose a different one. Ideally, rotate categories evenly (25% each if possible).
            * Review the student's recent problems to determine category distribution. 
            (Ex. If they have only been asked 3 of the 4 categories recently, choose the missing one)
            (Ex. If one category is overrepresented, avoid it this time)
            * If the student has not completed 20 problems yet, aim for equal distribution across all categories. (25% each before focus_category adjustments)
            * Favor the student's focus_category if their performance in that category is below 70%. (Split should be 33/67 between focus and others until performance improves).
            * NEVER repeat the same category more than twice in a row UNLESS their performance is below 50% in that category. NEVER repeat more than 3 times in a row.
            * ONLY exception to this rule set is if overall attempts of any category is 10 + the next highest category. In this case, prioritize the underrepresented category.
            (Ex. If factual=15, procedural=4, strategic=3, rational=2, choose procedural/strategic/rational until factual evens out (<=5 attempts difference next highest))
        - Use student interests (from Notes) ONLY when:
            * The student's performance in that category is below 70%.
            * AND the topic benefits from real-world analogies.
            * Student interests should ONLY be used to reinforce engagement or to aid understanding. Interests should NOT be incorporated into every problem.
        - Avoid fabricated interests or irrelevant context.
        - ALWAYS adapt your tone and problem design based on the student's AI goal:
            - If AI Goal = 'teach_new':
                * Favor easier difficulty within the student's target range.
                * Use approachable phrasing.
            - If AI Goal = 'challenge':
                * Slightly increase difficulty beyond their target_difficulty.
                * Only maintain this if the student's overall performance is above 85% AND their focus category performance is above 75%.
            - If AI Goal = 'review':
                * Keep difficulty equal to target_difficulty.
                * Use gentle recap tone or “apply what you know” phrasing.
        - Regardless of goal, maintain category diversity over time.
        - Use word problems appropriately to enhance engagement without overcomplicating. Use ONLY IF needed to create the problem type, introduce variety, align with student interests, or match difficulty.
            * Difficulty levels 4-5 should favor word problems more often. 2-3 should use them sparingly. Level 1 should avoid them unless necessary (likely for factual and rational).
        - ALWAYS review your output for consistency and accuracy. Make sure the problem aligns with all constraints and the student's profile. As the tutor, you should feel that this problem is well-suited to help the student learn effectively.
            * Ensure the category balance rules are followed. (Ex. Out of 20 problems, generally aim for 5 factual, 5 procedural, 5 strategic, 5 rational. If focus_category performance < 70%, aim for ~7 in that category and ~4 in others)
        </constraints>


        <answer_format>
        - Factual / Rational -> short, direct textual responses (less than or equal to 2 sentences) (One word answers are preferred if applicable).
        - Procedural / Strategic -> final numeric or algebraic answer only, no full walkthrough.
        - Do NOT leave the answer blank. 
        </answer_format>

        <format>
        Category: [factual / procedural / strategic / rational]
        Problem: ...
        Answer: ...
        </format>

        [variation:{noise}]
    """

    try:
        resp = client.models.generate_content(
            model="gemini-2.5-flash-lite",
            contents=[prompt],
            config=types.GenerateContentConfig(
                temperature=0.8,
                max_output_tokens=200
            )
        )
        text = resp.candidates[0].content.parts[0].text.strip()

        category = None
        problem = ""
        answer = ""

        # Parse category
        if "Category:" in text:
            after = text.split("Category:")[1].strip()
            category_line = after.splitlines()[0].strip()
            category = category_line.lower()

        # Parse problem & answer
        if "Problem:" in text:
            prob_part = text.split("Problem:")[1]
            if "Answer:" in prob_part:
                prob_text, ans_text = prob_part.split("Answer:")
                problem = prob_text.strip()
                answer = ans_text.strip()
            else:
                problem = prob_part.strip()

        return problem, answer, category

    except Exception as e:
        print("Error generating problem:", e)
        return None, None, None
    
def get_full_performance(user_id):
    conn = sqlite3.connect(DB_PATH)
    cur = conn.cursor()
    cur.execute("""
        SELECT p.category, SUM(pp.is_correct), COUNT(*)
        FROM PracticeProblem pp
        JOIN GenProblem p ON p.id = pp.genProblem_id
        JOIN PracticeProblemSet ps ON ps.id = pp.set_id
        WHERE ps.user_id=?
        GROUP BY p.category
    """, (user_id,))
    rows = cur.fetchall()
    conn.close()

    all_cats = ["factual", "procedural", "strategic", "rational"]
    performance_summary = {cat: 0 for cat in all_cats}

    total_correct = 0
    total_attempts = 0
    for cat, correct, total in rows:
        accuracy = round((correct / total) * 100, 1) if total > 0 else 0
        performance_summary[cat] = accuracy
        total_correct += correct
        total_attempts += total

    overall_score = round((total_correct / total_attempts) * 100, 1) if total_attempts > 0 else 0
    return performance_summary, overall_score

# Insert generated problem into Databasee
def insert_gen_problem(user_id, topic_id, goal_id, obj_id, problem, answer, category):
    conn = sqlite3.connect(DB_PATH)
    cur = conn.cursor()

    cur.execute("""
        INSERT INTO GenProblem (user_id, topic_id, goal_id, objective_id, prompt, correct_answer, category)
        VALUES (?, ?, ?, ?, ?, ?, ?)
    """, (user_id, topic_id, goal_id, obj_id, problem, answer, category))

    pid = cur.lastrowid
    conn.commit()
    conn.close()

    return pid

# Tracks student attempts
def track_attempt(user_id, goal_id, problem_id, student_answer, is_correct):
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

def change_user(_=None):
    global current_user_id
    current_user_id = int(user_var.get())
    refresh_objectives()


user_attempt_count = {}

# Simulate problem generation and answering
def generate_problem_action():
    global user_attempt_count

    selection = listbox.curselection()
    if not selection:
        messagebox.showwarning("No Selection", "Choose an objective.")
        return

    idx = selection[0]
    obj_id, title, desc, goal_id, topic_id, goal_title, topic_title = objectives[idx]

    profile = load_user_profile(current_user_id)

    problem, answer, category = generate_problem(title, desc, profile)
    if not problem:
        messagebox.showerror("Error", "AI failed to generate a problem.")
        return

    # Insert into Database
    pid = insert_gen_problem(current_user_id, topic_id, goal_id, obj_id, problem, answer, category)

    # Simulate student answer
    correct = messagebox.askquestion("Answer", f"{problem}\n\nDid the student answer correctly?")
    is_correct = 1 if correct == "yes" else 0
    student_answer = answer if is_correct else  str(random.randint(1, 999))
    track_attempt(current_user_id, goal_id, pid, student_answer, is_correct)

    user_attempt_count[current_user_id] = user_attempt_count.get(current_user_id, 0) + 1

    # Run Profile_Alg every 5 problems
    if user_attempt_count[current_user_id] % 5 == 0:
        Profile_Alg(current_user_id)

    messagebox.showinfo(
        "Saved",
        f"Generated problem saved for {USERS[current_user_id]}.\n"
        f"Marked as {'Correct' if is_correct else 'Wrong'}.\n\n"
        f"Correct Answer: {answer}\nStudent Answer: {student_answer}"
    )

# View the current user's profile
def view_profile():
    profile = load_user_profile(current_user_id)

    # Accuracy table
    conn = sqlite3.connect(DB_PATH)
    cur = conn.cursor()
    cur.execute("""
        SELECT p.category, SUM(pp.is_correct), COUNT(*)
        FROM PracticeProblem pp
        JOIN GenProblem p ON p.id = pp.genProblem_id
        JOIN PracticeProblemSet ps ON ps.id = pp.set_id
        WHERE ps.user_id=?
        GROUP BY p.category
    """, (current_user_id,))
    rows = cur.fetchall()
    conn.close()

    perf = {cat: {"correct": 0, "wrong": 0} for cat in ["factual","procedural","strategic","rational"]}
    for cat, correct_sum, total in rows:
        perf[cat]["correct"] = correct_sum
        perf[cat]["wrong"] = total - correct_sum

    win = tk.Toplevel(root)
    win.title("Profile")

    # Create a frame for the Treeview
    frame = tk.Frame(win)
    frame.pack(fill=tk.BOTH, expand=True, padx=5, pady=5)

    tree = ttk.Treeview(frame, columns=("Metric", "Value"), show="headings", height=12)
    tree.heading("Metric", text="Metric")
    tree.heading("Value", text="Value")
    tree.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)

    scrollbar = tk.Scrollbar(frame, command=tree.yview)
    scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
    tree.config(yscrollcommand=scrollbar.set)

    # Insert performance metrics first
    for cat, vals in perf.items():
        tree.insert("", tk.END, values=(f"{cat} correct", vals["correct"]))
        tree.insert("", tk.END, values=(f"{cat} wrong", vals["wrong"]))

    # Insert all other profile fields except notes
    for key, value in profile.items():
        if key != "notes":
            tree.insert("", tk.END, values=(key, value))

    # Insert notes at the bottom in a Text widget
    tk.Label(win, text="Notes:").pack(anchor="w", padx=5)
    text_frame = tk.Frame(win)
    text_frame.pack(fill=tk.BOTH, expand=True, padx=5, pady=5)

    text_widget = tk.Text(text_frame, wrap=tk.WORD, height=10)
    text_widget.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)
    text_widget.insert(tk.END, profile.get("notes", ""))
    text_widget.config(state=tk.DISABLED)  # read-only

    scrollbar2 = tk.Scrollbar(text_frame, command=text_widget.yview)
    scrollbar2.pack(side=tk.RIGHT, fill=tk.Y)
    text_widget.config(yscrollcommand=scrollbar2.set)


def fetch_objectives():
    conn = sqlite3.connect(DB_PATH)
    cur = conn.cursor()

    cur.execute("""
        SELECT lo.id, lo.title, lo.description,
               go.id, tp.id, go.title, tp.name
        FROM LearningObjective lo
        JOIN Goal go ON lo.goal_id = go.id
        JOIN Topic tp ON go.topic_id = tp.id
        ORDER BY lo.id
    """)
    data = cur.fetchall()
    conn.close()
    return data

def refresh_objectives():
    global objectives
    objectives = fetch_objectives()

    listbox.delete(0, tk.END)
    for obj_id, title, desc, goal_id, topic_id, goal_title, topic_title in objectives:
        listbox.insert(tk.END, f"{title}  ({topic_title} – {goal_title})")

# GUI
root = tk.Tk()
root.title("AI Student Profile Builder - Demo")

tk.Button(root, text="Reset Database", command=reset_database).pack(pady=5)

tk.Label(root, text="Choose User:").pack(pady=5)
user_var = tk.StringVar(value=current_user_id)
user_menu = ttk.Combobox(root, values=list(USERS.keys()), textvariable=user_var)
user_menu.pack()
user_menu.bind("<<ComboboxSelected>>", change_user)

tk.Label(root, text="Choose Learning Objective:").pack(pady=5)
listbox = tk.Listbox(root, width=100, height=20)
listbox.pack(padx=10, pady=5)

refresh_objectives()

tk.Button(root, text="Generate Problem", command=generate_problem_action).pack(pady=5)
tk.Button(root, text="View Profile", command=view_profile).pack(pady=5)

root.mainloop()