import pytest

from project import db


def test_register_user(test_app, test_db, register):
    client = test_app.test_client()
    resp = register(client)
    data = resp.json

    assert resp.status_code == 201
    assert data["status"] == "success"
    assert len(data["data"].keys()) == 4
    assert data["data"]["id"]
    assert data["data"]["email"] == "test@test.com"
    assert data["data"]["created_date"]
    assert data["data"]["admin"] is False
    assert data["auth_token"]


def test_register_user_no_json(test_app, test_db):
    client = test_app.test_client()
    resp = client.post("/auth/register", content_type="application/json")
    data = resp.json

    assert resp.status_code == 400
    msg = "The browser (or proxy) sent a request that this server could not understand."
    assert data["message"] == msg


def test_register_user_empty_json(test_app, test_db, register):
    client = test_app.test_client()
    resp = register(client, {})
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
def test_register_user_missing_payload(
    test_app, test_db, register, field, value, property
):
    client = test_app.test_client()
    resp = register(client, {field: value})
    data = resp.json

    assert resp.status_code == 400
    assert len(data["errors"]) == 1
    assert data["errors"][property] == f"'{property}' is a required property"
    assert data["message"] == "Input payload validation failed"


@pytest.mark.parametrize(
    "email, password, field, value",
    [["t@.st", "test", "email", "t@.st"], ["test@test.com", "tes", "password", "tes"]],
)
def test_register_user_value_too_short(
    test_app, test_db, register, email, password, field, value
):
    client = test_app.test_client()
    resp = register(client, {"email": email, "password": password})
    data = resp.json

    assert resp.status_code == 400
    assert len(data["errors"]) == 1
    assert data["errors"][field] == f"'{value}' is too short"
    assert data["message"] == "Input payload validation failed"


def test_register_user_duplicate_email(test_app, test_db, add_user, register):
    client = test_app.test_client()
    add_user()
    resp = register(client)
    data = resp.json

    assert resp.status_code == 409
    assert data["status"] == "fail"
    assert data["message"] == "User already exists"


def test_registered_user_login(test_app, test_db, add_user, login):
    client = test_app.test_client()
    add_user()
    resp = login(client)
    data = resp.json

    assert resp.status_code == 200
    assert data["status"] == "success"
    assert len(data["data"].keys()) == 4
    assert data["data"]["id"]
    assert data["data"]["email"] == "test@test.com"
    assert data["data"]["created_date"]
    assert data["data"]["admin"] is False
    assert data["auth_token"]


def test_not_registered_user_login(test_app, test_db, login):
    client = test_app.test_client()
    resp = login(client)
    data = resp.json

    assert resp.status_code == 404
    assert data["status"] == "fail"
    assert data["message"] == "Incorrect credentials"


@pytest.mark.parametrize(
    "email, password", [["test1@test.com", "test"], ["test@test.com", "test1"]]
)
def test_login_with_wrong_credentials(
    test_app, test_db, add_user, login, email, password
):
    client = test_app.test_client()
    add_user()
    resp = login(client, {"email": email, "password": password})
    data = resp.json

    assert resp.status_code == 404
    assert data["status"] == "fail"
    assert data["message"] == "Incorrect credentials"


@pytest.mark.parametrize(
    "field, value, property",
    [["password", "test", "email"], ["email", "test@test.com", "password"]],
)
def test_login_with_missing_credentials(
    test_app, test_db, add_user, login, field, value, property
):
    client = test_app.test_client()
    add_user()
    resp = login(client, {field: value})
    data = resp.json

    assert resp.status_code == 400
    assert len(data["errors"]) == 1
    assert data["errors"][property] == f"'{property}' is a required property"
    assert data["message"] == "Input payload validation failed"


def test_valid_logout(test_app, test_db, logged_in_user, logout):
    client = test_app.test_client()
    _, auth_token = logged_in_user(client)
    resp = logout(client, auth_token)
    data = resp.json

    assert resp.status_code == 200
    assert data["status"] == "success"
    assert data["message"] == "User successfully logged out"


def test_invalid_logout_no_user(test_app, test_db, logout):
    client = test_app.test_client()
    resp = logout(client, "test")
    data = resp.json

    assert resp.status_code == 401
    assert data["status"] == "fail"
    assert data["message"] == "Invalid token"


def test_invalid_logout_user_not_logged_in(test_app, test_db, add_user, logout):
    client = test_app.test_client()
    add_user()
    resp = logout(client, "test")
    data = resp.json

    assert resp.status_code == 401
    assert data["status"] == "fail"
    assert data["message"] == "Invalid token"


