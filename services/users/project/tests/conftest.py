import json

import pytest

from project import create_app, db
from project.models import User


@pytest.fixture(scope="module")
def test_app():
    app = create_app()
    app.config.from_object("project.config.TestingConfig")
    with app.app_context():
        yield app


@pytest.fixture(scope="function")
def test_db():
    db.create_all()
    yield db
    db.session.remove()
    db.drop_all()


@pytest.fixture(scope="function")
def add_user():
    def _add_user(email="test@test.com", password="test"):
        user = User(email=email, password=password)
        db.session.add(user)
        db.session.commit()
        return user

    return _add_user


@pytest.fixture(scope="function")
def post_users():
    def _post_users(client, email="test@test.com", password="test"):
        resp = client.post(
            "/users/",
            data=json.dumps({"email": email, "password": password}),
            content_type="application/json",
        )
        return resp

    return _post_users
