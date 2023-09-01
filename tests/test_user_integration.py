from lib.user import User
from lib.user_repository import UserRepository

def test_returns_all_users(db_connection):
    db_connection.seed("seeds/user.sql")
    repository = UserRepository(db_connection)
    users = repository.all()
    assert users ==[
        User(1, "name 1", "password1"),
        User(2, "name 2", "password2")
    ]


def test_update_user(db_connection):
    db_connection.seed("seeds/user.sql")
    repository = UserRepository(db_connection)
    updated_user = User(2, "name 4", "password4")
    repository.update(updated_user)
    users = repository.all()
    assert users == [
        User(1, "name 1", "password1"), 
        User(2, "name 4", "password4") 
    ]

def test_delete_user(db_connection):
    db_connection.seed("seeds/user.sql")
    repository = UserRepository(db_connection)
    repository.delete(1)
    users = repository.all()
    assert users == [
        User(2, "name 2", "password2")
    ]

def test_add_user(db_connection):
    db_connection.seed("seeds/user.sql")
    repository = UserRepository(db_connection)
    new_user = User(None, "name 3", "password3")
    repository.add(new_user)
    users = repository.all()
    assert users == [
        User(1, "name 1", "password1"), 
        User(2, "name 2", "password2"),
        User(3, "name 3", "password3") 
    ]

def test_find_user(db_connection):
    db_connection.seed("seeds/user.sql")
    repository = UserRepository(db_connection)
    user = repository.find_by_name("name 2")
    assert user == User(2, "name 2", "password2")

def test_find_id(db_connection):
    db_connection.seed("seeds/user.sql")
    repository = UserRepository(db_connection)
    user = repository.find_by_id(2)
    assert user == User(2, "name 2", "password2")
