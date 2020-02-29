from flask import Blueprint
from flask_restx import Api

from project.api.users import api as users_ns

blueprint = Blueprint("api", __name__)

api = Api(
    blueprint,
    title="GOALS APP USERS API",
    version="1.0",
    description="users resources for goals app",
    doc="/users/doc/",
)

api.add_namespace(users_ns, path="/users")
