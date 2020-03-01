from flask import request

from project import bcrypt
from project.models import BlacklistToken, User
from project.service.base_service import save_changes


def login_user(api):
    email = api.payload["email"]
    password = api.payload["password"]

    user = User.query.filter_by(email=email).first()
    if not user or not bcrypt.check_password_hash(user.password, password):
        api.abort(404, "Incorrect credentials", status="fail")

    auth_token = user.encode_auth_token(user.id)

    return {"status": "success", "data": user, "auth_token": auth_token.decode()}


def logout_user():
    auth_header = request.headers.get("Authorization")
    if not auth_header:
        return {"status": "fail", "message": "No auth token provided"}, 401

    try:
        auth_token = auth_header.split(" ")[1]
    except IndexError:
        return {"status": "fail", "message": "Invalid token"}, 401

    resp = User.decode_auth_token(auth_token)
    if isinstance(resp, str):
        return {"status": "fail", "message": resp}, 401

    blacklist_token = BlacklistToken(token=auth_token)
    save_changes(blacklist_token)
    return {"status": "success", "message": "User successfully logged out"}


def user_status(api):
    auth_header = request.headers.get("Authorization")
    if not auth_header:
        api.abort(401, "No auth token provided", status="fail")

    try:
        auth_token = auth_header.split(" ")[1]
    except IndexError:
        api.abort(401, "Invalid token", status="fail")

    resp = User.decode_auth_token(auth_token)
    if isinstance(resp, str):
        api.abort(401, resp, status="fail")

    return {"status": "success", "data": User.query.filter_by(id=resp).first()}
