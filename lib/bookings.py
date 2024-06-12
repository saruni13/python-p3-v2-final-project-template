from .connect import conn,cursor

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