from lib.space_repository import * 
from unittest.mock import Mock 
import datetime

def test_get_all(db_connection): 
    db_connection.seed("seeds/space.sql")
    repository = SpaceRepository(db_connection)
    spaces = repository.all()
    result = []
    for space in spaces:
        result.append(str(space))
    assert result == [
        f"Space(1, test 1, This is test 1, 10.0, {datetime.date(2000, 1, 1)}, {datetime.date(2000, 1, 2)}, 1)", 
        f"Space(2, test 2, This is test 2, 20.0, {datetime.date(2000, 1, 4)}, {datetime.date(2000, 1, 6)}, 2)"
    ]


def test_add_to_database(db_connection): 
    db_connection.seed("seeds/space.sql")
    repository = SpaceRepository(db_connection)
    space = Mock()
    space.name = "test 3"
    space.description = "This is test 3"
    space.price_per_night = 30.0
    space.start_date = datetime.date(2020, 1, 11)
    space.end_date = datetime.date(2020, 1, 31)
    space.user_id = 2
    repository.add(space)
    spaces = repository.all()
    result = []
    for space in spaces:
        result.append(str(space))
    assert result == [
        f"Space(1, test 1, This is test 1, 10.0, {datetime.date(2000, 1, 1)}, {datetime.date(2000, 1, 2)}, 1)", 
        f"Space(2, test 2, This is test 2, 20.0, {datetime.date(2000, 1, 4)}, {datetime.date(2000, 1, 6)}, 2)",
        f"Space(3, test 3, This is test 3, 30.0, {datetime.date(2020, 1, 11)}, {datetime.date(2020, 1, 31)}, 2)"
    ]

def test_update_space(db_connection):
    db_connection.seed("seeds/space.sql")
    repository = SpaceRepository(db_connection)
    updated_space = Mock()
    updated_space.name = "test 4"
    updated_space.description = "This is test 4"
    updated_space.price_per_night = 40.0
    updated_space.user_id = 1
    updated_space.start_date = datetime.date(2000, 1, 4)
    updated_space.end_date = datetime.date(2000, 1, 6)
    repository.update(2, updated_space)
    spaces = repository.all()
    result = []
    for space in spaces:
        result.append(str(space))
    assert result == [
        f"Space(1, test 1, This is test 1, 10.0, {datetime.date(2000, 1, 1)}, {datetime.date(2000, 1, 2)}, 1)", 
        f"Space(2, test 4, This is test 4, 40.0, {datetime.date(2000, 1, 4)}, {datetime.date(2000, 1, 6)}, 1)",
    ]

def test_delete_space(db_connection):
    db_connection.seed("seeds/space.sql")
    repository = SpaceRepository(db_connection)
    repository.delete(1)
    spaces = repository.all()
    result = []
    for space in spaces:
        result.append(str(space))
    assert result == [
        f"Space(2, test 2, This is test 2, 20.0, {datetime.date(2000, 1, 4)}, {datetime.date(2000, 1, 6)}, 2)"
    ]
