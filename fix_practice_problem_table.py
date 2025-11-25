"""
Migration script to fix PracticeProblem table schema
Changes problem_id to genProblem_id to match advanceAIDemo.py
"""

import sqlite3
import os

DB_PATH = "learning_platform.db"

def fix_practice_problem_table():
    """Fix the PracticeProblem table to use genProblem_id instead of problem_id"""
    
    if not os.path.exists(DB_PATH):
        print(f"ERROR: Database {DB_PATH} not found!")
        return False
    
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()
    
    print("=" * 60)
    print("Fixing PracticeProblem table schema...")
    print("=" * 60)
    
    try:
        # Check if table exists
        cursor.execute("SELECT name FROM sqlite_master WHERE type='table' AND name='PracticeProblem'")
        if not cursor.fetchone():
            print("\n❌ PracticeProblem table does not exist!")
            return False
        
        # Check current schema
        cursor.execute("PRAGMA table_info(PracticeProblem)")
        columns = cursor.fetchall()
        column_names = [col[1] for col in columns]
        
        print(f"\nCurrent columns: {', '.join(column_names)}")
        
        # Check if we need to migrate
        if 'genProblem_id' in column_names:
            print("\n✅ Table already has genProblem_id column!")
            return True
        
        if 'problem_id' not in column_names:
            print("\n❌ Table doesn't have problem_id column either!")
            return False
        
        print("\n📝 Migrating from problem_id to genProblem_id...")
        
        # Step 1: Get existing data
        print("   1. Backing up existing data...", end=" ")
        cursor.execute("SELECT * FROM PracticeProblem")
        existing_data = cursor.fetchall()
        print(f"✅ ({len(existing_data)} rows)")
        
        # Step 2: Drop the old table
        print("   2. Dropping old table...", end=" ")
        cursor.execute("DROP TABLE PracticeProblem")
        print("✅")
        
        # Step 3: Create new table with correct schema
        print("   3. Creating new table...", end=" ")
        cursor.execute("""
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
        """)
        print("✅")
        
        # Step 4: Restore data (if any)
        if existing_data:
            print(f"   4. Restoring {len(existing_data)} rows...", end=" ")
            # Assuming the old schema was: id, set_id, problem_id, student_answer, is_correct, is_completed
            for row in existing_data:
                cursor.execute("""
                    INSERT INTO PracticeProblem (id, set_id, genProblem_id, student_answer, is_correct, is_completed)
                    VALUES (?, ?, ?, ?, ?, ?)
                """, row)
            print("✅")
        else:
            print("   4. No data to restore (table was empty)")
        
        # Commit changes
        conn.commit()
        
        # Verify new schema
        cursor.execute("PRAGMA table_info(PracticeProblem)")
        new_columns = cursor.fetchall()
        new_column_names = [col[1] for col in new_columns]
        
        print(f"\n✅ Migration successful!")
        print(f"New columns: {', '.join(new_column_names)}")
        
        return True
        
    except sqlite3.Error as e:
        print(f"\n❌ Error during migration: {e}")
        conn.rollback()
        return False
    
    finally:
        conn.close()

if __name__ == "__main__":
    print("\n⚠️  WARNING: This will modify the PracticeProblem table!")
    print("Make sure you have a backup of your database if needed.\n")
    
    response = input("Continue? (yes/no): ").strip().lower()
    
    if response == 'yes':
        success = fix_practice_problem_table()
        if success:
            print("\n" + "=" * 60)
            print("✅ Database migration completed successfully!")
            print("=" * 60)
        else:
            print("\n" + "=" * 60)
            print("❌ Database migration failed!")
            print("=" * 60)
    else:
        print("\nMigration cancelled.")

