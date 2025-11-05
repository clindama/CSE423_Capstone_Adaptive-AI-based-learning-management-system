"""
Test script to verify enhanced progress tracking works correctly
This creates sample practice data to test the new detailed tracking features
"""

import sqlite3
import os
from datetime import datetime, timedelta

DB_PATH = "learning_platform.db"

def create_sample_practice_data():
    """Create sample practice data for testing the enhanced progress tracking"""
    
    if not os.path.exists(DB_PATH):
        print("❌ ERROR: Database not found!")
        print("Please run: python main.py")
        return False
    
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()
    
    print("=" * 70)
    print("CREATING SAMPLE PRACTICE DATA FOR TESTING")
    print("=" * 70)
    
    # Get a test user (use admin)
    cursor.execute("SELECT id FROM User WHERE username = 'admin'")
    result = cursor.fetchone()
    if not result:
        print("❌ ERROR: Admin user not found!")
        conn.close()
        return False
    
    user_id = result[0]
    print(f"\n✅ Using user ID: {user_id} (admin)")
    
    # Get some topics
    cursor.execute("SELECT id, name FROM Topic LIMIT 2")
    topics = cursor.fetchall()
    
    if not topics:
        print("❌ ERROR: No topics found!")
        conn.close()
        return False
    
    print(f"✅ Found {len(topics)} topics")
    
    sample_problems = [
        {
            "prompt": "Solve for x: x + 5 = 12",
            "correct_answer": "7",
            "student_answer": "7",
            "is_correct": True,
            "category": "procedural"
        },
        {
            "prompt": "Solve for x: 2x = 10",
            "correct_answer": "5",
            "student_answer": "5",
            "is_correct": True,
            "category": "procedural"
        },
        {
            "prompt": "Solve for x: x - 3 = 8",
            "correct_answer": "11",
            "student_answer": "10",
            "is_correct": False,
            "category": "procedural"
        },
        {
            "prompt": "What is the slope-intercept form of a linear equation?",
            "correct_answer": "y = mx + b",
            "student_answer": "y = mx + b",
            "is_correct": True,
            "category": "factual"
        },
        {
            "prompt": "Solve for x: 3x + 7 = 22",
            "correct_answer": "5",
            "student_answer": "6",
            "is_correct": False,
            "category": "procedural"
        },
    ]
    
    created_count = 0
    
    for topic_id, topic_name in topics:
        print(f"\n📚 Creating practice data for topic: {topic_name}")
        
        # Get goals for this topic
        cursor.execute("SELECT id, title FROM Goal WHERE topic_id = ? LIMIT 2", (topic_id,))
        goals = cursor.fetchall()
        
        for goal_id, goal_title in goals:
            print(f"  🎯 Goal: {goal_title}")
            
            # Get objectives for this goal
            cursor.execute("SELECT id FROM LearningObjective WHERE goal_id = ? LIMIT 1", (goal_id,))
            obj_result = cursor.fetchone()
            
            if not obj_result:
                continue
            
            objective_id = obj_result[0]
            
            # Create practice set
            cursor.execute("""
                INSERT INTO PracticeProblemSet (user_id, goal_id, start_time)
                VALUES (?, ?, ?)
            """, (user_id, goal_id, datetime.now() - timedelta(days=created_count)))
            set_id = cursor.lastrowid
            
            # Create 2-3 problems for this goal
            num_problems = min(3, len(sample_problems))
            for i in range(num_problems):
                problem = sample_problems[i % len(sample_problems)]
                
                # Create GenProblem
                cursor.execute("""
                    INSERT INTO GenProblem (user_id, topic_id, goal_id, objective_id, 
                                           prompt, correct_answer, category)
                    VALUES (?, ?, ?, ?, ?, ?, ?)
                """, (user_id, topic_id, goal_id, objective_id, 
                     problem["prompt"], problem["correct_answer"], problem["category"]))
                gen_problem_id = cursor.lastrowid
                
                # Create PracticeProblem
                cursor.execute("""
                    INSERT INTO PracticeProblem (set_id, problem_id, student_answer, 
                                                is_correct, is_completed)
                    VALUES (?, ?, ?, ?, TRUE)
                """, (set_id, gen_problem_id, problem["student_answer"], problem["is_correct"]))
                
                created_count += 1
                status = "✓" if problem["is_correct"] else "✗"
                print(f"    {status} Created problem: {problem['prompt'][:50]}...")
    
    conn.commit()
    conn.close()
    
    print("\n" + "=" * 70)
    print(f"✅ Successfully created {created_count} practice problems!")
    print("=" * 70)
    print("\n🚀 Now run: python unified_app.py")
    print("   Then click 'View Progress' to see the enhanced tracking!")
    print()
    
    return True

def clear_practice_data():
    """Clear all practice data (for testing)"""
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()
    
    print("\n🧹 Clearing existing practice data...")
    cursor.execute("DELETE FROM PracticeProblem")
    cursor.execute("DELETE FROM PracticeProblemSet")
    cursor.execute("DELETE FROM GenProblem")
    
    conn.commit()
    conn.close()
    print("✅ Practice data cleared!")

if __name__ == "__main__":
    print("\n" + "=" * 70)
    print("ENHANCED PROGRESS TRACKING TEST")
    print("=" * 70)
    print("\nThis script will create sample practice data to test the new features:")
    print("  • Detailed practice history grouped by topic")
    print("  • Tabbed interface for each topic")
    print("  • Individual problem cards with all details")
    print("  • AI Feedback button for each attempt")
    print()
    
    response = input("Do you want to clear existing practice data first? (y/n): ").lower()
    if response == 'y':
        clear_practice_data()
    
    success = create_sample_practice_data()
    
    if success:
        print("\n" + "=" * 70)
        print("✅ TEST DATA CREATED SUCCESSFULLY!")
        print("=" * 70)
        print("\nNext steps:")
        print("1. Run: python unified_app.py")
        print("2. Login with admin/1234")
        print("3. Click '📊 View Progress'")
        print("4. You should see:")
        print("   • Topic progress bars with percentages")
        print("   • Tabs for each topic with practice history")
        print("   • Detailed cards for each problem attempt")
        print("   • '🤖 Get AI Feedback' button on each card")
        print()
    else:
        print("\n❌ Failed to create test data!")
        exit(1)

