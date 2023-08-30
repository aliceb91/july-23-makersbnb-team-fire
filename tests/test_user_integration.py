from lib.user import User
from lib.user_repository import UserRepository

def test_returns_all_users(db_connection):
    db_connection.seed("seeds/user.sql")
    repository = UserRepository(db_connection)
    users = repository.all()
    assert users ==[
        User(1, "name 1"),
        User(2, "name 2")
    ]