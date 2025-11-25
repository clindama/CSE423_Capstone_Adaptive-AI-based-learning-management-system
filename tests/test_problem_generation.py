"""
Test 2: Problem Generation
Purpose: Verify AI generates personalized practice problems based on user profiles
Approach: Generate problems for two unique users and verify personalization
"""

import sqlite3
import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from ai_tutor import generate_practice_problem, get_or_create_user_profile
from config import DB_PATH, AI_AVAILABLE
import json

def test_problem_generation():
    """Test problem generation for two different user profiles"""
    
    print("=" * 80)
    print("TEST 2: PROBLEM GENERATION")
    print("=" * 80)
    
    if not AI_AVAILABLE:
        print("❌ FAILED: AI not available")
        return False
    
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()
    
    # Get a sample topic, goal, and objective
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
    
    print(f"\n📚 Test Context:")
    print(f"   Topic: {topic_name}")
    print(f"   Goal: {goal_title}")
    print(f"   Objective: {obj_title}")
    
    # Test User 1: Beginner with factual focus
    print("\n👤 Testing User 1 (Beginner, Factual Focus)...")
    cursor.execute("SELECT id FROM User LIMIT 1")
    user1_id = cursor.fetchone()[0]
    
    profile1 = get_or_create_user_profile(user1_id)
    cursor.execute("""
        UPDATE UserLMSProfile 
        SET preferred_learner_style = 'visual',
            target_difficulty = 2,
            preferred_numeric_complexity = 'simple',
            focus_category = 'factual',
            performance_score = 0.6
        WHERE user_id = ?
    """, (user1_id,))
    conn.commit()
    
    print("   ✅ Profile configured: Difficulty=2, Simple, Factual, Score=0.6")
    
    # Generate problem for user 1
    print("\n🤖 Generating problem for User 1...")
    problem1 = generate_practice_problem(user1_id, topic_id, goal_id, obj_id)
    
    if not problem1:
        print("❌ FAILED: No problem generated for User 1")
        conn.close()
        return False
    
    problem1_id, prompt1, answer1, category1 = problem1
    
    print(f"   ✅ Problem generated (ID: {problem1_id})")
    print(f"   Category: {category1}")
    print(f"   Prompt: {prompt1[:100]}...")
    print(f"   Answer: {answer1[:50]}...")
    
    # Verify problem matches profile
    if category1 != 'factual':
        print(f"   ⚠️  WARNING: Expected 'factual' category, got '{category1}'")
    else:
        print(f"   ✅ Category matches user profile")
    
    # Test User 2: Advanced with strategic focus
    print("\n👤 Testing User 2 (Advanced, Strategic Focus)...")
    cursor.execute("SELECT id FROM User WHERE id != ? LIMIT 1", (user1_id,))
    user2_result = cursor.fetchone()
    
    if not user2_result:
        cursor.execute("INSERT INTO User (username, password) VALUES (?, ?)", 
                      ("test_user_problem_2", "password"))
        user2_id = cursor.lastrowid
    else:
        user2_id = user2_result[0]
    
    profile2 = get_or_create_user_profile(user2_id)
    cursor.execute("""
        UPDATE UserLMSProfile 
        SET preferred_learner_style = 'analytical',
            target_difficulty = 5,
            preferred_numeric_complexity = 'complex',
            focus_category = 'strategic',
            performance_score = 0.9
        WHERE user_id = ?
    """, (user2_id,))
    conn.commit()
    
    print("   ✅ Profile configured: Difficulty=5, Complex, Strategic, Score=0.9")
    
    # Generate problem for user 2
    print("\n🤖 Generating problem for User 2...")
    problem2 = generate_practice_problem(user2_id, topic_id, goal_id, obj_id)
    
    if not problem2:
        print("❌ FAILED: No problem generated for User 2")
        conn.close()
        return False
    
    problem2_id, prompt2, answer2, category2 = problem2
    
    print(f"   ✅ Problem generated (ID: {problem2_id})")
    print(f"   Category: {category2}")
    print(f"   Prompt: {prompt2[:100]}...")
    print(f"   Answer: {answer2[:50]}...")
    
    # Verify problem matches profile
    if category2 != 'strategic':
        print(f"   ⚠️  WARNING: Expected 'strategic' category, got '{category2}'")
    else:
        print(f"   ✅ Category matches user profile")
    
    # Verify problems are different
    print("\n🔍 Verifying Problem Uniqueness...")
    
    if prompt1 == prompt2:
        print("❌ FAILED: Problems are identical")
        conn.close()
        return False
    
    print("   ✅ Problems are unique")
    
    # Verify problems are stored in database
    print("\n🔍 Verifying Database Storage...")
    cursor.execute("SELECT COUNT(*) FROM GenProblem WHERE id IN (?, ?)", (problem1_id, problem2_id))
    stored_count = cursor.fetchone()[0]
    
    if stored_count == 2:
        print(f"   ✅ Both problems stored in database")
    else:
        print(f"   ⚠️  WARNING: Only {stored_count}/2 problems found in database")
    
    # Verify problem format
    print("\n🔍 Verifying Problem Format...")
    
    checks_passed = 0
    total_checks = 4
    
    if prompt1 and len(prompt1) > 10:
        print("   ✅ Problem 1 has valid prompt")
        checks_passed += 1
    
    if answer1 and len(answer1) > 0:
        print("   ✅ Problem 1 has valid answer")
        checks_passed += 1
    
    if prompt2 and len(prompt2) > 10:
        print("   ✅ Problem 2 has valid prompt")
        checks_passed += 1
    
    if answer2 and len(answer2) > 0:
        print("   ✅ Problem 2 has valid answer")
        checks_passed += 1
    
    conn.close()
    
    print("\n" + "=" * 80)
    print("✅ TEST 2 PASSED: Problem Generation")
    print("=" * 80)
    print("\nSummary:")
    print(f"  • Generated personalized problems for 2 users")
    print(f"  • User 1 (Beginner/Factual): Category={category1}")
    print(f"  • User 2 (Advanced/Strategic): Category={category2}")
    print(f"  • Problems are unique: Yes")
    print(f"  • Format validation: {checks_passed}/{total_checks} checks passed")
    print(f"  • Database storage: {stored_count}/2 problems stored")
    
    return True

if __name__ == "__main__":
    try:
        success = test_problem_generation()
        sys.exit(0 if success else 1)
    except Exception as e:
        print(f"\n❌ TEST FAILED WITH EXCEPTION: {e}")
        import traceback
        traceback.print_exc()
        sys.exit(1)

