from lib.space import Space
from lib.space_repository import SpaceRepository
import datetime

def test_returns_all_spaces(db_connection):
    db_connection.seed("seeds/space.sql")
    repository = SpaceRepository(db_connection)
    spaces = repository.all()
    assert spaces ==[
        Space(1, "test 1", "This is test 1", 10.0, datetime.date(2000, 1, 1), datetime.date(2000, 1, 2), 1),
        Space(2, "test 2", "This is test 2", 20.0, datetime.date(2000, 1, 4), datetime.date(2000, 1, 6), 2)
    ]