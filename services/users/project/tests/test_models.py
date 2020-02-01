import pytest
from sqlalchemy.exc import IntegrityError


def test_add_user(test_app, test_db, add_user):
    user = add_user()

    assert user.id
    assert user.email == "test@test.com"
    assert user.active
    assert user.created_date


def test_add_duplicate_email(test_app, test_db, add_user):
    add_user()
    with pytest.raises(IntegrityError):
        add_user()
