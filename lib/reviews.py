from .connect import conn,cursor

class User:
    def __init__(self, username, password, email, phone, role):
        self.username = username
        self.password = password
        self.email = email
        self.phone = phone
        self.role = role

    def save(self):
        cursor.cursor.execute('''
            INSERT INTO users (username, password, email, phone, role)
            VALUES (?, ?, ?, ?, ?)
        ''', (self.username, self.password, self.email, self.phone, self.role))
        conn.commit()