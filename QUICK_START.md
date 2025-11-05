# Quick Start Guide - Unified Learning Management System

## 🚀 First Time Setup (Run these commands in order)

### Step 1: Install Dependencies
```bash
pip install google-genai faker
```

### Step 2: Initialize Database
```bash
python main.py
```
This creates the base database with users, topics, goals, and objectives.

### Step 3: Add AI Tables
```bash
python add_ai_tables.py
```
This adds the GenProblem, PracticeProblemSet, and PracticeProblem tables needed for AI features.

### Step 4: Test Everything (Optional but Recommended)
```bash
python test_unified_app.py
```
This verifies all tables are set up correctly and all database operations work.

### Step 5: Run the Application
```bash
python unified_app.py
```

## 🎯 Using the Application

### Login
- **Default Admin Account:**
  - Username: `admin`
  - Password: `1234`
- Or click "Register" to create a new account

### Main Dashboard
After login, you'll see 4 main options:

1. **📚 Student Pick Topic** - Browse and select topics manually
2. **🎲 Computer Pick Topic** - Get a random topic assigned
3. **📊 View Progress** - See your learning progress
4. **🤖 AI Practice Problems** - Practice with AI-generated problems

### Practicing with AI Problems

1. Click **"Student Pick Topic"** or **"AI Practice Problems"**
2. Select a topic (e.g., "Equations")
3. Select a goal (e.g., "Solve one-step equations")
4. Click **"Practice Problems"**
5. Select a learning objective
6. Choose problem type:
   - **Factual** - Basic facts and definitions
   - **Procedural** - Step-by-step problem solving
   - **Strategic** - Multi-step complex problems
   - **Rational** - Explanations and reasoning
7. Click **"Generate Problem"**
8. **Answer input will appear below the problem**
9. Type your answer and click **"Submit Answer"**
10. Get immediate feedback!
11. **Your progress updates automatically!**

### Viewing Progress

1. Click **"📊 View Progress"** from the main dashboard
2. See all topics with completion percentages
3. Click **"View Completed Topics"** to see achievements

## 🔧 Troubleshooting

### "No such table: GenProblem" Error
**Solution:** Run `python add_ai_tables.py`

### Answer Input Not Showing
**Causes:**
- Database error (check terminal for errors)
- Missing AI tables (run `add_ai_tables.py`)
- Problem generation failed (try again)

**What should happen:**
- After clicking "Generate Problem", you should see the problem text
- Below the problem, an input field should appear with label "Your Answer:"
- If you don't see it, check the terminal for error messages

### Database Locked Error
**Solution:** Close all instances of the application and try again

### AI Not Working
**Causes:**
- Missing `google-genai` package
- Invalid API key

**Solutions:**
- Install: `pip install google-genai`
- Check API key in `unified_app.py` line 20

## 📊 How Progress Tracking Works

### Automatic Updates
When you submit an answer to a practice problem:

1. ✅ Your answer is recorded in the database
2. 📈 Goal grade is calculated: `(Correct / Total) × 100`
3. 🎯 Goal is marked complete if grade ≥ 70%
4. 📚 Topic progress is updated (average of all goal grades)
5. 💾 Everything is saved automatically

### Progress Calculation
- **Goal Grade:** Percentage of correct answers for that goal
- **Topic Progress:** Average of all goal grades in that topic
- **Completion:** Goals with 70% or higher are marked complete

## 📁 File Structure

```
unified_app.py              ← Main application (RUN THIS!)
add_ai_tables.py           ← Database migration script
test_unified_app.py        ← Test script to verify setup
main.py                    ← Database initialization
learning_platform.db       ← SQLite database (created by main.py)
login_subsystem.py         ← Authentication service
test.sql                   ← Database schema
toplist.sql                ← Topics and goals data
```

## 🎓 Example Workflow

```
1. Run: python unified_app.py
2. Login with admin/1234
3. Click "Student Pick Topic"
4. Select "Equations"
5. Browse through goals
6. Click "Practice Problems" on any goal
7. Select an objective (e.g., "Solve x + a = b")
8. Choose "Procedural" problem type
9. Click "Generate Problem"
10. See problem: "Solve for x: x + 5 = 12"
11. Answer input appears below
12. Type: "7"
13. Click "Submit Answer"
14. Get feedback: "Correct! ✓"
15. Progress updates automatically!
16. Click "View Progress" to see updated scores
```

## ✅ Verification Checklist

Before using the app, make sure:

- [ ] Python 3.10+ installed
- [ ] Virtual environment activated (`.venv`)
- [ ] Dependencies installed (`google-genai`, `faker`)
- [ ] Database created (`python main.py`)
- [ ] AI tables added (`python add_ai_tables.py`)
- [ ] Tests pass (`python test_unified_app.py`)
- [ ] Application runs (`python unified_app.py`)

## 🆘 Getting Help

### Check Terminal Output
The terminal shows helpful error messages. Common ones:

```
ERROR: no such table: GenProblem
→ Run: python add_ai_tables.py

ERROR: Database not found
→ Run: python main.py

ERROR: AI Not Available
→ Run: pip install google-genai
```

### Test Database
Run the test script to diagnose issues:
```bash
python test_unified_app.py
```

This will tell you exactly what's missing or broken.

## 🎉 Success Indicators

You'll know everything is working when:

1. ✅ Application launches without errors
2. ✅ You can login successfully
3. ✅ Topics and goals are visible
4. ✅ "Generate Problem" creates a problem
5. ✅ **Answer input field appears below the problem**
6. ✅ Submitting answer shows feedback
7. ✅ Progress dashboard shows updated percentages

## 📝 Notes

- **Progress is saved permanently** in the database
- **Each problem attempt is recorded** for analytics
- **You can practice the same objective multiple times** to improve your grade
- **Topic progress updates in real-time** as you complete problems
- **All features work offline** except AI problem generation (requires internet)

## 🔐 Default Credentials

- **Username:** admin
- **Password:** 1234

**Security Note:** Change the admin password in a production environment!

---

**Branch:** `integrated-app`  
**Last Updated:** 2025-11-05  
**Status:** ✅ Fully Functional

