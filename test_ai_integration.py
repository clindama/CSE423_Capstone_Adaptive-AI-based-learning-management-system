"""
Test script to verify AI integration is working correctly
Tests API key configuration and AI functionality
"""

import sys
import os

# Configuration
API_KEY = "AIzaSyDlIbDoYs5yqCTpyf-FPXuwRIWvecl5Lc0"
DB_PATH = "learning_platform.db"

def test_imports():
    """Test that all required packages are installed"""
    print("=" * 70)
    print("TEST 1: Checking Required Packages")
    print("=" * 70)
    
    try:
        import google.genai as genai
        print("✅ google-genai package installed")
        return True
    except ImportError:
        print("❌ google-genai package NOT installed")
        print("   Run: pip install google-genai")
        return False

def test_api_key():
    """Test that API key is valid and working"""
    print("\n" + "=" * 70)
    print("TEST 2: Verifying API Key")
    print("=" * 70)
    
    try:
        import google.genai as genai
        
        print(f"API Key: {API_KEY[:20]}...{API_KEY[-10:]}")
        
        # Initialize client
        client = genai.Client(api_key=API_KEY)
        print("✅ API client initialized successfully")
        
        # Test a simple generation
        print("\n🤖 Testing AI generation...")
        response = client.models.generate_content(
            model='gemini-2.5-flash',
            contents="Say 'Hello, I am working!' in exactly those words."
        )
        
        print(f"✅ AI Response: {response.text[:100]}")
        return True
        
    except Exception as e:
        print(f"❌ API Key Error: {str(e)}")
        return False

def test_database():
    """Test that database exists and has required tables"""
    print("\n" + "=" * 70)
    print("TEST 3: Checking Database")
    print("=" * 70)
    
    if not os.path.exists(DB_PATH):
        print(f"❌ Database not found: {DB_PATH}")
        print("   Run: python main.py")
        return False
    
    print(f"✅ Database found: {DB_PATH}")
    
    import sqlite3
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()
    
    required_tables = [
        'User', 'Topic', 'Goal', 'LearningObjective',
        'TopicProgress', 'GoalProgress',
        'GenProblem', 'PracticeProblemSet', 'PracticeProblem'
    ]
    
    cursor.execute("SELECT name FROM sqlite_master WHERE type='table'")
    existing_tables = [row[0] for row in cursor.fetchall()]
    
    all_exist = True
    for table in required_tables:
        if table in existing_tables:
            print(f"  ✅ {table}")
        else:
            print(f"  ❌ {table} - MISSING")
            all_exist = False
    
    conn.close()
    
    if not all_exist:
        print("\n⚠️  Missing tables. Run: python add_ai_tables.py")
        return False
    
    return True

def test_unified_app_config():
    """Test that unified_app.py has correct API key"""
    print("\n" + "=" * 70)
    print("TEST 4: Checking unified_app.py Configuration")
    print("=" * 70)
    
    if not os.path.exists("unified_app.py"):
        print("❌ unified_app.py not found")
        return False
    
    with open("unified_app.py", "r", encoding="utf-8") as f:
        content = f.read()
    
    if API_KEY in content:
        print(f"✅ API key correctly configured in unified_app.py")
        return True
    else:
        print(f"❌ API key NOT found in unified_app.py")
        return False

def main():
    """Run all tests"""
    print("\n" + "=" * 70)
    print("AI INTEGRATION TEST SUITE")
    print("=" * 70)
    
    results = []
    
    # Run tests
    results.append(("Package Installation", test_imports()))
    results.append(("API Key Validation", test_api_key()))
    results.append(("Database Setup", test_database()))
    results.append(("App Configuration", test_unified_app_config()))
    
    # Summary
    print("\n" + "=" * 70)
    print("TEST SUMMARY")
    print("=" * 70)
    
    passed = sum(1 for _, result in results if result)
    total = len(results)
    
    for test_name, result in results:
        status = "✅ PASS" if result else "❌ FAIL"
        print(f"{status} - {test_name}")
    
    print("\n" + "=" * 70)
    print(f"Results: {passed}/{total} tests passed")
    print("=" * 70)
    
    if passed == total:
        print("\n🎉 ALL TESTS PASSED! Your AI integration is ready to use!")
        print("\nRun the app with: python unified_app.py")
    else:
        print("\n⚠️  Some tests failed. Please fix the issues above.")
    
    return passed == total

if __name__ == "__main__":
    success = main()
    sys.exit(0 if success else 1)

