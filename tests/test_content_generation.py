"""
Test 1: Content Generation
Purpose: Verify AI Tutor generates unique instructional content based on user profiles
Approach: Test with two different student profiles and verify content uniqueness
"""

import sqlite3
import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from ai_tutor import generate_instructional_content, get_or_create_user_profile
from config import DB_PATH, AI_AVAILABLE
import json

def test_content_generation():
    """Test content generation for two different user profiles"""
    
    print("=" * 80)
    print("TEST 1: CONTENT GENERATION")
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
    
    # Create two different user profiles
    print("\n👤 Creating User Profile 1 (Visual Learner, Beginner)...")
    cursor.execute("SELECT id FROM User LIMIT 1")
    user1_id = cursor.fetchone()[0]
    
    profile1 = get_or_create_user_profile(user1_id)
    cursor.execute("""
        UPDATE UserLMSProfile 
        SET preferred_learner_style = 'visual',
            target_difficulty = 1,
            preferred_numeric_complexity = 'simple',
            focus_category = 'factual'
        WHERE user_id = ?
    """, (user1_id,))
    conn.commit()
    
    print("   ✅ Profile 1 configured: Visual, Difficulty=1, Simple, Factual")
    
    # Generate content for user 1
    print("\n🤖 Generating content for User 1...")
    content1 = generate_instructional_content(user1_id, topic_id, goal_id, obj_id)
    
    if not content1:
        print("❌ FAILED: No content generated for User 1")
        conn.close()
        return False
    
    print(f"   ✅ Generated {len(content1)} characters of content")
    print(f"   Preview: {content1[:150]}...")
    
    # Create second user profile (different characteristics)
    print("\n👤 Creating User Profile 2 (Analytical Learner, Advanced)...")
    cursor.execute("SELECT id FROM User WHERE id != ? LIMIT 1", (user1_id,))
    user2_result = cursor.fetchone()
    
    if not user2_result:
        # Create a test user if needed
        cursor.execute("INSERT INTO User (username, password) VALUES (?, ?)", 
                      ("test_user_2", "password"))
        user2_id = cursor.lastrowid
    else:
        user2_id = user2_result[0]
    
    profile2 = get_or_create_user_profile(user2_id)
    cursor.execute("""
        UPDATE UserLMSProfile 
        SET preferred_learner_style = 'analytical',
            target_difficulty = 5,
            preferred_numeric_complexity = 'complex',
            focus_category = 'strategic'
        WHERE user_id = ?
    """, (user2_id,))
    conn.commit()
    
    print("   ✅ Profile 2 configured: Analytical, Difficulty=5, Complex, Strategic")
    
    # Generate content for user 2
    print("\n🤖 Generating content for User 2...")
    content2 = generate_instructional_content(user2_id, topic_id, goal_id, obj_id)
    
    if not content2:
        print("❌ FAILED: No content generated for User 2")
        conn.close()
        return False
    
    print(f"   ✅ Generated {len(content2)} characters of content")
    print(f"   Preview: {content2[:150]}...")
    
    # Verify content is different
    print("\n🔍 Verifying Content Uniqueness...")
    
    if content1 == content2:
        print("❌ FAILED: Content is identical for both users")
        conn.close()
        return False
    
    # Calculate similarity (simple word overlap check)
    words1 = set(content1.lower().split())
    words2 = set(content2.lower().split())
    overlap = len(words1.intersection(words2)) / max(len(words1), len(words2))
    
    print(f"   Word overlap: {overlap*100:.1f}%")
    
    if overlap > 0.9:
        print("⚠️  WARNING: Content is very similar (>90% overlap)")
    else:
        print("   ✅ Content is sufficiently unique")
    
    # Verify content is relevant to the objective
    print("\n🔍 Verifying Content Relevance...")
    objective_keywords = obj_title.lower().split()
    content1_lower = content1.lower()
    
    relevant_keywords_found = sum(1 for keyword in objective_keywords if keyword in content1_lower)
    
    if relevant_keywords_found > 0:
        print(f"   ✅ Found {relevant_keywords_found} objective keywords in content")
    else:
        print("   ⚠️  No objective keywords found in content")
    
    conn.close()
    
    print("\n" + "=" * 80)
    print("✅ TEST 1 PASSED: Content Generation")
    print("=" * 80)
    print("\nSummary:")
    print(f"  • Generated unique content for 2 different user profiles")
    print(f"  • User 1 (Visual/Beginner): {len(content1)} chars")
    print(f"  • User 2 (Analytical/Advanced): {len(content2)} chars")
    print(f"  • Content uniqueness: {(1-overlap)*100:.1f}%")
    print(f"  • Relevance: {relevant_keywords_found} keywords matched")
    
    return True

if __name__ == "__main__":
    try:
        success = test_content_generation()
        sys.exit(0 if success else 1)
    except Exception as e:
        print(f"\n❌ TEST FAILED WITH EXCEPTION: {e}")
        import traceback
        traceback.print_exc()
        sys.exit(1)

