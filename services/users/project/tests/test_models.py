import pytest
from sqlalchemy.exc import IntegrityError

from project.api.models import User


def test_add_user(test_app, test_db, add_user):
    user = add_user()

    assert user.id
    assert user.email == "test@test.com"
    assert user.password
    assert user.active
    assert user.created_date


def test_add_duplicate_email(test_app, test_db, add_user):
    add_user()
    with pytest.raises(IntegrityError):
        add_user()


def test_passwords_are_random(test_app, test_db, add_user):
    user_one = add_user()
    user_two = add_user("test2@test.com")
    assert user_one.password != user_two.password


def test_encode_auth_token(test_app, test_db, add_user):
    user = add_user()
    token = user.encode_auth_token(user.id)
    assert isinstance(token, bytes)


def test_decode_auth_token(test_app, test_db, add_user):
    user = add_user()
    token = user.encode_auth_token(user.id)
    user_id = User.decode_auth_token(token)
    assert user.id == user_id
