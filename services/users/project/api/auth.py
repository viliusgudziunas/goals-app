from flask_restx import Resource

from project.service.auth_service import login_user, logout_user, user_status
from project.service.users_service import add_new_user
from project.util.dto import AuthDto

api = AuthDto.api
_users_payload = AuthDto.users_payload
_auth_response = AuthDto.auth_response
_logout_response = AuthDto.logout_response
_user_status_response = AuthDto.user_status_response


@api.route("/register")
class Register(Resource):
    @api.doc("register a new user")
    @api.expect(_users_payload, validate=True)
    @api.marshal_with(_auth_response)
    def post(self):
        """Register a new user"""
        return add_new_user(api)


@api.route("/login")
class Login(Resource):
    @api.doc("login a user")
    @api.expect(_users_payload, validate=True)
    @api.marshal_with(_auth_response)
    def post(self):
        """Login a user"""
        return login_user(api)


@api.route("/logout")
class Logout(Resource):
    @api.doc("logout a user")
    @api.marshal_with(_logout_response)
    def get(self):
        """Logout a user"""
        return logout_user()


@api.route("/status")
class UserStatus(Resource):
    @api.doc("get user status")
    @api.marshal_with(_user_status_response)
    def get(self):
        """Get user status"""
        return user_status(api)
