"""
Database Operations Module
Handles all database queries and operations for the Learning Management System
"""

import sqlite3
from config import DB_PATH


# ==================== USER OPERATIONS ====================

def get_user_by_id(user_id):
    """Get user information by ID"""
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()
    cursor.execute("SELECT username, first_name, last_name, email FROM User WHERE id = ?", (user_id,))
    result = cursor.fetchone()
    conn.close()
    return result


# ==================== TOPIC OPERATIONS ====================

def fetch_all_topics():
    """Fetch all topics from database"""
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()
    cursor.execute("SELECT id, name FROM Topic ORDER BY topic_order")
    topics = cursor.fetchall()
    conn.close()
    return topics


def fetch_goals_for_topic(topic_name):
    """Fetch all goals for a specific topic"""
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()
    cursor.execute("""
        SELECT g.id, g.title, g.description
        FROM Goal g
        JOIN Topic t ON g.topic_id = t.id
        WHERE t.name = ?
        ORDER BY g.goal_order
    """, (topic_name,))
    goals = cursor.fetchall()
    conn.close()
    return goals


def fetch_objectives_for_goal(goal_id):
    """Fetch all learning objectives for a specific goal"""
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()
    cursor.execute("""
        SELECT id, title, description
        FROM LearningObjective
        WHERE goal_id = ?
        ORDER BY obj_order
    """, (goal_id,))
    objectives = cursor.fetchall()
    conn.close()
    return objectives


def get_topic_id_by_name(topic_name):
    """Get topic ID by topic name"""
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()
    cursor.execute("SELECT id FROM Topic WHERE name = ?", (topic_name,))
    result = cursor.fetchone()
    conn.close()
    return result[0] if result else None


def get_goal_info(goal_id):
    """Get goal information including topic"""
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()
    cursor.execute("""
        SELECT g.title, t.name, t.id
        FROM Goal g
        JOIN Topic t ON g.topic_id = t.id
        WHERE g.id = ?
    """, (goal_id,))
    result = cursor.fetchone()
    conn.close()
    return result


def get_objective_details(objective_id):
    """Get objective details"""
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()
    cursor.execute("SELECT title, description FROM LearningObjective WHERE id = ?", (objective_id,))
    result = cursor.fetchone()
    conn.close()
    return result


# ==================== PROBLEM OPERATIONS ====================

def save_generated_problem(user_id, topic_id, goal_id, objective_id, problem, answer, category):
    """Save AI-generated problem to database"""
    try:
        conn = sqlite3.connect(DB_PATH)
        cur = conn.cursor()

        cur.execute("""
            INSERT INTO GenProblem (user_id, topic_id, goal_id, objective_id, prompt, correct_answer, category)
            VALUES (?, ?, ?, ?, ?, ?, ?)
        """, (user_id, topic_id, goal_id, objective_id, problem, answer, category))

        pid = cur.lastrowid
        conn.commit()
        conn.close()
        return pid
    except sqlite3.OperationalError as e:
        if "no such table" in str(e):
            print(f"ERROR: {e}")
            print("Please run: python add_ai_tables.py")
            raise
        raise


def record_practice_attempt(user_id, goal_id, problem_id, student_answer, is_correct):
    """Record a practice problem attempt"""
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


def get_practice_history(user_id, limit=20):
    """Get practice problem history for a user"""
    conn = sqlite3.connect(DB_PATH)
    cur = conn.cursor()
    
    cur.execute("""
    SELECT pp.id, p.category, p.prompt, pp.student_answer, pp.is_correct
    FROM PracticeProblem pp
    JOIN GenProblem p ON p.id = pp.genProblem_id
    JOIN PracticeProblemSet ps ON ps.id = pp.set_id
    WHERE ps.user_id=?
    ORDER BY pp.id DESC
    LIMIT ?
    """, (user_id, limit))
    
    attempts = cur.fetchall()
    conn.close()
    return attempts

