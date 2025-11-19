import sqlite3

# Connect to the database
conn = sqlite3.connect("learning_platform.db")
cursor = conn.cursor()

# Check if user already exists
cursor.execute("SELECT username FROM User WHERE username = ?", ("student1",))
existing = cursor.fetchone()

if existing:
    print("User 'student1' already exists. Updating password...")
    cursor.execute("UPDATE User SET password = ? WHERE username = ?", ("test123", "student1"))
else:
    print("Creating new user 'student1'...")
    cursor.execute('''
        INSERT INTO User (username, password, first_name, last_name, email, account_type)
        VALUES (?, ?, ?, ?, ?, ?)
    ''', ("student1", "test123", "Test", "Student", "student1@example.com", "student"))

conn.commit()
print("\n✅ Test user created successfully!")
print("\n📝 Login credentials:")
print("   Username: student1")
print("   Password: test123")
print("\nYou can now login with these credentials to test the BRD-compliant tutoring flow!")

conn.close()

