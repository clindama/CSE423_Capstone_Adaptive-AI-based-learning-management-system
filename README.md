# Adaptive AI-based Learning Management System

## 📚 Overview

An intelligent Learning Management System (LMS) that uses Google's Gemini AI to provide personalized, adaptive learning experiences for students. The system tracks student performance, adapts problem difficulty, and provides real-time feedback to optimize learning outcomes.

### Key Features

- 🤖 **AI-Powered Tutoring**: Personalized problem generation using Google Gemini AI
- 📊 **Adaptive Learning**: Automatically adjusts difficulty based on student performance
- 📈 **Progress Tracking**: Comprehensive tracking of topics, goals, and learning objectives
- 🎯 **Student Profiling**: Maintains detailed profiles including learning style, difficulty preferences, and performance metrics
- 💬 **Real-time Feedback**: AI-generated explanations and hints for incorrect answers
- 🎨 **Modern UI**: Clean, responsive interface with scrollable content areas

---

## 🚀 Quick Start

### Prerequisites

- Python 3.8 or higher
- pip (Python package manager)
- Google Gemini API key

### Installation

1. **Clone the repository**
   ```bash
   git clone <repository-url>
   cd CSE423_Capstone_Adaptive-AI-based-learning-management-system
   ```

2. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

   Or install manually:
   ```bash
   pip install google-genai
   ```

3. **Set up the database**
   ```bash
   # Initialize the main database and tables
   python main.py

   # Add AI-specific tables (UserLMSProfile, GenProblem, etc.)
   python add_ai_tables.py
   ```

4. **Configure API Key**

   Edit `config.py` and add your Google Gemini API key:
   ```python
   API_KEY = "your-api-key-here"
   ```

5. **Run the application**
   ```bash
   python unified_app.py
   ```

---

## 📁 Project Structure

```
CSE423_Capstone_Adaptive-AI-based-learning-management-system/
│
├── 📄 unified_app.py          # Main application entry point
├── 📄 config.py               # Configuration, constants, colors, fonts
├── 📄 ai_tutor.py            # AI tutoring functionality
├── 📄 database.py            # Database operations
├── 📄 progress_tracker.py    # Progress tracking and analytics
├── 📄 ui_components.py       # Reusable UI components
├── 📄 login_subsystem.py     # User authentication
│
├── 📄 main.py                # Database initialization script
├── 📄 add_ai_tables.py       # AI tables migration script
├── 📄 add_test_user.py       # Test user creation script
│
├── 📄 learning_platform.db   # SQLite database (created after setup)
├── 📄 requirements.txt       # Python dependencies
│
├── 📁 AI_Tutor/              # Reference implementation and SQL schemas
│   ├── advanceAIDemo.py      # Advanced AI demo
│   ├── tables.sql            # Database schema definitions
│   └── seed_*.sql            # Database seed data
│
└── 📁 Documentation/
    ├── PROJECT_STRUCTURE.md   # Detailed module documentation
    ├── ARCHITECTURE.md        # System architecture and data flow
    ├── DEVELOPER_GUIDE.md     # Developer quick start guide
    └── REFACTORING_SUMMARY.md # Code refactoring details
```

---

## 📖 File Descriptions

### Core Application Files

#### `unified_app.py` (Main Application)
**Purpose**: Main entry point and UI orchestration

**Contains**:
- Login screen integration
- Main dashboard with learning path cards
- Topic/Goal/Objective selection screens
- Practice problem session interface
- Progress dashboard
- AI feedback dialogs

**Key Functions**:
- `show_login_screen()` - Display login interface
- `show_main_dashboard()` - Display main menu
- `show_student_pick()` - Topic selection
- `show_goals_for_topic()` - Goal selection
- `show_practice_for_goal()` - Practice session
- `show_progress_dashboard()` - Progress tracking

**Run**: `python unified_app.py`

---

#### `config.py` (Configuration)
**Purpose**: Central configuration file for the entire application

**Contains**:
- Database path configuration (`DB_PATH`)
- Google Gemini API key and client initialization
- Color palette (`COLORS` dictionary)
- Font definitions (`FONTS` dictionary)
- Learning categories (factual, procedural, strategic, rational)
- Session configuration constants

