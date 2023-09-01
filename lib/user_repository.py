from lib.user import User

class UserRepository:
    # CRUD methods for user class 
    def __init__(self, connection):
        # Stores connection object 
        self._connection = connection

    def add(self, user):
        # Adds user to the database 
        self._connection.execute("INSERT INTO users(name, password) VALUES (%s, %s)",[user.name, user.password])
        return None 

    def all(self): 
        # Gets all users from the database 
        rows = self._connection.execute("SELECT * FROM users")
        users = []
        for row in rows: 
            user = User(row['id'], row['name'], row['password'])
            users.append(user)
        return users

    def update(self, user):
        # Updates and existing user
        self._connection.execute("UPDATE users SET name=%s, password=%s WHERE id=%s", [user.name, user.password, user.id])
        return None

    def delete(self, id):
        # Deletes a specified user from the database.
        self._connection.execute("DELETE FROM users WHERE id=%s", [id])
        return None
    
    def find_by_name(self,name):
        rows = self._connection.execute("SELECT * FROM users WHERE name=%s", [name])
        row = rows[0]
        return User(row["id"], row["name"], row['password'])

    def find_by_id(self,id):
        rows = self._connection.execute("SELECT * FROM users WHERE id=%s", [id])
        row = rows[0]
        return User(row["id"], row["name"], row['password'])
