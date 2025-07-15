import sqlite3

# Connect to your database
conn = sqlite3.connect("learning_platform.db")
cursor = conn.cursor()

# Load and execute schema
with open("test.sql", "r") as f:
    schema_sql = f.read()
cursor.executescript(schema_sql)

# Load and execute topic/goal data
with open("toplist.sql", "r") as f:
    topic_data_sql = f.read()
cursor.executescript(topic_data_sql)

# Add default admin user
cursor.execute('''
    INSERT INTO User (username, password, first_name, last_name, email, account_type)
    VALUES (?, ?, ?, ?, ?, ?)
''', ("admin", "1234", "Admin", "User", "admin@example.com", "admin"))

conn.commit()
print("Database initialized and seeded.")
conn.close()
