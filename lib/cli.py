# lib/cli.py
from connect import conn,cursor
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

class Booking:
    def __init__(self, user_id, listing_id, booking_date, status, payment_status):
        self.user_id = user_id
        self.listing_id = listing_id
        self.date = booking_date
        self.status = status
        self.payment_status = payment_status

    def save(self):
        cursor.cursor.execute('''
            INSERT INTO bookings (user_id, listing_id, date, status, payment_status)
            VALUES (?, ?, ?, ?, ?)
        ''', (self.user_id, self.listing_id, self.date, self.status, self.payment_status))
        conn.commit()

class Review:
    def __init__(self, user_id, listing_id, rating, comment, review_date):
        self.user_id = user_id
        self.listing_id = listing_id
        self.rating = rating
        self.comment = comment
        self.date = review_date

    def save(self):
        cursor.cursor.execute('''
            INSERT INTO reviews (user_id, listing_id, rating, comment, date)
            VALUES (?, ?, ?, ?, ?)
        ''', (self.user_id, self.listing_id, self.rating, self.comment, self.date))
        conn.commit()


new_user = User(username="Steve_Obala", password="password123", email="steveobala1@gmail.com", phone="1234567890", role="user")
new_user.save(db)

new_listing = Listing(name="Grand Hotel", location="123 Main St", category="hotel", description="A grand hotel", average_rating=4.5)
new_listing.save(db)

new_booking = Booking(user_id=1, listing_id=1, booking_date=date.today(), status="confirmed", payment_status="paid")
new_booking.save(db)

new_review = Review(user_id=1, listing_id=1, rating=5, comment="Great stay!", review_date=date.today())
new_review.save(db)

# Query to ensure data is added
db.cursor.execute('SELECT * FROM users WHERE username = ?', ("Steve_ obala",))
user = db.cursor.fetchone()
print(f"Added user: {user}")

db.cursor.execute('SELECT * FROM listings WHERE name = ?', ("Grand Hotel",))
listing = db.cursor.fetchone()
print(f"Added listing: {listing}")

db.cursor.execute('SELECT * FROM bookings WHERE user_id = ? AND listing_id = ?', (1, 1))
booking = db.cursor.fetchone()
print(f"Added booking: {booking}")

db.cursor.execute('SELECT * FROM reviews WHERE user_id = ? AND listing_id = ?', (1, 1))
review = db.cursor.fetchone()
print(f"Added review: {review}")
