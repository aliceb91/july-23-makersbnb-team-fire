from lib.user_repository import * 
from unittest.mock import Mock 

def test_get_all(db_connection): 
    db_connection.seed("seeds/user.sql")
    repository = UserRepository(db_connection)
    users = repository.all()
    result = []
    for user in users:
        result.append(str(user))
    assert result == [
        "User(1, name 1)", 
        "User(2, name 2)"
    ]

def test_update_user(db_connection):
    db_connection.seed("seeds/user.sql")
    repository = UserRepository(db_connection)
    updated_user = Mock()
    updated_user.id = 2
    updated_user.name = "name 4"
    repository.update(updated_user)
    users = repository.all()
    result = []
    for user in users:
        result.append(str(user))
    assert result == [
        "User(1, name 1)", 
        "User(2, name 4)", 
    ]

def test_delete_user(db_connection):
    db_connection.seed("seeds/user.sql")
    repository = UserRepository(db_connection)
    repository.delete(1)
    users = repository.all()
    result = []
    for user in users:
        result.append(str(user))
    assert result == [
        "User(2, name 2)"
    ]

def test_add_user(db_connection):
    db_connection.seed("seeds/user.sql")
    repository = UserRepository(db_connection)
    new_user = Mock()
    new_user.name = "name 3"
    repository.add(new_user)
    users = repository.all()
    result = []
    for user in users:
        result.append(str(user))
    assert result == [
        "User(1, name 1)", 
        "User(2, name 2)",
        "User(3, name 3)" 
    ]

def test_find_user(db_connection):
    db_connection.seed("seeds/user.sql")
    repository = UserRepository(db_connection)
    user = repository.find(2)
    assert str(user) == "User(2, name 2)"
