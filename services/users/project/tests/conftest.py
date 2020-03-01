import json

import pytest

from project import create_app, db
from project.models import User


@pytest.fixture(scope="function")
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


credentials = {"email": "test@test.com", "password": "test"}


def post_request(client, url, payload):
    resp = client.post(url, data=json.dumps(payload), content_type="application/json")
    return resp


@pytest.fixture(scope="function")
def post_user():
    def _post_user(client, credentials=credentials):
        return post_request(client, "/users/", credentials)

    return _post_user


@pytest.fixture(scope="function")
def register():
    def _register(client, credentials=credentials):
        return post_request(client, "/auth/register", credentials)

    return _register


@pytest.fixture(scope="function")
def login():
    def _login(client, credentials=credentials):
        return post_request(client, "/auth/login", credentials)

    return _login


@pytest.fixture(scope="function")
def logout():
    def _logout(client, token):
        return client.get("/auth/logout", headers={"Authorization": f"Bearer {token}"})

    return _logout


@pytest.fixture(scope="function")
def check_status():
    def _check_status(client, token):
        return client.get("/auth/status", headers={"Authorization": f"Bearer {token}"})

    return _check_status
