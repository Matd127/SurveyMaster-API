from models.user import User 
import pytest
from pydantic import ValidationError
from bson import ObjectId

def test_valid_user():
    user = User(
        username="valid_user",
        email="valid@example.com",
        password="Password1!"
    )
    assert user.username == "valid_user"
    assert user.email == "valid@example.com"
    assert user.password == "Password1!"
    assert isinstance(user.id, ObjectId)

def test_username_too_short():
    with pytest.raises(ValidationError) as exc_info:
        User(username="ab", email="valid@example.com", password="Password1!")
    assert 'String should have at least 3 characters' in str(exc_info.value)

def test_username_not_alphanumeric():
    with pytest.raises(ValidationError) as exc_info:
        User(username="invalid_user!", email="valid@example.com", password="Password1!")
    assert 'must contain only letters, numbers, and underscores' in str(exc_info.value)

def test_password_too_short():
    with pytest.raises(ValidationError) as exc_info:
        User(username="valid_user", email="valid@example.com", password="Short1!")
    assert 'String should have at least 8 characters' in str(exc_info.value)

def test_password_missing_lowercase():
    with pytest.raises(ValidationError) as exc_info:
        User(username="valid_user", email="valid@example.com", password="PASSWORD1!")
    assert 'Password must be at least 8 characters long' in str(exc_info.value)

def test_password_missing_uppercase():
    with pytest.raises(ValidationError) as exc_info:
        User(username="valid_user", email="valid@example.com", password="password1!")
    assert 'Password must be at least 8 characters long' in str(exc_info.value)

def test_password_missing_digit():
    with pytest.raises(ValidationError) as exc_info:
        User(username="valid_user", email="valid@example.com", password="Password!")
    assert 'Password must be at least 8 characters long' in str(exc_info.value)

def test_password_missing_special_char():
    with pytest.raises(ValidationError) as exc_info:
        User(username="valid_user", email="valid@example.com", password="Password1")
    assert 'Password must be at least 8 characters long' in str(exc_info.value)

def test_password_complexity():
    with pytest.raises(ValidationError) as exc_info:
        User(username="valid_user", email="valid@example.com", password="password")
    assert 'Password must be at least 8 characters long' in str(exc_info.value)

def test_invalid_email():
    with pytest.raises(ValidationError) as exc_info:
        User(username="valid_user", email="invalid_email", password="Password1!")
    assert 'value is not a valid email address' in str(exc_info.value)

if __name__ == '__main__':
    pytest.main()
