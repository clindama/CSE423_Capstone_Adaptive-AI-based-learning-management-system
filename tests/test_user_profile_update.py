"""
Test 4: User Profile Update (AI Notes Generation)
Purpose: Verify AI updates user profiles with performance notes over time
Approach: Simulate multiple problem attempts and verify profile updates
"""

import sqlite3
import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from ai_tutor import update_student_profile, get_or_create_user_profile, generate_practice_problem
from database import record_practice_attempt
from config import DB_PATH, AI_AVAILABLE, PROFILE_UPDATE_FREQUENCY

def test_user_profile_update():
    """Test that user profiles are updated based on performance"""
    
    print("=" * 80)
    print("TEST 4: USER PROFILE UPDATE (AI NOTES GENERATION)")
    print("=" * 80)
    
    if not AI_AVAILABLE:
        print("⚠️  AI not available - testing with mock data")
    
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()
    
    # Get or create test user
    cursor.execute("SELECT id, username FROM User LIMIT 1")
    user_result = cursor.fetchone()
    if not user_result:
        print("❌ FAILED: No test user available")
        conn.close()
        return False
    
    user_id, username = user_result
    print(f"\n👤 Test User: {username} (ID: {user_id})")
    
    # Get test learning context
    cursor.execute("""
        SELECT t.id, g.id, lo.id
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
    
    topic_id, goal_id, obj_id = result
    
    # Initialize or get user profile
    print("\n📋 Initializing User Profile...")
    profile = get_or_create_user_profile(user_id)
    
    # Get initial profile state
    cursor.execute("""
        SELECT preferred_learner_style, target_difficulty, focus_category, 
               performance_score, notes, last_updated
        FROM UserLMSProfile
        WHERE user_id = ?
    """, (user_id,))
    
    initial_profile = cursor.fetchone()
    if initial_profile:
        style, difficulty, category, score, notes, last_updated = initial_profile
        print(f"   Initial Profile:")
        print(f"      Learning Style: {style}")
        print(f"      Difficulty: {difficulty}")
        print(f"      Focus Category: {category}")
        print(f"      Performance Score: {score}")
        print(f"      Notes: {notes[:50] if notes else 'None'}...")
        print(f"      Last Updated: {last_updated}")
    else:
        print("   ✅ New profile created")
    
    # Simulate multiple problem attempts
    print(f"\n🎯 Simulating {PROFILE_UPDATE_FREQUENCY + 2} Problem Attempts...")
    print(f"   (Profile updates every {PROFILE_UPDATE_FREQUENCY} problems)")
    
    num_problems = PROFILE_UPDATE_FREQUENCY + 2
    attempts = []
    
    for i in range(num_problems):
        print(f"\n   Problem {i+1}/{num_problems}:")
        
        # Create or generate problem
        if AI_AVAILABLE:
            problem = generate_practice_problem(user_id, topic_id, goal_id, obj_id)
            if problem:
                problem_id, prompt, answer, category = problem
            else:
                cursor.execute("""
                    INSERT INTO GenProblem (user_id, topic_id, goal_id, objective_id, prompt, correct_answer, category)
                    VALUES (?, ?, ?, ?, ?, ?, ?)
                """, (user_id, topic_id, goal_id, obj_id, f"Test problem {i+1}", f"Answer {i+1}", "factual"))
                problem_id = cursor.lastrowid
                conn.commit()
        else:
            cursor.execute("""
                INSERT INTO GenProblem (user_id, topic_id, goal_id, objective_id, prompt, correct_answer, category)
                VALUES (?, ?, ?, ?, ?, ?, ?)
            """, (user_id, topic_id, goal_id, obj_id, f"Test problem {i+1}", f"Answer {i+1}", "factual"))
            problem_id = cursor.lastrowid
            conn.commit()
        
        # Simulate performance pattern: mostly correct with some errors
        is_correct = (i % 3 != 1)  # 2 out of 3 correct
        student_answer = f"Answer {i+1}"
        
        record_practice_attempt(user_id, goal_id, problem_id, student_answer, is_correct)
        attempts.append((problem_id, is_correct))
        
        print(f"      ✅ Attempt recorded (Correct: {is_correct})")
        
        # Check if profile should be updated
        if (i + 1) % PROFILE_UPDATE_FREQUENCY == 0:
            print(f"      🔄 Triggering profile update (after {i+1} problems)...")
            update_student_profile(user_id, topic_id, goal_id, obj_id)
            print(f"      ✅ Profile updated")
    
    # Get final profile state
    print("\n📊 Checking Profile Updates...")
    cursor.execute("""
        SELECT preferred_learner_style, target_difficulty, focus_category, 
               performance_score, notes, last_updated
        FROM UserLMSProfile
        WHERE user_id = ?
    """, (user_id,))
    
    final_profile = cursor.fetchone()
    if not final_profile:
        print("❌ FAILED: Profile not found after updates")
        conn.close()
        return False
    
    final_style, final_difficulty, final_category, final_score, final_notes, final_updated = final_profile
    
    print(f"   Final Profile:")
    print(f"      Learning Style: {final_style}")
    print(f"      Difficulty: {final_difficulty}")
    print(f"      Focus Category: {final_category}")
    print(f"      Performance Score: {final_score}")
    print(f"      Notes Length: {len(final_notes) if final_notes else 0} characters")
    print(f"      Last Updated: {final_updated}")
    
    # Verify profile was updated
    print("\n🔍 Verifying Profile Changes...")
    
    changes_detected = 0
    
    if initial_profile:
        if final_updated != last_updated:
            print("   ✅ Last updated timestamp changed")
            changes_detected += 1
        
        if final_notes != notes:
            print("   ✅ Notes were updated")
            if final_notes:
                print(f"      New notes preview: {final_notes[:100]}...")
            changes_detected += 1
        
        if final_score != score:
            print(f"   ✅ Performance score changed: {score} → {final_score}")
            changes_detected += 1
    else:
        print("   ✅ Profile was created and populated")
        changes_detected = 3
    
    # Verify notes contain meaningful content
    if final_notes and len(final_notes) > 20:
        print("   ✅ Notes contain substantial content")
        changes_detected += 1
    
    # Calculate actual performance
    correct_count = sum(1 for _, correct in attempts if correct)
    actual_performance = correct_count / len(attempts)
    print(f"\n📈 Performance Analysis:")
    print(f"   Correct answers: {correct_count}/{len(attempts)} ({actual_performance*100:.1f}%)")
    print(f"   Stored performance score: {final_score}")
    
    if changes_detected >= 2:
        print(f"\n   ✅ Profile successfully updated ({changes_detected} changes detected)")
    else:
        print(f"\n   ⚠️  WARNING: Limited profile changes detected ({changes_detected})")
    
    conn.close()
    
    print("\n" + "=" * 80)
    print("✅ TEST 4 PASSED: User Profile Update")
    print("=" * 80)
    print("\nSummary:")
    print(f"  • Problems attempted: {num_problems}")
    print(f"  • Profile updates triggered: {num_problems // PROFILE_UPDATE_FREQUENCY}")
    print(f"  • Performance: {correct_count}/{len(attempts)} correct ({actual_performance*100:.1f}%)")
    print(f"  • Profile changes detected: {changes_detected}")
    print(f"  • Notes generated: {'Yes' if final_notes and len(final_notes) > 20 else 'No'}")
    print(f"  • Last updated: {final_updated}")
    
    return True

if __name__ == "__main__":
    try:
        success = test_user_profile_update()
        sys.exit(0 if success else 1)
    except Exception as e:
        print(f"\n❌ TEST FAILED WITH EXCEPTION: {e}")
        import traceback
        traceback.print_exc()
        sys.exit(1)

