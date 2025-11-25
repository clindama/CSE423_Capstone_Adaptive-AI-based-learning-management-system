# Learning Management System - Project Structure

## Overview
This is an Adaptive AI-based Learning Management System built with Python and Tkinter. The system uses Google's Gemini AI to provide personalized learning experiences.

## Project Structure

```
CSE423_Capstone_Adaptive-AI-based-learning-management-system/
│
├── unified_app.py          # Main application entry point
├── config.py               # Configuration, constants, colors, fonts
├── ai_tutor.py            # AI tutoring functionality (problem generation, profiling)
├── database.py            # Database operations and queries
├── progress_tracker.py    # Progress tracking and reporting
├── ui_components.py       # Reusable UI components and widgets
├── login_subsystem.py     # User authentication (existing)
│
├── learning_platform.db   # SQLite database
├── add_ai_tables.py       # Database migration script
├── main.py                # Database initialization script
│
├── AI_Tutor/              # Advanced AI demo and reference
│   ├── advanceAIDemo.py
│   ├── tables.sql
│   └── ...
│
└── README.md              # Project documentation
```

## Module Descriptions

### 1. `config.py`
**Purpose:** Central configuration file for the entire application

**Contains:**
- Database path configuration
- AI API key and client initialization
- Color palette (COLORS dictionary)
- Font definitions (FONTS dictionary)
- Learning categories and descriptions
- Session configuration (mastery thresholds, etc.)

**Key Variables:**
- `DB_PATH`: Path to SQLite database
- `AI_AVAILABLE`: Boolean flag for AI features
- `client`: Google Gemini AI client instance
- `COLORS`: Modern color scheme for UI
- `FONTS`: Typography settings

---

### 2. `ai_tutor.py`
**Purpose:** All AI-powered tutoring functionality

**Key Functions:**
- `load_user_profile(user_id)`: Load or create student profile
- `load_context(user_id)`: Generate comprehensive context for AI
- `get_full_performance(user_id)`: Calculate performance by category
- `Profile_Alg(user_id)`: AI-driven profile updating algorithm
- `generate_problem(obj_title, obj_desc, profile)`: Generate personalized problems

**Features:**
- Student profiling with adaptive learning
- Context-aware AI prompts
- Category balancing (factual, procedural, strategic, rational)
- Performance-based difficulty adjustment
- Automatic profile updates every 5 problems

---

### 3. `database.py`
**Purpose:** All database operations and queries

**Key Functions:**

**User Operations:**
- `get_user_by_id(user_id)`: Fetch user information

**Topic Operations:**
- `fetch_all_topics()`: Get all learning topics
- `fetch_goals_for_topic(topic_name)`: Get goals for a topic
- `fetch_objectives_for_goal(goal_id)`: Get objectives for a goal
- `get_topic_id_by_name(topic_name)`: Convert topic name to ID
- `get_goal_info(goal_id)`: Get goal details
- `get_objective_details(objective_id)`: Get objective details

**Problem Operations:**
- `save_generated_problem(...)`: Save AI-generated problem
- `record_practice_attempt(...)`: Record student attempt
- `get_practice_history(user_id, limit)`: Get recent practice history

---

### 4. `progress_tracker.py`
**Purpose:** Progress tracking and reporting

**Key Functions:**
- `update_topic_progress(user_id, topic_id, progress_increment)`: Update topic progress
- `update_goal_progress(user_id, goal_id, correct_count, total_count)`: Update goal progress
- `get_user_progress_summary(user_id)`: Get comprehensive progress summary
- `get_practice_statistics(user_id)`: Get practice problem statistics

**Features:**
- Topic-level progress tracking
- Goal-level progress tracking (with 90% mastery requirement)
- Overall statistics and analytics
- Category-based performance metrics

---

### 5. `ui_components.py`
**Purpose:** Reusable UI components and widgets

**Key Functions:**
- `create_modern_button(...)`: Create styled button with hover effects
- `create_dashboard_card(...)`: Create dashboard card widget
- `create_scrollable_frame(parent, bg_color)`: Create scrollable frame with canvas
- `setup_mousewheel_scrolling(window, canvas)`: Setup mousewheel scrolling
- `center_window(window, width, height)`: Center window on screen
- `get_responsive_window_size(...)`: Calculate responsive window dimensions

**Features:**
- Modern, consistent UI styling
- Hover effects and animations
- Responsive design helpers
- Scrollable containers

---

### 6. `unified_app.py`
**Purpose:** Main application entry point and UI orchestration

**Contains:**
- Main dashboard
- Login screen integration
- Topic/Goal/Objective selection screens
- Practice problem sessions
- Progress dashboard
- AI feedback dialogs

**Key Functions:**
- `show_login_screen()`: Display login interface
- `show_main_dashboard()`: Display main menu
- `show_student_pick(window)`: Topic selection interface
- `show_goals_for_topic(...)`: Goal selection interface
- `show_practice_for_goal(...)`: Practice session interface
- `show_progress_dashboard(window)`: Progress tracking interface

---

## Database Schema

### Core Tables
- **User**: User accounts and authentication
- **Topic**: Learning topics (e.g., "Foundations for Algebra")
- **Goal**: Learning goals within topics
- **LearningObjective**: Specific objectives within goals

### Progress Tables
- **TopicProgress**: User progress per topic (0-100%)
- **GoalProgress**: User progress per goal (grade, completion status)

### AI Tables
- **GenProblem**: AI-generated practice problems
- **PracticeProblemSet**: Sets of practice problems
- **PracticeProblem**: Individual problem attempts
- **UserLMSProfile**: Student learning profiles for adaptive AI

---

## How to Run

### 1. Setup Database
```bash
python main.py              # Initialize database
python add_ai_tables.py     # Add AI tables
```

### 2. Install Dependencies
```bash
pip install google-genai
```

### 3. Run Application
```bash
python unified_app.py
```

---

## Key Features

1. **Adaptive AI Tutoring**: Problems adapt to student performance
2. **Student Profiling**: Tracks learning style, difficulty preference, performance
3. **Category Balancing**: Ensures balanced exposure to all knowledge types
4. **Progress Tracking**: Comprehensive progress monitoring
5. **Modern UI**: Clean, responsive interface with scrolling support
6. **Mastery-Based Learning**: 90% accuracy + 20 problems minimum

---

## For Developers

### Adding New Features
1. **New AI functionality** → Add to `ai_tutor.py`
2. **New database queries** → Add to `database.py`
3. **New UI components** → Add to `ui_components.py`
4. **New progress metrics** → Add to `progress_tracker.py`
5. **New screens/flows** → Add to `unified_app.py`

### Configuration Changes
- Update `config.py` for colors, fonts, constants
- Never hardcode values in other modules

### Database Changes
- Update `add_ai_tables.py` for schema changes
- Add migration functions as needed

---

## Contact
CSE423 Capstone Project - Adaptive AI-based Learning Management System

