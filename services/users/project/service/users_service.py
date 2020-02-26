from project import db
from project.models import User


def add_new_user(data):
    response_object = {"status_code": 201}
    email = data["email"]
    password = data["password"]

    user = User.query.filter_by(email=email).first()
    if user:
        response_object["fail"] = True
        response_object["message"] = "User already exists"
        response_object["status_code"] = 409
        return response_object

    new_user = User(email=email, password=password)
    save_changes(new_user)

    response_object["data"] = new_user
    return response_object


def get_all_users():
    return User.query.all()


def get_single_user(id):
    response_object = {"status_code": 200}
    user = User.query.filter_by(id=id).first()
    if not user:
        response_object["fail"] = True
        response_object["message"] = "User does not exist"
        response_object["status_code"] = 404
        return response_object

    response_object["data"] = user
    return response_object


def save_changes(obj):
    db.session.add(obj)
    db.session.commit()
