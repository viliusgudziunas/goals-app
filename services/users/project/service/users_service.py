from project import db
from project.models import User


def add_new_user(api):
    email = api.payload["email"]
    password = api.payload["password"]

    user = User.query.filter_by(email=email).first()
    if user:
        api.abort(409, "User already exists", status="fail")

    new_user = User(email=email, password=password)
    save_changes(new_user)

    response_object = {"status": "success", "data": new_user}
    return response_object, 201


def get_all_users():
    response_object = {"status": "success", "data": User.query.all()}
    return response_object


def get_single_user(api, id):
    user = User.query.filter_by(id=id).first()
    if not user:
        api.abort(404, "User does not exist", status="fail")

    response_object = {"status": "success", "data": user}
    return response_object


def save_changes(obj):
    db.session.add(obj)
    db.session.commit()