**Key Variables**:
```python
DB_PATH = "learning_platform.db"
API_KEY = "your-api-key"
COLORS = {...}  # UI color scheme
FONTS = {...}   # Typography settings
LEARNING_CATEGORIES = ["factual", "procedural", "strategic", "rational"]
PROFILE_UPDATE_FREQUENCY = 5  # Update profile every N problems
```

**Why it exists**: Single source of truth for all configuration. Change colors, fonts, or settings here instead of throughout the codebase.

---

#### `ai_tutor.py` (AI Tutoring)
**Purpose**: All AI-powered tutoring functionality

**Contains**:
- Student profile management
- AI context generation
- Problem generation with adaptive difficulty
- Automatic profile updating based on performance
- Performance analytics by category

**Key Functions**:
- `load_user_profile(user_id)` - Load or create student profile
- `load_context(user_id)` - Generate comprehensive AI context
- `generate_problem(obj_title, obj_desc, profile)` - Generate personalized problems
- `Profile_Alg(user_id)` - AI-driven profile updating algorithm
- `get_full_performance(user_id)` - Calculate performance by category

**AI Models Used**:
- `gemini-2.5-flash-lite` for problem generation and profile updates
- Temperature: 0.7 for profile updates, 0.8 for problem generation

**Features**:
- Adaptive difficulty based on student performance
- Category balancing (ensures exposure to all knowledge types)
- Learning style adaptation
- Automatic profile updates every 5 problems

---

#### `database.py` (Database Operations)
**Purpose**: All database queries and operations

**Contains**:
- User operations
- Topic/Goal/Objective queries
- Problem saving and retrieval
- Practice attempt recording
- Practice history queries

**Key Functions**:

**User Operations**:
- `get_user_by_id(user_id)` - Fetch user information

**Topic Operations**:
- `fetch_all_topics()` - Get all learning topics
- `fetch_goals_for_topic(topic_name)` - Get goals for a topic
- `fetch_objectives_for_goal(goal_id)` - Get objectives for a goal
- `get_topic_id_by_name(topic_name)` - Convert topic name to ID

**Problem Operations**:
- `save_generated_problem(...)` - Save AI-generated problem
- `record_practice_attempt(...)` - Record student attempt
- `get_practice_history(user_id, limit)` - Get recent practice history

**Why it exists**: Clean separation of data access logic. Easy to modify queries or switch databases.

---

#### `progress_tracker.py` (Progress Tracking)
**Purpose**: Progress tracking and reporting functionality

**Contains**:
- Topic-level progress tracking
- Goal-level progress tracking
- Overall statistics and analytics
- Category-based performance metrics

**Key Functions**:
- `update_topic_progress(user_id, topic_id, progress_increment)` - Update topic progress
- `update_goal_progress(user_id, goal_id, correct_count, total_count)` - Update goal progress
- `get_user_progress_summary(user_id)` - Get comprehensive progress summary
- `get_practice_statistics(user_id)` - Get practice problem statistics

**Features**:
- Automatic progress calculation
- Mastery tracking (90% accuracy requirement)
- Performance by category
- Overall accuracy metrics

---

#### `ui_components.py` (UI Components)
**Purpose**: Reusable UI components and widgets

**Contains**:
- Modern styled buttons with hover effects
- Dashboard cards
- Scrollable frames with mousewheel support
- Responsive window sizing helpers

**Key Functions**:
- `create_modern_button(...)` - Create styled button
- `create_dashboard_card(...)` - Create dashboard card widget
- `create_scrollable_frame(parent, bg_color)` - Create scrollable container
- `setup_mousewheel_scrolling(window, canvas)` - Setup mousewheel scrolling
- `get_responsive_window_size(...)` - Calculate responsive dimensions

**Why it exists**: Consistent UI styling across the application. Reduces code duplication.

---

#### `login_subsystem.py` (Authentication)
**Purpose**: User authentication and session management

**Contains**:
- User registration
- Login validation
- Password hashing
- Session management

