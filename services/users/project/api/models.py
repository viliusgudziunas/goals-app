import os

from sqlalchemy.sql import func

from project import db


class User(db.Model):
    __tablename__ = "users"
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    email = db.Column(db.String(128), nullable=False)
    active = db.Column(db.Boolean(), default=True, nullable=False)
    created_date = db.Column(db.DateTime, default=func.now(), nullable=False)

    def __init__(self, email):
        self.email = email


if os.getenv("FLASK_ENV") == "development":
    from project import admin
    from project.api.admin import UsersAdminView

    admin.add_view(UsersAdminView(User, db.session))
