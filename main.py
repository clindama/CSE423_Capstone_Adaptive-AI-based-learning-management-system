import sqlite3

# Connect to your new DB
db_name = "learning_platform.db"
conn = sqlite3.connect(db_name)
cursor = conn.cursor()

# --- Seed objectives first ---
with open("seed_objectives.sql", "r", encoding="utf-8") as f:
    objectives_sql = f.read()
cursor.executescript(objectives_sql)
print("✅ seed_objectives.sql inserted successfully.")

# --- Then seed instruction methods + content ---
with open("seed_instruction.sql", "r", encoding="utf-8") as f:
    instruction_sql = f.read()
cursor.executescript(instruction_sql)
print("✅ seed_instruction.sql inserted successfully.")

conn.commit()
conn.close()

print("🎉 Database seeding complete!")
