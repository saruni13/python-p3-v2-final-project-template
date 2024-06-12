from .connect import get_db_connection


def create_table():
    conn = get_db_connection()
    cursor=conn.cursor()
    
    cursor.execute('''
       CREATE TABLE IF NOT EXISTS users (
         id INTEGER PRIMARY KEY AUTOINCREMENT,
         username TEXT NOT NULL,
        password TEXT NOT NULL,
        email TEXT NOT NULL,
        phone TEXT NOT NULL,
       role TEXT NOT NULL
''')
    cursor.execute('''
       CREATE TABLE IF NOT EXISTS listings (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
         name TEXT NOT NULL,
         location TEXT NOT NULL,
         category TEXT NOT NULL,
         description TEXT,
         average_rating REAL
)
''')

    cursor.execute('''
     CREATE TABLE IF NOT EXISTS bookings (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    user_id INTEGER NOT NULL,
    listing_id INTEGER NOT NULL,
    date DATE NOT NULL,
    status TEXT NOT NULL,
    payment_status TEXT NOT NULL,
    FOREIGN KEY (user_id) REFERENCES users(id),
    FOREIGN KEY (listing_id) REFERENCES listings(id)
)
''')

    cursor.execute('''
    CREATE TABLE IF NOT EXISTS reviews (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    user_id INTEGER NOT NULL,
    listing_id INTEGER NOT NULL,
    rating INTEGER NOT NULL,
    comment TEXT,
    date DATE NOT NULL,
    FOREIGN KEY (user_id) REFERENCES users(id),
    FOREIGN KEY (listing_id) REFERENCES listings(id)
)
''')

    conn.commit()
    conn.close()
def execute_query(query, params=None):
    conn = get_db_connection()
    cursor = conn.cursor()
    if params:
        cursor.execute(query, params)
    else:
        cursor.execute(query)
    conn.commit()
    conn.close()

def fetch_all(query, params=None):
    conn = get_db_connection()
    cursor = conn.cursor()
    if params:
        cursor.execute(query, params)
    else:
        cursor.execute(query)
    records = cursor.fetchall()
    conn.close()
    return records

if __name__== "_main_":
   create_table()