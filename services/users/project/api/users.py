from flask import Blueprint
from flask_restplus import Resource, Api, fields
from project import db
from project.api.models import User

users_blueprint = Blueprint("users", __name__)
api = Api(users_blueprint)


@api.route("/users/ping")
class UsersPing(Resource):
    def get(self):
        return {"message": "pong!"}, 200


user = api.model("User", {
    "id": fields.Integer(readOnly=True),
    "email": fields.String(required=True, min_length=6),
    "created_date": fields.DateTime
})


@api.route("/users")
class UsersList(Resource):
    @api.marshal_with(user, as_list=True, envelope="data")
    def get(self):
        return User.query.all(), 200

    @api.expect(user, validate=True)
    def post(self):
        data = api.payload
        email = data.get("email")
        user = User.query.filter_by(email=email).first()
        if user:
            message = f"Email {email} already exists"
            api.abort(400, message, status="fail")

        db.session.add(User(email=email))
        db.session.commit()
        return {"message": f"{email} was successfully added!"}, 201


@api.route("/users/<int:user_id>")
class Users(Resource):
    @api.marshal_with(user)
    def get(self, user_id):
        user = User.query.filter_by(id=user_id).first()
        if not user:
            message = f"User {user_id} does not exist"
            api.abort(404, message, status="fail")

        return user, 200
