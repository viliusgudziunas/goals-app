from flask import Blueprint
from flask_restx import Api

from project.api.auth import api as auth_ns
from project.api.users import api as users_ns
from project.util.dto import BaseDto

blueprint = Blueprint("api", __name__)

api = Api(
    blueprint,
    title="GOALS APP USERS API",
    version="1.0",
    description="users resources for goals app",
    doc="/users/doc/",
)

api.add_namespace(BaseDto.api)
api.add_namespace(users_ns)
api.add_namespace(auth_ns)
