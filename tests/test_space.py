from lib.space import Space
import datetime

def test_creates_space():
    # Given space data
    # It creates a valid Space object
    space = Space(1, "Test Space", "Test Description", 10.0, 1)
    assert space.id == 1
    assert space.name == "Test Space"
    assert space.description == "Test Description"
    assert space.price_per_night == 10.0
    assert space.user_id == 1

def test_compares_to_similar_object():
    # Given two space objects
    # It compares their contents
    space_1 = Space(1, "Test Space", "Test Description", 10.0, 1)
    space_2 = Space(1, "Test Space", "Test Description", 10.0, 1)
    assert space_1 == space_2

def test_outputs_string_when_called():
    # Given a Space object
    # It returns a string when called
    space = Space(1, "Test Space", "Test Description", 10.0, 1)
    assert str(space) == "Space(1, Test Space, Test Description, 10.0, 1)"

def test_create_date_range():
    # Given a Space object
    # It creates a range of dates between a given start and end date.
    space = Space(1, "Test Space", "Test Description", 10.0, 1)
    start_date = datetime.date(2000,1,1)
    end_date = datetime.date(2000,1,4)
    space.dates_generator(start_date, end_date)
    assert space.available_dates == [
        datetime.date(2000, 1, 1),
        datetime.date(2000, 1, 2),
        datetime.date(2000, 1, 3),
        datetime.date(2000, 1, 4)
    ]
