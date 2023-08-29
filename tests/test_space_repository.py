from lib.space_repository import * 
from unittest.mock import Mock 

def test_get_all(db_connection): 
    db_connection.seed("seeds/space.sql")
    repository = SpaceRepository(db_connection)
    spaces = repository.all()
    assert spaces == [
        "1, test 1, This is test 1, 10.0", 
        "2, test 2, This is test 2, 20.0"
    ]


def test_add_to_database(db_connection): 
    db_connection.seed("seeds/space.sql")
    repository = SpaceRepository(db_connection)
    space = Mock()
    space.name = "test 3"
    space.description = "This is test 3"
    space.price_per_night = 30.0
    repository.add(space)
    spaces = repository.all()
    assert spaces == [
        "1, test 1, This is test 1, 10.0", 
        "2, test 2, This is test 2, 20.0", 
        "3, test 3, This is test 3, 30.0"
    ]
