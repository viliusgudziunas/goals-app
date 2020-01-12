import os
from flask import Flask, jsonify
from flask_restful import Resource, Api
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app_settings = os.getenv("APP_SETTINGS")
app.config.from_object(app_settings)

api = Api(app)
db = SQLAlchemy(app)


class User(db.Model):
    __tablename__ = "users"
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    email = db.Column(db.String(128), nullable=False)
    active = db.Column(db.Boolean(), default=True, nullable=False)

    def __init__(self, email):
        self.email = email


class UsersPing(Resource):
    def get(self):
        return {
            "status": "success",
            "message": "pong!"
        }


api.add_resource(UsersPing, "/users/ping")
