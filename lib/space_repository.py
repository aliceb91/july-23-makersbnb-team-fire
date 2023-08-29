from lib.space import Space

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
            space = Space(row['id'], row['name'], row['description'], row['price_per_night'])
            spaces.append(space)
        return spaces

    def update(self, id, space):
        # Updates and existing space
        self._connection.execute("UPDATE spaces SET name=%s, description=%s, price_per_night=%s WHERE id=%s", [space.name, space.description, space.price_per_night, id])
        return None

    def delete(self, id):
        # Deletes a specified space from the database.
        self._connection.execute("DELETE FROM spaces WHERE id=%s", [id])
        return None
