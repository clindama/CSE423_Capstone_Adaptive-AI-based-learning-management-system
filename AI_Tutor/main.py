import sqlite3
from faker import Faker
import random


conn = sqlite3.connect("learning_platform.db")  
cursor = conn.cursor()


with open("tables.sql", "r") as f:
    schema = f.read()
cursor.executescript(schema)


fake = Faker()


def create_users(n=10):
    account_types = ['student', 'parent', 'admin']
    for _ in range(n):
        username = fake.user_name()
        password = fake.password()
        first = fake.first_name()
        last = fake.last_name()
        email = fake.email()
        acc_type = random.choice(account_types)
        try:
            cursor.execute('''
                INSERT INTO User (username, password, first_name, last_name, email, account_type)
                VALUES (?, ?, ?, ?, ?, ?)
            ''', (username, password, first, last, email, acc_type))
        except sqlite3.IntegrityError:
            pass  


def create_topics(n=5):
    for i in range(n):
        name = f"Topic {i+1}"
        desc = fake.sentence()
        order = i + 1
        try:
            cursor.execute('''
                INSERT INTO Topic (name, description, topic_order)
                VALUES (?, ?, ?)
            ''', (name, desc, order))
        except sqlite3.IntegrityError:
            pass


def create_topic_progress():
    cursor.execute("SELECT id FROM User WHERE account_type = 'student'")
    student_ids = [row[0] for row in cursor.fetchall()]
    cursor.execute("SELECT id FROM Topic")
    topic_ids = [row[0] for row in cursor.fetchall()]
    
    for student_id in student_ids:
        for topic_id in topic_ids:
            progress = random.randint(0, 100)
            try:
                cursor.execute('''
                    INSERT INTO TopicProgress (user_id, topic_id, progress)
                    VALUES (?, ?, ?)
                ''', (student_id, topic_id, progress))
            except sqlite3.IntegrityError:
                pass


create_users()
create_topics()
create_topic_progress()


conn.commit()
print("Database seeded with dummy data.")

for row in cursor.execute("SELECT id, username, email, account_type FROM User LIMIT 5"):
    print(row)

conn.close()
