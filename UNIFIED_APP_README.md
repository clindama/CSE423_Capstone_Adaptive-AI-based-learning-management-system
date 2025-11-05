# Unified Learning Management System

## Overview
This is the integrated version of the Adaptive AI-based Learning Management System that combines:
- **Progress Tracking** from the ProgressTracking branch
- **AI-Powered Problem Generation** from the main branch
- **Unified User Interface** with seamless navigation

## Main Entry Point
**Run this file to start the application:**
```bash
python unified_app.py
```

## Features

### 1. **User Authentication**
- Login with existing credentials
- Register new accounts
- Secure password handling
- Default admin account: username=`admin`, password=`1234`

### 2. **Topic & Goal Navigation**
- **Student Pick**: Manually select topics and browse learning goals
- **Computer Pick**: Randomly select a topic for practice
- Navigate through learning objectives for each goal

### 3. **Enhanced Progress Tracking** ✨ ⭐ NEW!
- **Visual Progress Bars**: See completion percentage for each topic with color-coded status
  - 🟢 Green (70-100%): Complete or almost there
  - 🟡 Yellow (40-69%): In progress
  - 🔴 Red (0-39%): Just started
- **Detailed Practice History**: Review every problem you've attempted
  - Organized by topic in tabbed interface
  - Individual cards for each attempt
  - Shows problem, your answer, correct answer
  - Timestamp and problem type
  - Goal and objective information
- **AI Feedback Button**: Click "🤖 Get AI Feedback" on any attempt to get personalized feedback
- **Real-time progress updates** based on problem-solving performance
- Track progress at multiple levels:
  - **Topic Progress**: Overall completion percentage per topic
  - **Goal Progress**: Grade and completion status per goal
  - **Automatic Updates**: Progress updates when you complete practice problems
- View completed topics and achievements

### 4. **AI-Powered Practice Problems** 🤖
- Generate custom problems using Google's Gemini AI
- Four knowledge types:
  - **Factual**: Basic facts and definitions
  - **Procedural**: Step-by-step problem solving
  - **Strategic**: Multi-step complex problems
  - **Rational**: Explanations and reasoning
- Immediate feedback on answers
- **Progress tracking integration**: Your performance automatically updates your goal and topic progress

### 5. **AI Tutor Feedback** 🤖 ⭐ NEW!
- Get personalized feedback on any practice attempt
- Click "🤖 Get AI Feedback" button on problem cards
- AI analyzes your answer vs. correct answer
- Provides:
  - Explanation of why answer is correct/incorrect
  - Tips and learning strategies
  - Encouraging and educational feedback
- Uses Google Gemini 1.5 Flash for fast responses

### 6. **Integrated Workflow**
```
Login → Dashboard → Select Topic → View Goals → Practice Problems → Progress Updates → Review History → Get AI Feedback
```

## How Progress Tracking Works

### Automatic Progress Updates
When you complete a practice problem:

1. **Problem Attempt Recorded**: Your answer is saved to the database
2. **Goal Progress Updated**: 
   - Grade calculated based on correct/total problems
   - Goal marked as completed if grade ≥ 70%
3. **Topic Progress Updated**:
   - Calculated as average of all goal grades in that topic
   - Updates automatically in real-time

### Progress Calculation
- **Goal Grade**: `(Correct Problems / Total Problems) × 100`
- **Topic Progress**: `Average of all Goal Grades in Topic`
- **Completion Threshold**: 70% or higher

### Viewing Progress
- Click **"📊 View Progress"** from the main dashboard
- See all topics with current progress percentages and visual progress bars
- View detailed practice history organized by topic
- Click on topic tabs to see all attempts for that topic
- Review individual problem cards with full details
- Click "🤖 Get AI Feedback" on any attempt to get personalized feedback
- Track your learning journey with comprehensive insights

## Database Schema

### Progress Tables
- **TopicProgress**: Tracks user progress per topic (0-100%)
- **GoalProgress**: Tracks user grade and completion per goal
- **PracticeProblemSet**: Groups practice problems by goal
- **PracticeProblem**: Individual problem attempts with answers
- **GenProblem**: AI-generated problems with correct answers

