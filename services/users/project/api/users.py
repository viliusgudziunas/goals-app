from flask import Blueprint
from flask_restplus import Api, Resource, fields, marshal

from project import db
from project.api.models import User

users_blueprint = Blueprint("users", __name__)
api = Api(users_blueprint)


@api.route("/users/ping")
class UsersPing(Resource):
    def get(self):
        return {"status": "success", "message": "pong!"}, 200


response = api.model("Response", {"status": fields.String})

user_model = api.model("User", {"id": fields.Integer,
                                "email": fields.String,
                                "created_date": fields.DateTime, })

users_list = api.inherit("UsersList", response, {
    "data": fields.List(fields.Nested(user_model))
})

post_users_list = api.model("PostUsersList", {
    "email": fields.String(required=True, min_length=6),
    "password": fields.String(required=True, min_length=4)
})

users_success = api.inherit("UsersSuccess", response, {
    "data": fields.Nested(user_model)
})


@api.route("/users")
class UsersList(Resource):
    @api.marshal_with(users_list)
    def get(self):
        return {"status": "success", "data": User.query.all()}, 200

    @api.expect(post_users_list, validate=True)
    @api.marshal_with(users_success)
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
    @api.marshal_with(users_success)
    def get(self, user_id):
        user = User.query.filter_by(id=user_id).first()
        if not user:
            message = f"User id '{user_id}' does not exist"
            api.abort(404, message, status="fail")

        return {"status": "success", "data": user}, 200
