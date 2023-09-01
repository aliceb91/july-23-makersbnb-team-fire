from lib.user import User

def test_creates_user():
    # Given user data
    # It creates a valid User object
    user = User(1, "Test User", "Test Password")
    assert user.id == 1
    assert user.name == "Test User"
    assert user.password == "Test Password"

def test_compares_to_similar_object():
    # Given two user objects
    # It compares their contents
    user_1 = User(1, "Test User", "Test Password")
    user_2 = User(1, "Test User", "Test Password")
    assert user_1 == user_2

def test_outputs_string_when_called():
    # Given a User object
    # It returns a string when called
    user = User(1, "Test User", "Test Password")
    assert str(user) == "User(1, Test User, Test Password)"