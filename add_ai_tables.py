"""
Database migration script to add AI-related tables
Run this to add GenProblem, PracticeProblemSet, and PracticeProblem tables
"""

import sqlite3
import os

DB_PATH = "learning_platform.db"

def add_ai_tables():
    """Add AI-related tables to the database"""
    
    if not os.path.exists(DB_PATH):
        print(f"ERROR: Database {DB_PATH} not found!")
        print("Please run main.py first to create the database.")
        return False
    
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()
    
    print("=" * 60)
    print("Adding AI-related tables to database...")
    print("=" * 60)
    
    # Check if tables already exist
    cursor.execute("SELECT name FROM sqlite_master WHERE type='table'")
    existing_tables = [row[0] for row in cursor.fetchall()]
    print(f"\nExisting tables: {', '.join(existing_tables)}")
    
    tables_to_create = []
    
    # GenProblem table
    if 'GenProblem' not in existing_tables:
        tables_to_create.append(('GenProblem', """
            CREATE TABLE GenProblem (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                user_id INTEGER NOT NULL,
                topic_id INTEGER NOT NULL,
                goal_id INTEGER NOT NULL,
                objective_id INTEGER NOT NULL,
                prompt TEXT NOT NULL,
                correct_answer TEXT NOT NULL,
                category TEXT NOT NULL CHECK (category IN ('factual', 'procedural', 'strategic', 'rational')),
                FOREIGN KEY (topic_id) REFERENCES Topic(id),
                FOREIGN KEY (goal_id) REFERENCES Goal(id),
                FOREIGN KEY (objective_id) REFERENCES LearningObjective(id)
            )
        """))
    
    # PracticeProblemSet table
    if 'PracticeProblemSet' not in existing_tables:
        tables_to_create.append(('PracticeProblemSet', """
            CREATE TABLE PracticeProblemSet (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                user_id INTEGER NOT NULL,
                goal_id INTEGER NOT NULL,
                start_time DATETIME DEFAULT CURRENT_TIMESTAMP,
                grade INTEGER DEFAULT 0,
                is_complete BOOLEAN DEFAULT FALSE,
                FOREIGN KEY (user_id) REFERENCES User(id),
                FOREIGN KEY (goal_id) REFERENCES Goal(id)
            )
        """))
    
    # PracticeProblem table
    if 'PracticeProblem' not in existing_tables:
        tables_to_create.append(('PracticeProblem', """
            CREATE TABLE PracticeProblem (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                set_id INTEGER NOT NULL,
                genProblem_id INTEGER NOT NULL,
                student_answer TEXT,
                is_correct BOOLEAN,
                is_completed BOOLEAN DEFAULT FALSE,
                FOREIGN KEY (set_id) REFERENCES PracticeProblemSet(id),
                FOREIGN KEY (genProblem_id) REFERENCES GenProblem(id),
                UNIQUE (set_id, genProblem_id)
            )
        """))

    # UserLMSProfile table
    if 'UserLMSProfile' not in existing_tables:
        tables_to_create.append(('UserLMSProfile', """
            CREATE TABLE UserLMSProfile (
                user_id INTEGER PRIMARY KEY,
                preferred_learner_style TEXT,
                target_difficulty INTEGER,
                preferred_length TEXT,
                preferred_numeric_complexity TEXT,
                focus_category TEXT,
                performance_score REAL,
                ai_goal TEXT,
                notes TEXT,
                last_updated DATETIME DEFAULT CURRENT_TIMESTAMP,
                FOREIGN KEY (user_id) REFERENCES User(id)
            )
        """))

    if not tables_to_create:
        print("\n✅ All AI tables already exist!")
        conn.close()
        return True
    
    print(f"\n📝 Creating {len(tables_to_create)} missing table(s)...")
    
    try:
        for table_name, create_sql in tables_to_create:
            print(f"   Creating {table_name}...", end=" ")
            cursor.execute(create_sql)
            print("✅")
        
        conn.commit()
        print("\n✅ Successfully added all AI tables!")
        print("\nYou can now run unified_app.py")
        
    except sqlite3.Error as e:
        print(f"\n❌ Error creating tables: {e}")
        conn.rollback()
        return False
    
    finally:
        conn.close()
    
    return True

if __name__ == "__main__":
    success = add_ai_tables()
    if success:
        print("\n" + "=" * 60)
        print("Database migration completed successfully!")
        print("=" * 60)
    else:
        print("\n" + "=" * 60)
        print("Database migration failed!")
        print("=" * 60)

