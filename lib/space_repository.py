class SpaceRepository:
    # CRUD methods for space class 
    def __init__(self, connection):
        # Stores connection object 
        self._connection = connection

    def add(self, space):
        # Adds space to the database 
        self._connection.execute("INSERT INTO spaces(name, description, price_per_night) VALUES (%s, %s, %s)",[space.name, space.description, space.price_per_night])
        return None 

    def all(self): 
        # Gets all spaces from the database 
        rows = self._connection.execute("SELECT * FROM spaces")
        spaces = []
        for row in rows: 
            space = f"{row['id']}, {row['name']}, {row['description']}, {row['price_per_night']}"
            spaces.append(space)
        return spaces