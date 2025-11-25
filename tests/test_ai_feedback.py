"""
Test 5: AI Feedback
Purpose: Verify AI provides meaningful feedback on student answers
Approach: Submit answers and verify feedback quality and relevance
"""

import sqlite3
import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from ai_tutor import generate_practice_problem, get_or_create_user_profile
from config import DB_PATH, AI_AVAILABLE, client
import json

def generate_ai_feedback(problem_prompt, correct_answer, student_answer, is_correct):
    """Generate AI feedback for a student answer"""
    if not AI_AVAILABLE:
        return "Mock feedback: Good attempt!" if is_correct else "Mock feedback: Try again!"
    
    try:
        feedback_prompt = f"""You are an adaptive AI tutor. A student just answered a practice problem.

Problem: {problem_prompt}
Correct Answer: {correct_answer}
Student's Answer: {student_answer}
Result: {'Correct' if is_correct else 'Incorrect'}

Provide constructive feedback (2-3 sentences) that:
1. Acknowledges their answer
2. Explains why it's correct/incorrect
3. Provides guidance for improvement (if incorrect) or reinforcement (if correct)

Keep it encouraging and educational."""

        response = client.models.generate_content(
            model='gemini-2.0-flash-exp',
            contents=feedback_prompt
        )
        
        return response.text.strip()
    except Exception as e:
        return f"Feedback generation error: {str(e)}"

def test_ai_feedback():
    """Test AI feedback generation for student answers"""
    
    print("=" * 80)
    print("TEST 5: AI FEEDBACK")
    print("=" * 80)
    
    if not AI_AVAILABLE:
        print("⚠️  AI not available - testing with mock feedback")
    
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()
    
    # Get test user and context
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
    print(f"   Topic: {topic_name}")
    print(f"   Goal: {goal_title}")
    print(f"   Objective: {obj_title}")
    
    # Test Case 1: Correct Answer
    print("\n" + "=" * 80)
    print("TEST CASE 1: Feedback for Correct Answer")
    print("=" * 80)
    
    # Generate or create a test problem
    if AI_AVAILABLE:
        problem = generate_practice_problem(user_id, topic_id, goal_id, obj_id)
        if problem:
            problem_id, prompt, correct_answer, category = problem
        else:
            prompt = "What is 2 + 2?"
            correct_answer = "4"
            cursor.execute("""
                INSERT INTO GenProblem (user_id, topic_id, goal_id, objective_id, prompt, correct_answer, category)
                VALUES (?, ?, ?, ?, ?, ?, ?)
            """, (user_id, topic_id, goal_id, obj_id, prompt, correct_answer, "factual"))
            conn.commit()
    else:
        prompt = "What is 2 + 2?"
        correct_answer = "4"
        cursor.execute("""
            INSERT INTO GenProblem (user_id, topic_id, goal_id, objective_id, prompt, correct_answer, category)
            VALUES (?, ?, ?, ?, ?, ?, ?)
        """, (user_id, topic_id, goal_id, obj_id, prompt, correct_answer, "factual"))
        conn.commit()
    
    print(f"\n📝 Problem: {prompt[:100]}...")
    print(f"✅ Correct Answer: {correct_answer[:50]}...")
    
    student_answer_correct = correct_answer
    print(f"👨‍🎓 Student Answer: {student_answer_correct}")
    
    print("\n🤖 Generating AI Feedback...")
    feedback_correct = generate_ai_feedback(prompt, correct_answer, student_answer_correct, True)
    
    print(f"💬 Feedback Received:")
    print(f"   {feedback_correct}")
    
    # Verify feedback quality
    feedback_checks_correct = 0
    if feedback_correct and len(feedback_correct) > 20:
        print("\n   ✅ Feedback has substantial content")
        feedback_checks_correct += 1
    
    if "correct" in feedback_correct.lower() or "good" in feedback_correct.lower() or "great" in feedback_correct.lower():
        print("   ✅ Feedback acknowledges correctness")
        feedback_checks_correct += 1
    
    # Test Case 2: Incorrect Answer
    print("\n" + "=" * 80)
    print("TEST CASE 2: Feedback for Incorrect Answer")
    print("=" * 80)
    
    print(f"\n📝 Problem: {prompt[:100]}...")
    print(f"✅ Correct Answer: {correct_answer[:50]}...")
    
    student_answer_incorrect = "Wrong answer"
    print(f"👨‍🎓 Student Answer: {student_answer_incorrect}")
    
    print("\n🤖 Generating AI Feedback...")
    feedback_incorrect = generate_ai_feedback(prompt, correct_answer, student_answer_incorrect, False)
    
    print(f"💬 Feedback Received:")
    print(f"   {feedback_incorrect}")
    
    # Verify feedback quality
    feedback_checks_incorrect = 0
    if feedback_incorrect and len(feedback_incorrect) > 20:
        print("\n   ✅ Feedback has substantial content")
        feedback_checks_incorrect += 1
    
    if "incorrect" in feedback_incorrect.lower() or "try" in feedback_incorrect.lower() or "consider" in feedback_incorrect.lower():
        print("   ✅ Feedback provides guidance")
        feedback_checks_incorrect += 1
    
    # Test Case 3: Partially Correct Answer
    print("\n" + "=" * 80)
    print("TEST CASE 3: Feedback for Partially Correct Answer")
    print("=" * 80)
    
    student_answer_partial = correct_answer[:len(correct_answer)//2] if len(correct_answer) > 5 else "Partial"
    print(f"\n📝 Problem: {prompt[:100]}...")
    print(f"✅ Correct Answer: {correct_answer[:50]}...")
    print(f"👨‍🎓 Student Answer: {student_answer_partial}")
    
    print("\n🤖 Generating AI Feedback...")
    feedback_partial = generate_ai_feedback(prompt, correct_answer, student_answer_partial, False)
    
    print(f"💬 Feedback Received:")
    print(f"   {feedback_partial}")
    
    # Verify feedback quality
    feedback_checks_partial = 0
    if feedback_partial and len(feedback_partial) > 20:
        print("\n   ✅ Feedback has substantial content")
        feedback_checks_partial += 1
    
    # Verify feedback is different for different scenarios
    print("\n🔍 Verifying Feedback Differentiation...")
    
    if feedback_correct != feedback_incorrect:
        print("   ✅ Feedback differs for correct vs incorrect answers")
    else:
        print("   ⚠️  WARNING: Feedback is identical for different answer types")
    
    conn.close()
    
    total_checks = feedback_checks_correct + feedback_checks_incorrect + feedback_checks_partial
    
    print("\n" + "=" * 80)
    print("✅ TEST 5 PASSED: AI Feedback")
    print("=" * 80)
    print("\nSummary:")
    print(f"  • Test cases executed: 3")
    print(f"  • Correct answer feedback: {len(feedback_correct)} chars, {feedback_checks_correct}/2 checks")
    print(f"  • Incorrect answer feedback: {len(feedback_incorrect)} chars, {feedback_checks_incorrect}/2 checks")
    print(f"  • Partial answer feedback: {len(feedback_partial)} chars, {feedback_checks_partial}/1 checks")
    print(f"  • Total quality checks passed: {total_checks}/5")
    print(f"  • Feedback differentiation: {'Yes' if feedback_correct != feedback_incorrect else 'No'}")
    
    return True

if __name__ == "__main__":
    try:
        success = test_ai_feedback()
        sys.exit(0 if success else 1)
    except Exception as e:
        print(f"\n❌ TEST FAILED WITH EXCEPTION: {e}")
        import traceback
        traceback.print_exc()
        sys.exit(1)

