from lib.booking import Booking
import datetime

def test_creates_booking():
    # Given booking data
    # It creates a valid Booking object
    date = datetime.date(2000,1,1)
    booking = Booking(1, 1, 11, 1, date)
    assert booking.id == 1
    assert booking.host_id == 1
    assert booking.guest_id == 11
    assert booking.space_id == 1
    assert booking.dates == date
    assert booking.confirmed == False

def test_compares_to_similar_object():
    # Given two booking objects
    # It compares their contents
    date = datetime.date(2000,1,1)
    booking_1 = Booking(1, 1, 11, 1, date)
    booking_2 = Booking(1, 1, 11, 1, date)
    assert booking_1 == booking_2

def test_outputs_string_when_called():
    # Given a Booking object
    # It returns a string when called
    date = datetime.date(2000,1,1)
    booking = Booking(1, 1, 11, 1, date)
    assert str(booking) == "Booking(1, 1, 11, 1, 2000-01-01, False)"

def test_confirmed_booking():
    date = datetime.date(2000,1,1)
    booking = Booking(1, 1, 11, 1, date)
    booking.confirmed_booking()
    assert booking.confirmed == True