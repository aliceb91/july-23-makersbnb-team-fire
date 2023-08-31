class Booking():
    def __init__(self, id, host_id, guest_id, space_id, dates):
        self.id = id
        self.host_id = host_id
        self.guest_id = guest_id
        self.space_id = space_id
        self.dates = dates
        self.confirmed = False

    def __eq__(self, other):
        return self.__dict__ == other.__dict__
    
    def __repr__(self):
        return f"Booking({self.id}, {self.host_id}, {self.guest_id}, {self.space_id}, {self.dates}, {self.confirmed})"
    
    def confirmed_booking(self):
        self.confirmed = True