**Key Class**: `AuthService`
- `register(username, password, ...)` - Register new user
- `login(username, password)` - Authenticate user
- `logout()` - End session

---

### Setup and Utility Files

#### `main.py` (Database Initialization)
**Purpose**: Initialize the main database and create core tables

**Creates**:
- User table
- Topic table
- Goal table
- LearningObjective table
- TopicProgress table
- GoalProgress table

**Run**: `python main.py` (run once during setup)

---

#### `add_ai_tables.py` (AI Tables Migration)
**Purpose**: Add AI-specific tables to the database

**Creates**:
- UserLMSProfile table (student learning profiles)
- GenProblem table (AI-generated problems)
- PracticeProblemSet table (problem sets)
- PracticeProblem table (individual attempts)

**Run**: `python add_ai_tables.py` (run once after main.py)

---

#### `add_test_user.py` (Test User Creation)
**Purpose**: Create a test user for development/testing

**Run**: `python add_test_user.py`

---

### Documentation Files

#### `PROJECT_STRUCTURE.md`
Comprehensive guide to the codebase including:
- Detailed module descriptions
- Function signatures and purposes
- Database schema documentation
- How to add new features

#### `ARCHITECTURE.md`
System architecture documentation including:
- Module dependency diagrams
- Data flow diagrams
- Design principles
- Testing strategy

#### `DEVELOPER_GUIDE.md`
Quick start guide for developers including:
- Setup instructions
- Common tasks with code examples
- Debugging tips
- Testing checklist

#### `REFACTORING_SUMMARY.md`
Details about the code refactoring including:
- What changed and why
- Before/after comparison
- Migration guide

---

## 🗄️ Database Schema

The application uses SQLite with the following main tables:

### Core Tables

**User**
- User accounts and authentication
- Fields: id, username, password_hash, first_name, last_name, email

**Topic**
- Learning topics (e.g., "Foundations for Algebra")
- Fields: id, name, description, topic_order

**Goal**
- Learning goals within topics
- Fields: id, topic_id, title, description, goal_order

**LearningObjective**
- Specific objectives within goals
- Fields: id, goal_id, title, description, obj_order

### Progress Tables

**TopicProgress**
- User progress per topic (0-100%)
- Fields: id, user_id, topic_id, progress

**GoalProgress**
- User progress per goal (grade, completion status)
- Fields: id, user_id, goal_id, grade, is_completed

### AI Tables

**UserLMSProfile**
- Student learning profiles for adaptive AI
- Fields: user_id, preferred_learner_style, target_difficulty, preferred_length, preferred_numeric_complexity, focus_category, performance_score, ai_goal, notes

**GenProblem**
- AI-generated practice problems
- Fields: id, user_id, topic_id, goal_id, objective_id, prompt, correct_answer, category

**PracticeProblemSet**
- Sets of practice problems
- Fields: id, user_id, goal_id, created_at

**PracticeProblem**
- Individual problem attempts
- Fields: id, set_id, genProblem_id, student_answer, is_correct, is_completed

---

## 🎓 How It Works

### 1. Student Login
- Students create an account or log in
- System creates a default learning profile

### 2. Topic Selection
- Students choose a topic to study
- Or let the system pick a random topic

### 3. Goal Selection
- View available goals within the topic
- Select a goal to practice

### 4. Practice Session
- System generates personalized problems using AI
- Problems adapt to student's:
  - Learning style (visual, auditory, kinesthetic, etc.)
  - Difficulty preference (1-5)
  - Performance history
  - Focus category (weakest area)

### 5. Problem Solving
- Student answers the problem
- System provides immediate feedback
- AI generates explanations for incorrect answers
- Progress is tracked automatically

### 6. Adaptive Learning
- Every 5 problems, AI analyzes performance
- Updates student profile:
  - Adjusts difficulty
  - Identifies focus areas
  - Balances problem categories
  - Adapts learning goals

### 7. Progress Tracking
- View overall progress by topic
- See detailed goal completion
- Track performance by category
- Monitor accuracy and improvement

---

