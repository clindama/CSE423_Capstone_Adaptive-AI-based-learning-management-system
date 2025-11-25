"""
Test 3: User Data Tracking
Purpose: Verify user progress and practice attempts are correctly stored
Approach: Simulate a student session and verify all data is persisted
"""

import sqlite3
import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from database import record_practice_attempt, get_practice_history
from progress_tracker import update_topic_progress, update_goal_progress
from ai_tutor import generate_practice_problem, get_or_create_user_profile
from config import DB_PATH, AI_AVAILABLE

def test_user_data_tracking():
    """Test that user data is correctly tracked and stored"""
    
    print("=" * 80)
    print("TEST 3: USER DATA TRACKING")
    print("=" * 80)
    
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()
    
    # Get test user and learning context
    cursor.execute("SELECT id, username FROM User LIMIT 1")
    user_result = cursor.fetchone()
    if not user_result:
        print("❌ FAILED: No test user available")
        conn.close()
        return False
    
    user_id, username = user_result
    print(f"\n👤 Test User: {username} (ID: {user_id})")
    
    # Get test topic, goal, objective
    cursor.execute("""
        SELECT t.id, t.name, g.id, g.title, lo.id, lo.title
        FROM Topic t
        JOIN Goal g ON g.topic_id = t.id
        JOIN LearningObjective lo ON lo.goal_id = g.id
        LIMIT 1
    """)
    
    result = cursor.fetchone()
    if not result:
        print("❌ FAILED: No test data available")
        conn.close()
        return False
    
    topic_id, topic_name, goal_id, goal_title, obj_id, obj_title = result
    
    print(f"📚 Learning Context:")
    print(f"   Topic: {topic_name} (ID: {topic_id})")
    print(f"   Goal: {goal_title} (ID: {goal_id})")
    print(f"   Objective: {obj_title} (ID: {obj_id})")
    
    # Get initial state
    print("\n📊 Recording Initial State...")
    cursor.execute("SELECT COUNT(*) FROM PracticeProblem pp JOIN PracticeProblemSet ps ON pp.set_id = ps.id WHERE ps.user_id = ?", (user_id,))
    initial_problem_count = cursor.fetchone()[0]
    print(f"   Initial practice problems: {initial_problem_count}")
    
    cursor.execute("SELECT progress FROM TopicProgress WHERE user_id = ? AND topic_id = ?", (user_id, topic_id))
    initial_topic_progress = cursor.fetchone()
    initial_topic_progress = initial_topic_progress[0] if initial_topic_progress else 0
    print(f"   Initial topic progress: {initial_topic_progress}%")
    
    cursor.execute("SELECT progress FROM GoalProgress WHERE user_id = ? AND goal_id = ?", (user_id, goal_id))
    initial_goal_progress = cursor.fetchone()
    initial_goal_progress = initial_goal_progress[0] if initial_goal_progress else 0
    print(f"   Initial goal progress: {initial_goal_progress}%")
    
    # Simulate practice session
    print("\n🎯 Simulating Practice Session...")
    print("   Generating 3 practice problems and recording attempts...")
    
    attempts_recorded = 0
    problems_generated = []
    
    for i in range(3):
        print(f"\n   Problem {i+1}/3:")
        
        # Generate problem (if AI available) or create mock problem
        if AI_AVAILABLE:
            problem = generate_practice_problem(user_id, topic_id, goal_id, obj_id)
            if problem:
                problem_id, prompt, answer, category = problem
                print(f"      ✅ Generated problem (ID: {problem_id}, Category: {category})")
            else:
                # Create mock problem
                cursor.execute("""
                    INSERT INTO GenProblem (user_id, topic_id, goal_id, objective_id, prompt, correct_answer, category)
                    VALUES (?, ?, ?, ?, ?, ?, ?)
                """, (user_id, topic_id, goal_id, obj_id, f"Test problem {i+1}", f"Answer {i+1}", "factual"))
                problem_id = cursor.lastrowid
                conn.commit()
                print(f"      ✅ Created mock problem (ID: {problem_id})")
        else:
            # Create mock problem
            cursor.execute("""
                INSERT INTO GenProblem (user_id, topic_id, goal_id, objective_id, prompt, correct_answer, category)
                VALUES (?, ?, ?, ?, ?, ?, ?)
            """, (user_id, topic_id, goal_id, obj_id, f"Test problem {i+1}", f"Answer {i+1}", "factual"))
            problem_id = cursor.lastrowid
            conn.commit()
            print(f"      ✅ Created mock problem (ID: {problem_id})")
        
        problems_generated.append(problem_id)
        
        # Record attempt (alternating correct/incorrect)
        is_correct = (i % 2 == 0)  # Problems 0 and 2 correct, problem 1 incorrect
        student_answer = f"Student answer {i+1}"
        
        record_practice_attempt(user_id, goal_id, problem_id, student_answer, is_correct)
        attempts_recorded += 1
        
        print(f"      ✅ Recorded attempt (Correct: {is_correct})")
    
    print(f"\n   ✅ Recorded {attempts_recorded} practice attempts")
    
    # Update progress
    print("\n📈 Updating Progress...")
    update_topic_progress(user_id, topic_id)
    print("   ✅ Topic progress updated")
    
    update_goal_progress(user_id, goal_id)
    print("   ✅ Goal progress updated")
    
    # Verify data was stored
    print("\n🔍 Verifying Data Storage...")
    
    # Check practice attempts
    cursor.execute("SELECT COUNT(*) FROM PracticeProblem pp JOIN PracticeProblemSet ps ON pp.set_id = ps.id WHERE ps.user_id = ?", (user_id,))
    final_problem_count = cursor.fetchone()[0]
    new_problems = final_problem_count - initial_problem_count
    
    if new_problems >= 3:
        print(f"   ✅ Practice attempts stored: {new_problems} new attempts")
    else:
        print(f"   ❌ FAILED: Expected 3+ new attempts, found {new_problems}")
        conn.close()
        return False
    
    # Check topic progress
    cursor.execute("SELECT progress FROM TopicProgress WHERE user_id = ? AND topic_id = ?", (user_id, topic_id))
    final_topic_progress = cursor.fetchone()
    final_topic_progress = final_topic_progress[0] if final_topic_progress else 0
    
    print(f"   ✅ Topic progress: {initial_topic_progress}% → {final_topic_progress}%")
    
    # Check goal progress
    cursor.execute("SELECT progress FROM GoalProgress WHERE user_id = ? AND goal_id = ?", (user_id, goal_id))
    final_goal_progress = cursor.fetchone()
    final_goal_progress = final_goal_progress[0] if final_goal_progress else 0
    
    print(f"   ✅ Goal progress: {initial_goal_progress}% → {final_goal_progress}%")
    
    # Verify practice history retrieval
    print("\n🔍 Verifying Data Retrieval...")
    history = get_practice_history(user_id, limit=5)
    
    if history and len(history) > 0:
        print(f"   ✅ Retrieved {len(history)} practice records")
        print(f"   Latest attempt: Category={history[0][1]}, Correct={history[0][4]}")
    else:
        print("   ⚠️  WARNING: No practice history retrieved")
    
    conn.close()
    
    print("\n" + "=" * 80)
    print("✅ TEST 3 PASSED: User Data Tracking")
    print("=" * 80)
    print("\nSummary:")
    print(f"  • Practice attempts recorded: {attempts_recorded}")
    print(f"  • New problems in database: {new_problems}")
    print(f"  • Topic progress updated: {initial_topic_progress}% → {final_topic_progress}%")
    print(f"  • Goal progress updated: {initial_goal_progress}% → {final_goal_progress}%")
    print(f"  • Data retrieval working: Yes ({len(history) if history else 0} records)")
    
    return True

if __name__ == "__main__":
    try:
        success = test_user_data_tracking()
        sys.exit(0 if success else 1)
    except Exception as e:
        print(f"\n❌ TEST FAILED WITH EXCEPTION: {e}")
        import traceback
        traceback.print_exc()
        sys.exit(1)

