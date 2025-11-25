# System Architecture

## Module Dependency Diagram

```
┌─────────────────────────────────────────────────────────────┐
│                      unified_app.py                          │
│                   (Main Application)                         │
│  - Login Screen                                              │
│  - Dashboard                                                 │
│  - Topic/Goal Selection                                      │
│  - Practice Sessions                                         │
│  - Progress Dashboard                                        │
└────────┬────────┬────────┬────────┬────────┬────────────────┘
         │        │        │        │        │
         ▼        ▼        ▼        ▼        ▼
    ┌────────┐ ┌──────┐ ┌──────┐ ┌──────┐ ┌──────────────┐
    │config  │ │ai    │ │data  │ │prog  │ │ui            │
    │.py     │ │tutor │ │base  │ │ress  │ │components    │
    │        │ │.py   │ │.py   │ │track │ │.py           │
    └────────┘ └──┬───┘ └──────┘ │er.py │ └──────────────┘
                  │               └──────┘
                  │
                  ▼
            ┌──────────┐
            │config.py │
            └──────────┘
                  │
                  ▼
         ┌────────────────┐
         │Google Gemini AI│
         └────────────────┘

         All modules connect to:
                  │
                  ▼
         ┌────────────────┐
         │learning_       │
         │platform.db     │
         │(SQLite)        │
         └────────────────┘
```

## Data Flow

### 1. User Login Flow
```
User Input → unified_app.py → login_subsystem.py → Database
                                                      ↓
                                              Authenticate
                                                      ↓
                                              Set current_user
```

### 2. Problem Generation Flow
```
User selects objective → unified_app.py
                              ↓
                    load_user_profile() [ai_tutor.py]
                              ↓
                    generate_problem() [ai_tutor.py]
                              ↓
                    Google Gemini AI
                              ↓
                    save_generated_problem() [database.py]
                              ↓
                    Display problem [unified_app.py]
```

### 3. Answer Submission Flow
```
User submits answer → unified_app.py
                              ↓
                    record_practice_attempt() [database.py]
                              ↓
                    update_goal_progress() [progress_tracker.py]
                              ↓
                    Profile_Alg() [ai_tutor.py] (every 5 problems)
                              ↓
                    Generate AI feedback [unified_app.py + client]
```

### 4. Progress Tracking Flow
```
User views progress → unified_app.py
                              ↓
                    get_user_progress_summary() [progress_tracker.py]
                              ↓
                    get_practice_statistics() [progress_tracker.py]
                              ↓
                    Display progress [unified_app.py]
```

## Module Responsibilities

### config.py
- **Responsibility**: Configuration and constants
- **Dependencies**: google.genai (optional)
- **Exports**: DB_PATH, COLORS, FONTS, client, AI_AVAILABLE

### ai_tutor.py
- **Responsibility**: AI-powered tutoring
- **Dependencies**: config.py, sqlite3
- **Exports**: load_user_profile, generate_problem, Profile_Alg, get_full_performance

### database.py
- **Responsibility**: Database operations
- **Dependencies**: config.py, sqlite3
- **Exports**: All database query functions

### progress_tracker.py
- **Responsibility**: Progress tracking and analytics
- **Dependencies**: config.py, sqlite3
- **Exports**: update_topic_progress, update_goal_progress, get_user_progress_summary

### ui_components.py
- **Responsibility**: Reusable UI widgets
- **Dependencies**: config.py, tkinter
- **Exports**: create_modern_button, create_dashboard_card, create_scrollable_frame

### unified_app.py
- **Responsibility**: Application orchestration
- **Dependencies**: All above modules + login_subsystem.py
- **Exports**: None (main entry point)

## Design Principles

### 1. Separation of Concerns
Each module has a single, well-defined responsibility.

### 2. Dependency Injection
Configuration is centralized in config.py and imported where needed.

### 3. Loose Coupling
Modules interact through well-defined interfaces (function calls).

### 4. High Cohesion
Related functionality is grouped together in the same module.

### 5. DRY (Don't Repeat Yourself)
Common UI components and database queries are reused.

## Testing Strategy

### Unit Tests (Recommended)
- **config.py**: Test configuration loading
- **ai_tutor.py**: Test profile loading, problem generation (with mocked AI)
- **database.py**: Test all database operations (with test database)
- **progress_tracker.py**: Test progress calculations
- **ui_components.py**: Test component creation

### Integration Tests (Recommended)
- Test complete user flows (login → select topic → practice → view progress)
- Test AI integration (problem generation → submission → feedback)
- Test database persistence

## Scalability Considerations

### Adding New Features
1. **New AI functionality** → Add to ai_tutor.py
2. **New database tables** → Add queries to database.py
3. **New progress metrics** → Add to progress_tracker.py
4. **New UI components** → Add to ui_components.py
5. **New screens** → Add to unified_app.py

### Performance Optimization
- Database queries are already optimized with proper JOINs
- AI calls are batched (profile updates every 5 problems)
- UI is responsive with scrollable containers

### Future Enhancements
- Add caching layer for frequently accessed data
- Implement async AI calls for better responsiveness
- Add database connection pooling
- Implement logging throughout the application
- Add error tracking and monitoring

