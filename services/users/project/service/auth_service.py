from project import bcrypt
from project.models import BlacklistToken, User
from project.service.base_service import save_changes


def login_user(api):
    email = api.payload["email"]
    password = api.payload["password"]

    user = User.query.filter_by(email=email).first()
    if not user or not bcrypt.check_password_hash(user.password, password):
        api.abort(404, "Incorrect credentials", status="fail")

    auth_token = user.encode_auth_token(user.id).decode()
    return {"status": "success", "data": user, "auth_token": auth_token}


def logout_user(auth_token):
    blacklist_token = BlacklistToken(token=auth_token)
    save_changes(blacklist_token)
    return {"status": "success", "message": "User successfully logged out"}


def user_status(resp):
    return {"status": "success", "data": User.query.filter_by(id=resp).first()}