## Installation

### Prerequisites
```bash
pip install google-genai faker
```

### Database Setup

**IMPORTANT: Run these commands in order:**

1. **Create the base database:**
```bash
python main.py
```

2. **Add AI tables (required for practice problems):**
```bash
python add_ai_tables.py
```

This creates `learning_platform.db` with:
- User table with default admin account
- Topics and Goals from `toplist.sql`
- Schema from `test.sql`
- AI tables: GenProblem, PracticeProblemSet, PracticeProblem

## Usage Guide

### First Time Setup
1. Run `python main.py` to initialize the database
2. **Run `python add_ai_tables.py` to add AI tables** ⚠️ **REQUIRED!**
3. Run `python unified_app.py` to start the application
4. Login with admin credentials or register a new account

### Practicing with Progress Tracking
1. **Login** to your account
2. **Select a Topic** (Student Pick or Computer Pick)
3. **Browse Goals** and learning objectives
4. **Click "Practice Problems"** on any goal
5. **Select an Objective** to practice
6. **Choose Problem Type** (Factual, Procedural, Strategic, or Rational)
7. **Generate Problem** using AI
8. **Submit Your Answer**
9. **View Feedback** and see your progress update automatically!
10. **Check Progress Dashboard** to see your updated scores

### Viewing Your Progress
1. From the main dashboard, click **"📊 View Progress"**
2. See all topics with progress percentages
3. Click **"View Completed Topics"** to see achievements
4. Progress updates in real-time as you complete problems

## Key Improvements Over Previous Versions

### From ProgressTracking Branch
✅ Real database-backed progress tracking (not mock data)
✅ Topic and Goal progress tables
✅ Progress dashboard with visual tables
✅ Completion tracking

### From Main Branch
✅ AI-powered problem generation
✅ Multiple knowledge types
✅ GenProblem and PracticeProblem tables
✅ Answer evaluation

### New in Unified App
✨ **Integrated progress updates** - Progress automatically updates when solving AI problems
✨ **Single entry point** - One file to run everything
✨ **Seamless navigation** - Easy flow between all features
✨ **Real-time feedback** - See progress update immediately after each problem
✨ **Complete workflow** - From login to practice to progress tracking

## File Structure
```
unified_app.py          # Main application (RUN THIS!)
learning_platform.db    # SQLite database
login_subsystem.py      # Authentication service
test.sql               # Database schema
toplist.sql            # Topics and goals data
main.py                # Database initialization
```

## API Key Configuration
The app uses Google's Gemini AI. To use your own API key:
1. Get an API key from [Google AI Studio](https://makersuite.google.com/app/apikey)
2. Edit `unified_app.py` line 20:
   ```python
   API_KEY = "your-api-key-here"
   ```

## Troubleshooting

### "AI Not Available" Error
- Install google-genai: `pip install google-genai`
- Check your API key is valid

### Database Not Found
- Run `python main.py` to create the database
- Make sure `test.sql` and `toplist.sql` exist

### "No such table: GenProblem" Error
- **Solution**: Run `python add_ai_tables.py` to add the missing AI tables
- This is required for the practice problem feature to work

### Answer Input Not Showing
- Make sure the problem generated successfully (no errors in terminal)
- The answer input field appears automatically after clicking "Generate Problem"
- If you see an error, check that AI tables exist (run `add_ai_tables.py`)

### Progress Not Updating
- Make sure you're submitting answers through the practice problem interface
- Check that you're logged in with a valid user account
- Progress updates happen automatically after each problem submission

## Branch Information
- **Branch**: `integrated-app`
- **Merged from**: `main` + `ProgressTracking`
- **Created**: 2025-11-05

## Future Enhancements
- [ ] More sophisticated answer evaluation using AI
- [ ] Practice problem sets with multiple questions
- [ ] Pre/post tests for goals
- [ ] Detailed analytics and learning insights
- [ ] Parent/admin dashboards
- [ ] Export progress reports

## Credits
Developed as part of CSE423 Capstone Project
Adaptive AI-based Learning Management System

