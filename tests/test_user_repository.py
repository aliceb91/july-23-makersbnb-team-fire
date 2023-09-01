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
        "User(1, name 1, password1)", 
        "User(2, name 2, password2)"
    ]

def test_update_user(db_connection):
    db_connection.seed("seeds/user.sql")
    repository = UserRepository(db_connection)
    updated_user = Mock()
    updated_user.id = 2
    updated_user.name = "name 4"
    updated_user.password = "password4"
    repository.update(updated_user)
    users = repository.all()
    result = []
    for user in users:
        result.append(str(user))
    assert result == [
        "User(1, name 1, password1)", 
        "User(2, name 4, password4)", 
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
        "User(2, name 2, password2)"
    ]

def test_add_user(db_connection):
    db_connection.seed("seeds/user.sql")
    repository = UserRepository(db_connection)
    new_user = Mock()
    new_user.name = "name 3"
    new_user.password = "password3"
    repository.add(new_user)
    users = repository.all()
    result = []
    for user in users:
        result.append(str(user))
    assert result == [
        "User(1, name 1, password1)", 
        "User(2, name 2, password2)",
        "User(3, name 3, password3)" 
    ]

def test_find_user_by_name(db_connection):
    db_connection.seed("seeds/user.sql")
    repository = UserRepository(db_connection)
    user = repository.find_by_name("name 2")
    assert str(user) == "User(2, name 2, password2)"

def test_find_user_by_id(db_connection):
    db_connection.seed("seeds/user.sql")
    repository = UserRepository(db_connection)
    user = repository.find_by_id(2)
    assert str(user) == "User(2, name 2, password2)"