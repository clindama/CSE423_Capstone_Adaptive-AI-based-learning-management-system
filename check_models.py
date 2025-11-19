"""
Quick script to check available Gemini models
"""

import google.genai as genai
import time

API_KEY = "AIzaSyDlIbDoYs5yqCTpyf-FPXuwRIWvecl5Lc0"

client = genai.Client(api_key=API_KEY)

print("Listing available models:")
print("=" * 70)

try:
    # Try to list models
    print("\nAttempting to list models...")
    models = client.models.list()
    for model in models:
        print(f"  - {model.name}")
except Exception as e:
    print(f"Could not list models: {e}")

print("\n" + "=" * 70)
print("Testing models with generation:")
print("=" * 70)

# Wait a bit to avoid rate limit
print("\nWaiting 35 seconds to avoid rate limit...")
time.sleep(35)

try:
    # Try different model names
    models_to_try = [
        'gemini-2.0-flash-exp',
        'gemini-1.5-flash-latest',
        'gemini-1.5-pro-latest',
    ]

    for model_name in models_to_try:
        try:
            print(f"\nTrying: {model_name}")
            response = client.models.generate_content(
                model=model_name,
                contents="Say hello"
            )
            print(f"✅ {model_name} - WORKS!")
            print(f"   Response: {response.text[:50]}")
            break  # Stop after first working model
        except Exception as e:
            error_str = str(e)
            if "429" in error_str:
                print(f"⏳ {model_name} - Rate limited")
            elif "404" in error_str:
                print(f"❌ {model_name} - Not found")
            else:
                print(f"❌ {model_name} - {error_str[:100]}")

except Exception as e:
    print(f"Error: {e}")