def test_invalid_logout_invalid_token(test_app, test_db, logged_in_user, logout):
    client = test_app.test_client()
    logged_in_user(client)
    resp = logout(client, "test")
    data = resp.json

    assert resp.status_code == 401
    assert data["status"] == "fail"
    assert data["message"] == "Invalid token"


def test_invalid_logout_expired_token(test_app, test_db, logged_in_user, logout):
    test_app.config["TOKEN_EXPIRATION_SECONDS"] = -1
    client = test_app.test_client()
    _, auth_token = logged_in_user(client)
    resp = logout(client, auth_token)
    data = resp.json

    assert resp.status_code == 401
    assert data["status"] == "fail"
    assert data["message"] == "Signature expired"


def test_invalid_logout_already_logged_out(test_app, test_db, logged_in_user, logout):
    client = test_app.test_client()
    _, auth_token = logged_in_user(client)
    logout(client, auth_token)
    resp = logout(client, auth_token)
    data = resp.json

    assert resp.status_code == 401
    assert data["status"] == "fail"
    assert data["message"] == "Token blacklisted"


def test_invalid_logout_no_header(test_app, test_db, logged_in_user):
    client = test_app.test_client()
    logged_in_user(client)
    resp = client.get("/auth/logout")
    data = resp.json

    assert resp.status_code == 401
    assert data["status"] == "fail"
    assert data["message"] == "No auth token provided"


def test_invalid_logout_header_without_bearer(test_app, test_db, logged_in_user):
    client = test_app.test_client()
    _, auth_token = logged_in_user(client)
    resp = client.get("/auth/logout", headers={"Authorization": auth_token})
    data = resp.json

    assert resp.status_code == 401
    assert data["status"] == "fail"
    assert data["message"] == "Invalid token"


def test_invalid_logout_inactive(test_app, test_db, logged_in_user, logout):
    client = test_app.test_client()
    user, auth_token = logged_in_user(client)
    user.active = False
    db.session.commit()
    resp = logout(client, auth_token)
    data = resp.json

    assert resp.status_code == 401
    assert data["status"] == "fail"
    assert data["message"] == "Invalid token"


def test_user_status(test_app, test_db, logged_in_user, check_status):
    client = test_app.test_client()
    _, auth_token = logged_in_user(client)
    resp = check_status(client, auth_token)
    data = resp.json

    assert resp.status_code == 200
    assert data["status"] == "success"
    assert len(data["data"].keys()) == 5
    assert data["data"]["id"]
    assert data["data"]["email"] == "test@test.com"
    assert data["data"]["created_date"]
    assert data["data"]["active"]
    assert data["data"]["admin"] is False


def test_user_status_invalid_token(test_app, test_db, check_status):
    client = test_app.test_client()
    resp = check_status(client, "test")
    data = resp.json

    assert resp.status_code == 401
    assert data["status"] == "fail"
    assert data["message"] == "Invalid token"


def test_user_status_expired_token(test_app, test_db, logged_in_user, check_status):
    test_app.config["TOKEN_EXPIRATION_SECONDS"] = -1
    client = test_app.test_client()
    _, auth_token = logged_in_user(client)
    resp = check_status(client, auth_token)
    data = resp.json

    assert resp.status_code == 401
    assert data["status"] == "fail"
    assert data["message"] == "Signature expired"


def test_user_status_no_header(test_app, test_db, logged_in_user):
    client = test_app.test_client()
    logged_in_user(client)
    resp = client.get("/auth/status")
    data = resp.json

    assert resp.status_code == 401
    assert data["status"] == "fail"
    assert data["message"] == "No auth token provided"


def test_user_status_header_without_bearer(test_app, test_db, logged_in_user):
    client = test_app.test_client()
    _, auth_token = logged_in_user(client)
    resp = client.get("/auth/status", headers={"Authorization": auth_token})
    data = resp.json

    assert resp.status_code == 401
    assert data["status"] == "fail"
    assert data["message"] == "Invalid token"


def test_user_status_inactive(test_app, test_db, logged_in_user, check_status):
    client = test_app.test_client()
    user, auth_token = logged_in_user(client)
    user.active = False
    db.session.commit()
    resp = check_status(client, auth_token)
    data = resp.json

    assert resp.status_code == 401
    assert data["status"] == "fail"
    assert data["message"] == "Invalid token"
