# login_subsystem.py
import sqlite3

class LoginForm:
    def __init__(self, auth_service):
        self.auth_service = auth_service

    def submit_form(self, username, password):
        return self.auth_service.authenticate(username, password)


class RegisteredUser:
    def __init__(self, username, password):
        self.username = username
        self.password = password

    def get_user_info(self):
        return {"username": self.username}


class AuthService:
    
    def __init__(self, db_path="learning_platform.db"):
        self.db_path = db_path
        self.current_user = None

    def authenticate(self, username, password):
        conn = sqlite3.connect(self.db_path)
        cursor = conn.cursor()

        cursor.execute('''
            SELECT id, username, password FROM User
            WHERE username = ? AND password = ?
        ''', (username, password))

        row = cursor.fetchone()
        conn.close()

        if row:
            self.current_user = RegisteredUser(username=row[1], password=row[2])
            return True
        else:
            return False

    def register(self, username, password, email, first_name, last_name, account_type='student'):
        conn = sqlite3.connect(self.db_path)
        cursor = conn.cursor()

        try:
            cursor.execute('''
                INSERT INTO User (username, password, first_name, last_name, email, account_type)
                VALUES (?, ?, ?, ?, ?, ?)
            ''', (username, password, first_name, last_name, email, account_type))
            conn.commit()
            return True
        except sqlite3.IntegrityError:
            return False
        finally:
            conn.close()

    def logout(self):
        self.current_user = None
    