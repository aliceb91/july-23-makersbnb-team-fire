from datetime import datetime, timedelta

class Space():
    def __init__(self, id, name, description, price_per_night, start_date, end_date, user_id):
        self.id = id
        self.name = name
        self.description = description
        self.price_per_night = price_per_night
        self.user_id = user_id
        self.start_date = start_date
        self.end_date = end_date
        self.available_dates = []
        self.bookings = []

    def __eq__(self, other):
        return self.__dict__ == other.__dict__
    
    def __repr__(self):
        return f"Space({self.id}, {self.name}, {self.description}, {self.price_per_night}, {self.start_date}, {self.end_date}, {self.user_id})"

    def dates_generator(self):
        current_date = self.start_date
        while current_date <= self.end_date:
            date_taken = False
            if self.bookings == []:
                self.available_dates.append(current_date)
                current_date += timedelta(days=1)
            else:
                for booking in self.bookings:
                    if booking['date'] == current_date:
                        date_taken = True
                if date_taken == False:
                    self.available_dates.append(current_date)
                    current_date += timedelta(days=1)
                else:
                    current_date += timedelta(days=1)

    def make_booking(self, guest_user, date):
        booking = {
            "host_user_id": self.user_id,
            "guest_user_id": guest_user,
            "date": date
        }
        self.bookings.append(booking)