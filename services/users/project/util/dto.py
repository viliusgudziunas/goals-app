from flask_restx import Namespace, fields


class UsersDto:
    api = Namespace("users", description="users related operations")
    user = api.model(
        "User",
        {
            "id": fields.Integer(description="user identifier"),
            "email": fields.String(
                required=True, min_length=6, description="user email address"
            ),
            "created_date": fields.DateTime(description="user created date"),
        },
    )
    response = api.model("Response", {"status": fields.String})
    user_response = api.inherit("UserResponse", response, {"data": fields.Nested(user)})
    users_response = api.inherit(
        "UsersResponse", response, {"data": fields.List(fields.Nested(user))}
    )
    users_payload = api.inherit(
        "UsersPayload", user, {"password": fields.String(required=True, min_length=4)},
    )
