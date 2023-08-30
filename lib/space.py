from datetime import datetime, timedelta

class Space():
    def __init__(self, id, name, description, price_per_night, user_id):
        self.id = id
        self.name = name
        self.description = description
        self.price_per_night = price_per_night
        self.user_id = user_id
        self.available_dates = []

    def __eq__(self, other):
        return self.__dict__ == other.__dict__
    
    def __repr__(self):
        return f"Space({self.id}, {self.name}, {self.description}, {self.price_per_night}, {self.user_id})"

    def dates_generator(self, start_date, end_date):
        current_date = start_date
        while current_date <= end_date:
            self.available_dates.append(current_date)
            current_date += timedelta(days=1)
