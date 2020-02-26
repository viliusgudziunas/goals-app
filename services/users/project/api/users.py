from flask import Blueprint
from flask_restplus import Api, Resource, fields

from project.models import User
from project.service.users_service import add_new_user, get_all_users, get_single_user

users_blueprint = Blueprint("users", __name__)
api = Api(users_blueprint)

user_model = api.model(
    "User",
    {
        "id": fields.Integer,
        "email": fields.String(required=True, min_length=6),
        "created_date": fields.DateTime,
    },
)
response_model = api.model("Response", {"status": fields.String})

post_users = api.inherit(
    "PostUsers", user_model, {"password": fields.String(required=True, min_length=4)},
)

user_response = api.inherit(
    "UserResponse", response_model, {"data": fields.Nested(user_model)}
)
users_response = api.inherit(
    "UsersResponse", response_model, {"data": fields.List(fields.Nested(user_model))}
)


@api.route("/users/ping")
class UsersPing(Resource):
    def get(self):
        return {"status": "success", "message": "pong!"}, 200


@api.route("/users")
class UsersList(Resource):
    @api.marshal_with(users_response)
    def get(self):
        return {"status": "success", "data": get_all_users()}, 200

    @api.expect(post_users, validate=True)
    @api.marshal_with(user_response)
    def post(self):
        response = add_new_user(api.payload)
        if "fail" in response:
            api.abort(response["status_code"], response["message"], status="fail")

        response_object = {"status": "success", "data": response["data"]}
        return response_object, response["status_code"]


@api.route("/users/<int:user_id>")
class Users(Resource):
    @api.marshal_with(user_response)
    def get(self, user_id):
        response = get_single_user(user_id)
        if "fail" in response:
            api.abort(response["status_code"], response["message"], status="fail")

        response_object = {"status": "success", "data": response["data"]}
        return response_object, response["status_code"]
