# Developer Quick Start Guide

## Welcome! 👋

This guide will help you get started with the Adaptive AI-based Learning Management System codebase.

## Prerequisites

- Python 3.8 or higher
- Basic knowledge of Python, Tkinter, and SQLite
- Google Gemini API key (for AI features)

## Setup

### 1. Install Dependencies
```bash
pip install google-genai
```

### 2. Initialize Database
```bash
python main.py              # Create database and tables
python add_ai_tables.py     # Add AI-specific tables
```

### 3. Run the Application
```bash
python unified_app.py
```

## Project Structure Overview

```
📁 Project Root
├── 📄 unified_app.py          # Main application - START HERE
├── 📄 config.py               # Configuration and constants
├── 📄 ai_tutor.py            # AI tutoring logic
├── 📄 database.py            # Database operations
├── 📄 progress_tracker.py    # Progress tracking
├── 📄 ui_components.py       # Reusable UI components
├── 📄 login_subsystem.py     # Authentication (existing)
├── 📄 learning_platform.db   # SQLite database
└── 📁 AI_Tutor/              # Reference implementation
```

## Common Tasks

### Task 1: Change UI Colors
**File**: `config.py`
```python
# Edit the COLORS dictionary
COLORS = {
    'primary': '#2563eb',      # Change this to your color
    'success': '#10b981',      # Change this too
    # ... etc
}
```

### Task 2: Modify AI Prompts
**File**: `ai_tutor.py`
```python
# Find the function you want to modify:
# - generate_problem() - Problem generation prompt
# - Profile_Alg() - Profile update prompt
# - load_context() - Context generation

# Edit the prompt string inside the function
```

### Task 3: Add a New Database Query
**File**: `database.py`
```python
# Add your new function
def get_my_new_data(user_id):
    """Description of what this does"""
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()
    
    cursor.execute("SELECT ... FROM ... WHERE ...", (user_id,))
    result = cursor.fetchall()
    
    conn.close()
    return result
```

**File**: `unified_app.py`
```python
# Import it at the top
from database import (
    # ... existing imports ...
    get_my_new_data  # Add your new function
)

# Use it in your code
data = get_my_new_data(current_user_id)
```

### Task 4: Add a New UI Screen
**File**: `unified_app.py`
```python
def show_my_new_screen(parent_window):
    """Display my new screen"""
    # Create window
    window = tk.Toplevel()
    window.title("My New Screen")
    
    # Get responsive size
    width, height = get_responsive_window_size(window, 800, 600)
    window.geometry(f"{width}x{height}")
    
    # Create scrollable content
    container, content, canvas = create_scrollable_frame(window)
    container.pack(fill='both', expand=True, padx=20, pady=20)
    
    # Add your content to 'content' frame
    tk.Label(content, text="Hello!", font=FONTS['heading']).pack()
    
    # Add buttons
    create_modern_button(
        content, 
        "Click Me", 
        lambda: print("Clicked!"),
        COLORS['primary']
    ).pack()
    
    # Setup scrolling
    setup_mousewheel_scrolling(window, canvas)
```

### Task 5: Modify Progress Tracking
**File**: `progress_tracker.py`
```python
# Add new progress metric
def get_my_custom_metric(user_id):
    """Calculate custom metric"""
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()
    
    # Your query here
    cursor.execute("SELECT ... FROM ... WHERE user_id = ?", (user_id,))
    result = cursor.fetchone()
    
    conn.close()
    return result
```

## Code Style Guidelines

### 1. Function Documentation
```python
def my_function(param1, param2):
    """
    Brief description of what this function does
    
    Args:
        param1: Description of param1
        param2: Description of param2
        
    Returns:
        Description of return value
    """
    # Implementation
```

### 2. Database Operations
```python
# Always use context or close connections
conn = sqlite3.connect(DB_PATH)
cursor = conn.cursor()

try:
    # Your operations
    cursor.execute("...")
    conn.commit()
finally:
    conn.close()
```

### 3. UI Components
```python
# Use constants from config.py
bg_color = COLORS['bg_secondary']
font = FONTS['heading']

# Use helper functions from ui_components.py
button = create_modern_button(parent, "Text", command, COLORS['primary'])
```

## Debugging Tips

### 1. Check Database
```bash
sqlite3 learning_platform.db
.tables                    # List all tables
.schema TableName          # Show table structure
SELECT * FROM User;        # Query data
```

### 2. Test AI Functions
```python
# In Python console
from ai_tutor import load_user_profile, generate_problem

profile = load_user_profile(1)
print(profile)

problem, answer, category = generate_problem("Title", "Description", profile)
print(f"Problem: {problem}")
print(f"Answer: {answer}")
print(f"Category: {category}")
```

### 3. Check Imports
```python
# Test all imports
python -c "import config; import ai_tutor; import database; import progress_tracker; import ui_components; print('OK')"
```

## Common Issues

### Issue 1: "No module named 'google.genai'"
**Solution**: Install the package
```bash
pip install google-genai
```

### Issue 2: "No such table: UserLMSProfile"
**Solution**: Run the migration script
```bash
python add_ai_tables.py
```

### Issue 3: "Database is locked"
**Solution**: Close all connections properly
```python
# Always close connections
conn.close()
```

### Issue 4: UI elements not scrolling
**Solution**: Make sure you're using create_scrollable_frame and setup_mousewheel_scrolling
```python
container, content, canvas = create_scrollable_frame(window)
setup_mousewheel_scrolling(window, canvas)
```

## Testing Checklist

Before committing changes:
- [ ] Code compiles without errors: `python -m py_compile filename.py`
- [ ] All imports work
- [ ] Database operations close connections
- [ ] UI is responsive and scrollable
- [ ] No hardcoded values (use config.py)
- [ ] Functions are documented
- [ ] Code follows existing style

## Resources

- **PROJECT_STRUCTURE.md** - Detailed module documentation
- **ARCHITECTURE.md** - System architecture and data flow
- **REFACTORING_SUMMARY.md** - What changed during refactoring
- **AI_Tutor/advanceAIDemo.py** - Reference implementation

## Getting Help

1. Check the documentation files listed above
2. Look at existing code for examples
3. Search for similar functionality in the codebase
4. Check the database schema in `AI_Tutor/tables.sql`

## Next Steps

1. Read **PROJECT_STRUCTURE.md** for detailed module information
2. Explore the codebase starting with `unified_app.py`
3. Try making a small change (e.g., change a color in config.py)
4. Run the application and test your change

Happy coding! 🚀

