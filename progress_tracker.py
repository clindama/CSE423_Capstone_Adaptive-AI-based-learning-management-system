"""
Progress Tracking Module
Handles all progress tracking and reporting functionality
"""

import sqlite3
from config import DB_PATH


def update_topic_progress(user_id, topic_id, progress_increment):
    """Update user's progress for a topic"""
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()
    
    # Check if progress record exists
    cursor.execute("""
        SELECT progress FROM TopicProgress 
        WHERE user_id = ? AND topic_id = ?
    """, (user_id, topic_id))
    
    result = cursor.fetchone()
    
    if result:
        # Update existing progress
        new_progress = min(100, result[0] + progress_increment)
        cursor.execute("""
            UPDATE TopicProgress 
            SET progress = ? 
            WHERE user_id = ? AND topic_id = ?
        """, (new_progress, user_id, topic_id))
    else:
        # Create new progress record
        cursor.execute("""
            INSERT INTO TopicProgress (user_id, topic_id, progress)
            VALUES (?, ?, ?)
        """, (user_id, topic_id, min(100, progress_increment)))
    
    conn.commit()
    conn.close()


def update_goal_progress(user_id, goal_id, correct_count, total_count):
    """Update user's progress for a goal"""
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()
    
    # Calculate grade as percentage
    grade = int((correct_count / total_count) * 100) if total_count > 0 else 0
    
    # Check if progress record exists
    cursor.execute("""
        SELECT grade FROM GoalProgress 
        WHERE user_id = ? AND goal_id = ?
    """, (user_id, goal_id))
    
    result = cursor.fetchone()
    
    if result:
        # Update existing progress (take the better grade)
        new_grade = max(result[0], grade)
        cursor.execute("""
            UPDATE GoalProgress 
            SET grade = ?, is_completed = ?
            WHERE user_id = ? AND goal_id = ?
        """, (new_grade, new_grade >= 90, user_id, goal_id))
    else:
        # Create new progress record
        cursor.execute("""
            INSERT INTO GoalProgress (user_id, goal_id, grade, is_completed)
            VALUES (?, ?, ?, ?)
        """, (user_id, goal_id, grade, grade >= 90))
    
    conn.commit()
    conn.close()


def get_user_progress_summary(user_id):
    """Get comprehensive progress summary for a user"""
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()
    
    # Get topic progress
    cursor.execute("""
        SELECT t.name, tp.progress
        FROM TopicProgress tp
        JOIN Topic t ON tp.topic_id = t.id
        WHERE tp.user_id = ?
        ORDER BY t.topic_order
    """, (user_id,))
    topic_progress = cursor.fetchall()
    
    # Get goal progress
    cursor.execute("""
        SELECT g.title, gp.grade, gp.is_completed, t.name
        FROM GoalProgress gp
        JOIN Goal g ON gp.goal_id = g.id
        JOIN Topic t ON g.topic_id = t.id
        WHERE gp.user_id = ?
        ORDER BY t.topic_order, g.goal_order
    """, (user_id,))
    goal_progress = cursor.fetchall()
    
    # Get overall statistics
    cursor.execute("""
        SELECT COUNT(*), AVG(grade)
        FROM GoalProgress
        WHERE user_id = ?
    """, (user_id,))
    stats = cursor.fetchone()
    
    conn.close()
    
    return {
        'topics': topic_progress,
        'goals': goal_progress,
        'total_goals': stats[0] if stats else 0,
        'average_grade': stats[1] if stats and stats[1] else 0
    }


def get_practice_statistics(user_id):
    """Get practice problem statistics for a user"""
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()
    
    # Get overall statistics
    cursor.execute("""
        SELECT 
            COUNT(*) as total_problems,
            SUM(CASE WHEN pp.is_correct = 1 THEN 1 ELSE 0 END) as correct_count
        FROM PracticeProblem pp
        JOIN PracticeProblemSet ps ON pp.set_id = ps.id
        WHERE ps.user_id = ?
    """, (user_id,))
    
    overall = cursor.fetchone()
    
    # Get statistics by category
    cursor.execute("""
        SELECT 
            gp.category,
            COUNT(*) as total,
            SUM(CASE WHEN pp.is_correct = 1 THEN 1 ELSE 0 END) as correct
        FROM PracticeProblem pp
        JOIN GenProblem gp ON pp.genProblem_id = gp.id
        JOIN PracticeProblemSet ps ON pp.set_id = ps.id
        WHERE ps.user_id = ?
        GROUP BY gp.category
    """, (user_id,))
    
    by_category = cursor.fetchall()
    conn.close()
    
    return {
        'total_problems': overall[0] if overall else 0,
        'correct_count': overall[1] if overall else 0,
        'accuracy': (overall[1] / overall[0] * 100) if overall and overall[0] > 0 else 0,
        'by_category': by_category
    }

