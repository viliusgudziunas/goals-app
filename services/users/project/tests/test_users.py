import pytest

from project import db


def test_users_ping(test_app):
    client = test_app.test_client()
    resp = client.get("/users/ping")
    data = resp.json

    assert resp.status_code == 200
    assert data["status"] == "success"
    assert data["message"] == "pong!"


def test_add_user(test_app, test_db, logged_in_user, post_user):
    client = test_app.test_client()
    _, auth_token = logged_in_user(client)
    resp = post_user(
        client,
        credentials={"email": "test1@test.com", "password": "test"},
        token=auth_token,
    )
    data = resp.json

    assert resp.status_code == 201
    assert data["status"] == "success"
    assert len(data["data"].keys()) == 3
    assert data["data"]["id"]
    assert data["data"]["email"] == "test1@test.com"
    assert data["data"]["created_date"]


def test_add_user_no_json(test_app, test_db):
    client = test_app.test_client()
    resp = client.post("/users/", content_type="application/json")
    data = resp.json

    assert resp.status_code == 400
    msg = "The browser (or proxy) sent a request that this server could not understand."
    assert data["message"] == msg


def test_add_user_empty_json(test_app, test_db, post_user):
    client = test_app.test_client()
    resp = post_user(client, {})
    data = resp.json

    assert resp.status_code == 400
    assert len(data["errors"]) == 2
    assert data["errors"]["email"] == "'email' is a required property"
    assert data["errors"]["password"] == "'password' is a required property"
    assert data["message"] == "Input payload validation failed"


@pytest.mark.parametrize(
    "field, value, property",
    [["password", "test", "email"], ["email", "test@test.com", "password"]],
)
def test_add_user_missing_payload(test_app, test_db, post_user, field, value, property):
    client = test_app.test_client()
    resp = post_user(client, {field: value})
    data = resp.json

    assert resp.status_code == 400
    assert len(data["errors"]) == 1
    assert data["errors"][property] == f"'{property}' is a required property"
    assert data["message"] == "Input payload validation failed"


@pytest.mark.parametrize(
    "email, password, field, value",
    [["t@.st", "test", "email", "t@.st"], ["test@test.com", "tes", "password", "tes"]],
)
def test_add_user_value_too_short(
    test_app, test_db, post_user, email, password, field, value
):
    client = test_app.test_client()
    resp = post_user(client, {"email": email, "password": password})
    data = resp.json

    assert resp.status_code == 400
    assert len(data["errors"]) == 1
    assert data["errors"][field] == f"'{value}' is too short"
    assert data["message"] == "Input payload validation failed"


def test_add_user_duplicate_email(test_app, test_db, logged_in_user, post_user):
    client = test_app.test_client()
    _, auth_token = logged_in_user(client)
    resp = post_user(client, token=auth_token)
    data = resp.json

    assert resp.status_code == 409
    assert data["status"] == "fail"
    assert data["message"] == "User already exists"


def test_add_user_inactive(test_app, test_db, logged_in_user, post_user):
    client = test_app.test_client()
    user, auth_token = logged_in_user(client)
    user.active = False
    db.session.commit()
    resp = post_user(client, token=auth_token)
    data = resp.json

    assert resp.status_code == 401
    assert data["status"] == "fail"
    assert data["message"] == "Invalid token"


def test_single_user(test_app, test_db, add_user):
    client = test_app.test_client()
    user = add_user()
    resp = client.get(f"/users/{user.id}")
    data = resp.json

    assert resp.status_code == 200
    assert data["status"] == "success"
    assert len(data["data"].keys()) == 3
    assert data["data"]["id"]
    assert data["data"]["email"] == "test@test.com"
    assert data["data"]["created_date"]


def test_single_user_id_not_integer(test_app, test_db):
    client = test_app.test_client()
    resp = client.get("/users/test")

    assert resp.status_code == 404


def test_single_user_incorrect_id(test_app, test_db):
    client = test_app.test_client()
    resp = client.get("/users/0")
    data = resp.json

    assert resp.status_code == 404
    assert data["status"] == "fail"
    assert data["message"] == "User does not exist"


def test_all_users(test_app, test_db, add_user):
    client = test_app.test_client()
    add_user()
    add_user("test2@test.com")
    resp = client.get("/users/")
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
