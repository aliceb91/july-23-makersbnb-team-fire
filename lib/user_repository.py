from lib.user import User

class UserRepository:
    # CRUD methods for user class 
    def __init__(self, connection):
        # Stores connection object 
        self._connection = connection

    def add(self, user):
        # Adds user to the database 
        self._connection.execute("INSERT INTO users(name) VALUES (%s)",[user.name])
        return None 

    def all(self): 
        # Gets all users from the database 
        rows = self._connection.execute("SELECT * FROM users")
        users = []
        for row in rows: 
            user = User(row['id'], row['name'])
            users.append(user)
        return users

    def update(self, user):
        # Updates and existing user
        self._connection.execute("UPDATE users SET name=%s WHERE id=%s", [user.name, user.id])
        return None

    def delete(self, id):
        # Deletes a specified user from the database.
        self._connection.execute("DELETE FROM users WHERE id=%s", [id])
        return None
