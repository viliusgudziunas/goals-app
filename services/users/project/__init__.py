import os
from flask import Flask, jsonify
from flask_restful import Resource, Api

app = Flask(__name__)
app_settings = os.getenv("APP_SETTINGS")
app.config.from_object(app_settings)

api = Api(app)


class UsersPing(Resource):
    def get(self):
        return {
            "status": "success",
            "message": "pong!"
        }


api.add_resource(UsersPing, "/users/ping")
