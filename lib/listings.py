from .connect import conn,cursor

class Listing:
    def __init__(self, name, location, category, description=None, average_rating=None):
        self.name = name
        self.location = location
        self.category = category
        self.description = description
        self.average_rating = average_rating

    def save(self):
        cursor.cursor.execute('''
            INSERT INTO listings (name, location, category, description, average_rating)
            VALUES (?, ?, ?, ?, ?)
        ''', (self.name, self.location, self.category, self.description, self.average_rating))
        conn.commit()