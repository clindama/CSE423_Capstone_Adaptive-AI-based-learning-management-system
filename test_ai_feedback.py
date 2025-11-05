"""
Test script to verify AI feedback generation works correctly
"""

from google import genai
from google.genai import types

# Configuration
API_KEY = "AIzaSyAuKWT3v9pI3YZKlxWBZoxEt1pyAm6zNik"

# Initialize client
client = genai.Client(api_key=API_KEY)

def test_ai_feedback():
    """Test AI feedback generation"""
    print("=" * 70)
    print("TESTING AI FEEDBACK GENERATION")
    print("=" * 70)
    
    problem_text = "Solve for x: 2x = 10"
    student_answer = "6"
    correct_answer = "5"
    is_correct = False
    
    prompt = f"""You are a helpful math tutor. A student attempted this problem:

Problem: {problem_text}

Student's Answer: {student_answer}
Correct Answer: {correct_answer}
Result: {"Correct" if is_correct else "Incorrect"}

Provide constructive feedback:
1. If correct: Praise the student and explain why the answer is right
2. If incorrect: Gently explain the mistake and guide them to the correct solution
3. Provide tips or insights to help them understand the concept better

Keep the feedback encouraging, clear, and educational. Use simple language."""

    print("\n📝 Test Problem:")
    print(f"   Problem: {problem_text}")
    print(f"   Student Answer: {student_answer}")
    print(f"   Correct Answer: {correct_answer}")
    print(f"   Result: {'Correct' if is_correct else 'Incorrect'}")
    
    print("\n🤖 Generating AI Feedback...")
    
    try:
        response = client.models.generate_content(
            model='gemini-2.0-flash-exp',
            contents=prompt
        )
        
        print("\n✅ AI Feedback Generated Successfully!")
        print("\n" + "=" * 70)
        print("FEEDBACK:")
        print("=" * 70)
        print(response.text)
        print("=" * 70)
        
        return True
        
    except Exception as e:
        print(f"\n❌ ERROR: {str(e)}")
        print("\nTrying alternative model: gemini-1.5-flash...")
        
        try:
            response = client.models.generate_content(
                model='gemini-1.5-flash',
                contents=prompt
            )
            
            print("\n✅ AI Feedback Generated Successfully with gemini-1.5-flash!")
            print("\n" + "=" * 70)
            print("FEEDBACK:")
            print("=" * 70)
            print(response.text)
            print("=" * 70)
            
            return True
            
        except Exception as e2:
            print(f"\n❌ ERROR with gemini-1.5-flash: {str(e2)}")
            return False

def list_available_models():
    """List all available models"""
    print("\n" + "=" * 70)
    print("LISTING AVAILABLE MODELS")
    print("=" * 70)

    try:
        models = client.models.list()
        print("\n✅ Available Models:")
        for model in models:
            print(f"   - {model.name}")
        return True
    except Exception as e:
        print(f"\n❌ ERROR listing models: {str(e)}")
        return False

if __name__ == "__main__":
    # First, try to list available models
    print("\n🔍 Checking available models...")
    list_available_models()

    # Then test AI feedback
    success = test_ai_feedback()

    if success:
        print("\n✅ AI Feedback test PASSED!")
        print("\nThe AI feedback feature is working correctly.")
    else:
        print("\n❌ AI Feedback test FAILED!")
        print("\nPlease check your API key and internet connection.")
        print("\n💡 Tip: The API might be rate-limited. Wait a few minutes and try again.")

