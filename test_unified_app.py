"""
Test script to verify all database operations work correctly
Run this before using unified_app.py to ensure everything is set up properly
"""

import sqlite3
import os

DB_PATH = "learning_platform.db"

def test_database():
    """Test all database tables and operations"""
    
    print("=" * 70)
    print("TESTING UNIFIED APP DATABASE")
    print("=" * 70)
    
    if not os.path.exists(DB_PATH):
        print("\n❌ ERROR: Database not found!")
        print("Please run: python main.py")
        return False
    
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()
    
    # Get all tables
    cursor.execute("SELECT name FROM sqlite_master WHERE type='table' ORDER BY name")
    tables = [row[0] for row in cursor.fetchall()]
    
    print(f"\n✅ Database found: {DB_PATH}")
    print(f"📊 Total tables: {len(tables)}")
    
    # Required tables for unified app
    required_tables = {
        'User': 'User authentication',
        'Topic': 'Learning topics',
        'Goal': 'Learning goals',
        'LearningObjective': 'Learning objectives',
        'TopicProgress': 'Topic progress tracking',
        'GoalProgress': 'Goal progress tracking',
        'GenProblem': 'AI-generated problems',
        'PracticeProblemSet': 'Practice problem sets',
        'PracticeProblem': 'Individual practice attempts'
    }
    
    print("\n" + "=" * 70)
    print("CHECKING REQUIRED TABLES")
    print("=" * 70)
    
    all_present = True
    for table, description in required_tables.items():
        if table in tables:
            print(f"✅ {table:25} - {description}")
        else:
            print(f"❌ {table:25} - MISSING! {description}")
            all_present = False
    
    if not all_present:
        print("\n⚠️  Missing tables detected!")
        if 'GenProblem' not in tables:
            print("   Run: python add_ai_tables.py")
        return False
    
    # Check table schemas
    print("\n" + "=" * 70)
    print("CHECKING TABLE SCHEMAS")
    print("=" * 70)
    
    # Check PracticeProblem columns
    cursor.execute("PRAGMA table_info(PracticeProblem)")
    columns = {row[1]: row[2] for row in cursor.fetchall()}
    
    print("\n📋 PracticeProblem columns:")
    for col, dtype in columns.items():
        print(f"   - {col:20} ({dtype})")
    
    if 'problem_id' not in columns:
        print("   ❌ ERROR: Missing 'problem_id' column!")
        return False
    else:
        print("   ✅ Correct schema (uses 'problem_id')")
    
    # Check GenProblem columns
    cursor.execute("PRAGMA table_info(GenProblem)")
    gen_columns = {row[1]: row[2] for row in cursor.fetchall()}
    
    print("\n📋 GenProblem columns:")
    for col, dtype in gen_columns.items():
        print(f"   - {col:20} ({dtype})")
    
    required_gen_cols = ['id', 'user_id', 'topic_id', 'goal_id', 'objective_id', 'prompt', 'correct_answer', 'category']
    missing_cols = [col for col in required_gen_cols if col not in gen_columns]
    
    if missing_cols:
        print(f"   ❌ ERROR: Missing columns: {', '.join(missing_cols)}")
        return False
    else:
        print("   ✅ All required columns present")
    
    # Test data presence
    print("\n" + "=" * 70)
    print("CHECKING DATA")
    print("=" * 70)
    
    # Check users
    cursor.execute("SELECT COUNT(*) FROM User")
    user_count = cursor.fetchone()[0]
    print(f"\n👥 Users: {user_count}")
    if user_count == 0:
        print("   ⚠️  No users found. You'll need to register.")
    else:
        cursor.execute("SELECT username FROM User LIMIT 5")
        users = [row[0] for row in cursor.fetchall()]
        print(f"   Sample users: {', '.join(users)}")
    
    # Check topics
    cursor.execute("SELECT COUNT(*) FROM Topic")
    topic_count = cursor.fetchone()[0]
    print(f"\n📚 Topics: {topic_count}")
    if topic_count == 0:
        print("   ❌ ERROR: No topics found! Run: python main.py")
        return False
    else:
        cursor.execute("SELECT name FROM Topic LIMIT 3")
        topics = [row[0] for row in cursor.fetchall()]
        print(f"   Sample topics: {', '.join(topics)}")
    
    # Check goals
    cursor.execute("SELECT COUNT(*) FROM Goal")
    goal_count = cursor.fetchone()[0]
    print(f"\n🎯 Goals: {goal_count}")
    if goal_count == 0:
        print("   ⚠️  No goals found.")
    
    # Check objectives
    cursor.execute("SELECT COUNT(*) FROM LearningObjective")
    obj_count = cursor.fetchone()[0]
    print(f"\n📝 Learning Objectives: {obj_count}")
    if obj_count == 0:
        print("   ⚠️  No learning objectives found.")
    
    # Test insert operations
    print("\n" + "=" * 70)
    print("TESTING DATABASE OPERATIONS")
    print("=" * 70)
    
    try:
        # Test GenProblem insert
        print("\n🧪 Testing GenProblem insert...", end=" ")
        cursor.execute("""
            INSERT INTO GenProblem (user_id, topic_id, goal_id, objective_id, prompt, correct_answer, category)
            VALUES (1, 1, 1, 1, 'Test problem', 'Test answer', 'factual')
        """)
        test_problem_id = cursor.lastrowid
        print(f"✅ (ID: {test_problem_id})")
        
        # Test PracticeProblemSet insert
        print("🧪 Testing PracticeProblemSet insert...", end=" ")
        cursor.execute("""
            INSERT INTO PracticeProblemSet (user_id, goal_id)
            VALUES (1, 1)
        """)
        test_set_id = cursor.lastrowid
        print(f"✅ (ID: {test_set_id})")
        
        # Test PracticeProblem insert with correct column name
        print("🧪 Testing PracticeProblem insert...", end=" ")
        cursor.execute("""
            INSERT INTO PracticeProblem (set_id, problem_id, student_answer, is_correct, is_completed)
            VALUES (?, ?, 'Test answer', TRUE, TRUE)
        """, (test_set_id, test_problem_id))
        test_practice_id = cursor.lastrowid
        print(f"✅ (ID: {test_practice_id})")
        
        # Clean up test data
        print("🧹 Cleaning up test data...", end=" ")
        cursor.execute("DELETE FROM PracticeProblem WHERE id = ?", (test_practice_id,))
        cursor.execute("DELETE FROM PracticeProblemSet WHERE id = ?", (test_set_id,))
        cursor.execute("DELETE FROM GenProblem WHERE id = ?", (test_problem_id,))
        conn.commit()
        print("✅")
        
    except sqlite3.Error as e:
        print(f"\n❌ ERROR: {e}")
        conn.rollback()
        conn.close()
        return False
    
    conn.close()
    
    print("\n" + "=" * 70)
    print("✅ ALL TESTS PASSED!")
    print("=" * 70)
    print("\n🚀 You can now run: python unified_app.py")
    print()
    
    return True

if __name__ == "__main__":
    success = test_database()
    exit(0 if success else 1)

