from flask_restplus import Resource

from project.service.users_service import add_new_user, get_all_users, get_single_user
from project.util.dto import UsersDto

api = UsersDto.api
_users = UsersDto.users_response
_users_payload = UsersDto.users_payload
_user = UsersDto.user_response


@api.route("/ping")
class UsersPing(Resource):
    def get(self):
        """Check that the api resource is healthy"""
        return {"status": "success", "message": "pong!"}, 200


@api.route("/")
class UsersList(Resource):
    @api.doc("get a list of users")
    @api.marshal_with(_users)
    def get(self):
        """List all registered users"""
        return get_all_users()

    @api.doc("create a new user")
    @api.expect(_users_payload, validate=True)
    @api.marshal_with(_user)
    def post(self):
        return add_new_user(api)


@api.route("/<int:user_id>")
class Users(Resource):
    @api.doc("get a user")
    @api.marshal_with(_user)
    def get(self, user_id):
        return get_single_user(api, user_id)
