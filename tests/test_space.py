from lib.space import Space

def test_creates_space():
    # Given space data
    # It creates a valid Space object
    space = Space(1, "Test Space", "Test Description", 10.0)
    assert space.id == 1
    assert space.name == "Test Space"
    assert space.description == "Test Description"
    assert space.price_per_night == 10.0

def test_compares_to_similar_object():
    # Given two space objects
    # It compares their contents
    space_1 = Space(1, "Test Space", "Test Description", 10.0)
    space_2 = Space(1, "Test Space", "Test Description", 10.0)
    assert space_1 == space_2

def test_outputs_string_when_called():
    # Given a Space object
    # It returns a string when called
    space = Space(1, "Test Space", "Test Description", 10.0)
    assert str(space) == "Space(1, Test Space, Test Description, 10.0)"