from flask import Blueprint
from flask_restplus import Api, Resource, fields

from project import db
from project.api.models import User

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
        return {"status": "success", "data": User.query.all()}, 200

    @api.expect(post_users, validate=True)
    @api.marshal_with(user_response)
    def post(self):
        data = api.payload
        email = data.get("email")
        password = data.get("password")
        user = User.query.filter_by(email=email).first()
        if user:
            message = f"Email '{email}' already exists"
            api.abort(400, message, status="fail")

        user = User(email=email, password=password)
        db.session.add(user)
        db.session.commit()
        return {"status": "success", "data": user}, 201


@api.route("/users/<int:user_id>")
class Users(Resource):
    @api.marshal_with(user_response)
    def get(self, user_id):
        user = User.query.filter_by(id=user_id).first()
        if not user:
            message = f"User id '{user_id}' does not exist"
            api.abort(404, message, status="fail")

        return {"status": "success", "data": user}, 200
