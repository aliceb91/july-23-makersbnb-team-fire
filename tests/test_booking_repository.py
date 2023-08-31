from lib.booking_repository import * 
from unittest.mock import Mock 
import datetime

def test_get_all(db_connection): 
    db_connection.seed("seeds/booking.sql")
    repository = BookingRepository(db_connection)
    bookings = repository.all()
    result = []
    for booking in bookings:
        result.append(str(booking))
    assert result == [
        "Booking(1, 1, 11, 1, 2000-01-01, False)", 
        "Booking(2, 2, 12, 2, 2000-01-02, False)"
    ]


def test_add_to_database(db_connection): 
    db_connection.seed("seeds/booking.sql")
    repository = BookingRepository(db_connection)
    booking = Mock()
    booking.host_id = 3
    booking.guest_id = 13
    booking.space_id = 3
    booking.dates = datetime.date(2000,1,3)
    repository.add(booking)
    bookings = repository.all()
    result = []
    for booking in bookings:
        result.append(str(booking))
    assert result == [
        "Booking(1, 1, 11, 1, 2000-01-01, False)", 
        "Booking(2, 2, 12, 2, 2000-01-02, False)",
        "Booking(3, 3, 13, 3, 2000-01-03, False)"
    ]

def test_update_booking(db_connection):
    db_connection.seed("seeds/booking.sql")
    repository = BookingRepository(db_connection)
    updated_booking = Mock()
    updated_booking.host_id = 4
    updated_booking.guest_id = 14
    updated_booking.space_id = 4
    updated_booking.dates = datetime.date(2000,1,4)
    repository.update(2, updated_booking)
    bookings = repository.all()
    result = []
    for booking in bookings:
        result.append(str(booking))
    assert result == [
        "Booking(1, 1, 11, 1, 2000-01-01, False)", 
        "Booking(2, 4, 14, 4, 2000-01-04, False)"
    ]

def test_delete_booking(db_connection):
    db_connection.seed("seeds/booking.sql")
    repository = BookingRepository(db_connection)
    repository.delete(1)
    bookings = repository.all()
    result = []
    for booking in bookings:
        result.append(str(booking))
    assert result == [
        "Booking(2, 2, 12, 2, 2000-01-02, False)"
    ]
