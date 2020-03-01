from project.models import User
from project.service.base_service import save_changes


def add_new_user(api):
    email = api.payload["email"]
    password = api.payload["password"]

    user = User.query.filter_by(email=email).first()
    if user:
        api.abort(409, "User already exists", status="fail")

    new_user = User(email=email, password=password)
    save_changes(new_user)

    auth_token = new_user.encode_auth_token(new_user.id)
    return {"status": "success", "data": new_user, "auth_token": auth_token}, 201


def get_all_users():
    return {"status": "success", "data": User.query.all()}


def get_single_user(api, id):
    user = User.query.filter_by(id=id).first()
    if not user:
        api.abort(404, "User does not exist", status="fail")

    return {"status": "success", "data": user}