## 🧠 AI Features

### Problem Generation
- **Context-Aware**: Uses student's learning history
- **Adaptive Difficulty**: Adjusts based on performance
- **Category Balancing**: Ensures exposure to all knowledge types
  - Factual: Basic facts and definitions
  - Procedural: Step-by-step problem solving
  - Strategic: Multi-step complex problems
  - Rational: Explanations and reasoning

### Student Profiling
The AI maintains a detailed profile for each student:

- **Learning Style**: visual, auditory, reading/writing, kinesthetic, logical, social, solitary, nature
- **Target Difficulty**: 1 (Intro) to 5 (Expert)
- **Numeric Complexity**: integers, fractions, decimals, negatives, mixed, radicals
- **Focus Category**: Area needing most practice
- **Performance Score**: Overall accuracy (0-100%)
- **AI Goal**: teach_new, challenge, or review
- **Notes**: AI's observations about the student

### Feedback System
- **Correct Answers**: Encouraging feedback with next steps
- **Incorrect Answers**:
  - Explanation of the correct answer
  - Hints for understanding
  - Encouragement to try again

---

## 🛠️ Development

### Adding New Features

#### 1. New AI Functionality
Edit `ai_tutor.py`:
```python
def my_new_ai_feature(user_id):
    """Description"""
    profile = load_user_profile(user_id)
    # Your AI logic here
    return result
```

#### 2. New Database Query
Edit `database.py`:
```python
def get_my_data(user_id):
    """Description"""
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()
    cursor.execute("SELECT ... FROM ... WHERE user_id = ?", (user_id,))
    result = cursor.fetchall()
    conn.close()
    return result
```

#### 3. New UI Component
Edit `ui_components.py`:
```python
def create_my_component(parent, **kwargs):
    """Description"""
    # Create your component
    return component
```

#### 4. Change UI Colors/Fonts
Edit `config.py`:
```python
COLORS = {
    'primary': '#your-color',  # Change here
    # ...
}
```

### Testing

```bash
# Test all imports
python -c "import config; import ai_tutor; import database; import progress_tracker; import ui_components; print('OK')"

# Compile check
python -m py_compile unified_app.py

# Run the application
python unified_app.py
```

---

## 📊 Performance Metrics

The system tracks:
- **Overall Accuracy**: Percentage of correct answers
- **Category Performance**: Accuracy by knowledge type
- **Progress**: Completion percentage by topic/goal
- **Mastery**: 90% accuracy + 20 problems minimum
- **Learning Trends**: Performance over time

---

## 🔒 Security

- Passwords are hashed using secure hashing algorithms
- User sessions are managed securely
- Database uses parameterized queries to prevent SQL injection
- API keys should be kept secure (use environment variables in production)

---

## 🐛 Troubleshooting

### Common Issues

**Issue**: "No module named 'google.genai'"
```bash
# Solution: Install the package
pip install google-genai
```

**Issue**: "No such table: UserLMSProfile"
```bash
# Solution: Run the migration script
python add_ai_tables.py
```

**Issue**: "Database is locked"
```python
# Solution: Ensure all database connections are closed
conn.close()  # Always close connections
```

**Issue**: UI elements not scrolling
- Make sure you're using `create_scrollable_frame()` and `setup_mousewheel_scrolling()`

**Issue**: AI features not working
- Check that `AI_AVAILABLE` is True in config.py
- Verify your API key is correct
- Check internet connection

---

## 📝 License

[Add your license information here]

---

## 👥 Contributors

CSE423 Capstone Project Team
- [Add team member names]

---

## 📧 Contact

For questions or support:
- [Add contact information]

---

## 🙏 Acknowledgments

- Google Gemini AI for powering the adaptive learning features
- [Add other acknowledgments]

---

## 📚 Additional Resources

- **PROJECT_STRUCTURE.md** - Detailed technical documentation
- **ARCHITECTURE.md** - System design and data flow
- **DEVELOPER_GUIDE.md** - Developer quick start
- **REFACTORING_SUMMARY.md** - Code organization details

---

**Built with ❤️ for adaptive learning**