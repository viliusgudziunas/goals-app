from project.models import User
from project.service.base_service import save_changes


def add_new_user(api, user_id=None):
    if user_id:
        admin = User.query.with_entities(User.admin).filter_by(id=user_id).first()[0]
        if not admin:
            api.abort(401, "Insufficient permissions", status="fail")

    email = api.payload["email"]
    password = api.payload["password"]

    user = User.query.filter_by(email=email).first()
    if user:
        api.abort(409, "User already exists", status="fail")

    new_user = User(email=email, password=password)
    save_changes(new_user)

    auth_token = new_user.encode_auth_token(new_user.id).decode()
    return {"status": "success", "data": new_user, "auth_token": auth_token}, 201


def get_all_users():
    return {"status": "success", "data": User.query.all()}


def get_single_user(api, id):
    user = User.query.filter_by(id=id).first()
    if not user:
        api.abort(404, "User does not exist", status="fail")

    return {"status": "success", "data": user}
