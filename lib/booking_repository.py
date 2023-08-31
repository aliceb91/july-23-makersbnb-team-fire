from lib.booking import Booking

class BookingRepository:
    # CRUD methods for booking class 
    def __init__(self, connection):
        # Stores connection object 
        self._connection = connection

    def add(self, booking):
        # Adds booking to the database 
        self._connection.execute("INSERT INTO bookings(host_id, guest_id, space_id, dates) VALUES (%s, %s, %s, %s)",[booking.host_id, booking.guest_id, booking.space_id, booking.dates])
        return None 

    def all(self): 
        # Gets all bookings from the database 
        rows = self._connection.execute("SELECT * FROM bookings")
        bookings = []
        for row in rows: 
            booking = Booking(row['id'], row['host_id'], row['guest_id'], row['space_id'], row['dates'])
            bookings.append(booking)
        return bookings

    def update(self, id, booking):
        # Updates and existing booking
        self._connection.execute("UPDATE bookings SET host_id=%s, guest_id=%s, space_id=%s, dates=%s WHERE id=%s", [booking.host_id, booking.guest_id, booking.space_id, booking.dates, id])
        return None

    def delete(self, id):
        # Deletes a specified booking from the database.
        self._connection.execute("DELETE FROM bookings WHERE id=%s", [id])
        return None
    
    def find(self,id):
        rows = self._connection.execute("SELECT * FROM bookings WHERE id=%s", [id])
        row = rows[0]
        return Booking(row['id'], row['host_id'], row['guest_id'], row['space_id'], row['dates'])