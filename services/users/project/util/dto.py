from flask_restx import Namespace, fields


class BaseDto:
    api = Namespace("base", description="base data transfer object")
    response = api.model(
        "Response", {"status": fields.String(description="response status")}
    )


class UsersDto:
    api = Namespace("users", description="users related operations")
    user = api.model(
        "User",
        {
            "id": fields.Integer(description="user identifier"),
            "email": fields.String(description="user email address"),
            "active": fields.Boolean(description="indicator of whether user is active"),
            "admin": fields.Boolean(description="indicator of whether user is admin"),
        },
    )
    users_payload = api.inherit(
        "UsersPayload",
        user,
        {
            "email": fields.String(required=True, min_length=6),
            "password": fields.String(
                required=True, min_length=4, description="user password"
            ),
        },
    )
    users_response = api.inherit(
        "UsersResponse",
        BaseDto.response,
        {
            "data": fields.List(
                fields.Nested(user), description="list of users and their details",
            )
        },
    )
    user_response = api.inherit(
        "UserResponse", BaseDto.response, {"data": fields.Nested(user)}
    )


class AuthDto:
    api = Namespace("auth", description="authentication related operations")
    users_payload = UsersDto.users_payload
    auth_response = api.inherit(
        "AuthenticationResponse",
        UsersDto.user_response,
        {"auth_token": fields.String(description="authentication token")},
    )
    logout_response = api.inherit(
        "LogoutResponse",
        BaseDto.response,
        {"message": fields.String(description="success or failure message")},
    )
    user = UsersDto.user
    user_status_response = api.inherit(
        "UserStatusResponse", BaseDto.response, {"data": fields.Nested(user)}
    )
