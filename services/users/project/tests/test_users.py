import json

import pytest


def test_users_ping(test_app):
    """Ensure /users/ping route behaves correctly"""
    client = test_app.test_client()
    resp = client.get("/users/ping")

    data = resp.json
    assert resp.status_code == 200
    assert data["message"] == "pong!"


def test_add_user(test_app, test_db, post_users):
    """Ensure /users route adds a user correctly"""
    client = test_app.test_client()
    resp = post_users(client)

    data = resp.json
    assert resp.status_code == 201
    assert data["message"] == "test@test.com was successfully added!"


def test_add_user_no_json(test_app, test_db):
    """Ensure /users route responds propertly when no data is sent"""
    client = test_app.test_client()
    resp = client.post("/users", content_type="application/json")

    data = resp.json
    assert resp.status_code == 400
    msg = "The browser (or proxy) sent a request that this server could not understand."
    assert data["message"] == msg


def test_add_user_empty_json(test_app, test_db):
    """Ensure /users route responds propertly when empty json is sent"""
    client = test_app.test_client()
    resp = client.post("/users", data=json.dumps({}), content_type="application/json")

    data = resp.json
    assert resp.status_code == 400
    assert data["errors"]["email"] == "'email' is a required property"
    assert data["message"] == "Input payload validation failed"


@pytest.mark.parametrize(
    "email, password, field, value",
    [
        ["", "test", "email", "''"],
        ["test@test.com", "", "password", "''"],
        ["test@test.com", "123", "password", "'123'"],
    ],
)
def test_add_user_missing_payload(
    test_app, test_db, post_users, email, password, field, value
):
    """Ensure /users route responds properly when empty email is sent"""
    client = test_app.test_client()
    resp = post_users(client, email=email, password=password)

    data = resp.json
    assert resp.status_code == 400
    assert data["errors"][field] == f"{value} is too short"
    assert data["message"] == "Input payload validation failed"


def test_add_user_duplicate_email(test_app, test_db, add_user, post_users):
    """Ensure /users route responds propertly when duplicate email is sent"""
    client = test_app.test_client()
    add_user()
    resp = post_users(client)

    data = resp.json
    assert resp.status_code == 400
    assert data["status"] == "fail"
    assert "Email test@test.com already exists" in data["message"]


def test_single_user(test_app, test_db, add_user):
    """Ensure /users/<int:user_id> route gets a user correctly"""
    client = test_app.test_client()
    user = add_user()
    resp = client.get(f"/users/{user.id}")

    data = resp.json
    assert resp.status_code == 200
    assert len(data.keys()) == 3
    assert data["id"]
    assert data["email"] == "test@test.com"
    assert data["created_date"]


def test_single_user_id_not_integer(test_app, test_db):
    """Ensure /users/<int:user_id> route responds properly
    when a non integer value is passed in for user_id"""
    client = test_app.test_client()
    resp = client.get("/users/test")

    assert resp.status_code == 404


def test_single_user_incorrect_id(test_app, test_db):
    """Ensure /users/<int:user_id> route responds properly
    when incorrect user_id is passed in"""
    client = test_app.test_client()
    resp = client.get("/users/0")

    data = resp.json
    assert resp.status_code == 404
    assert data["status"] == "fail"
    assert "User 0 does not exist" in data["message"]


def test_all_users(test_app, test_db, add_user):
    """Ensure /users route returns all users"""
    client = test_app.test_client()
    add_user()
    add_user("test2@test.com")
    resp = client.get("/users")

    data = resp.json
    assert resp.status_code == 200
    assert data["status"] == "success"
    assert len(data["data"]) == 2
    for user in data["data"]:
        assert len(user.keys()) == 3
        assert user["id"]
        assert user["email"]
        assert user["created_date"]
    assert data["data"][0]["email"] == "test@test.com"
    assert data["data"][1]["email"] == "test2@test.com"
