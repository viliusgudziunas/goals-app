import os
from datetime import datetime, timedelta

import jwt
from flask import current_app
from sqlalchemy.sql import func

from project import bcrypt, db


class User(db.Model):
    """
    User Model for storing users data
    """

    __tablename__ = "users"

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    email = db.Column(db.String(128), nullable=False, unique=True)
    password = db.Column(db.String(255), nullable=False)
    active = db.Column(db.Boolean(), default=True, nullable=False)
    created_date = db.Column(db.DateTime, default=func.now(), nullable=False)

    def __init__(self, email, password):
        self.email = email
        self.password = bcrypt.generate_password_hash(
            password, current_app.config.get("BCRYPT_LOG_ROUNDS")
        ).decode()

    def encode_auth_token(self, id):
        """Generate user auth token"""
        payload = {
            "exp": datetime.utcnow()
            + timedelta(
                days=current_app.config.get("TOKEN_EXPIRATION_DAYS"),
                seconds=current_app.config.get("TOKEN_EXPIRATION_SECONDS"),
            ),
            "iat": datetime.utcnow(),
            "sub": id,
        }
        return jwt.encode(
            payload, current_app.config.get("SECRET_KEY"), algorithm="HS256"
        )

    @staticmethod
    def decode_auth_token(token):
        """Decodes jwt token"""
        try:
            payload = jwt.decode(token, current_app.config.get("SECRET_KEY"))

            is_blacklisted = BlacklistToken.check_blacklist(token)
            if is_blacklisted:
                return "Token blacklisted"

            return payload["sub"]

        except jwt.ExpiredSignatureError:
            return "Signature expired"

        except jwt.InvalidTokenError:
            return "Invalid token"


class BlacklistToken(db.Model):
    """
    Token Model for storing JWT tokens
    """

    __tablename__ = "blacklist_tokens"

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    token = db.Column(db.String(500), unique=True, nullable=False)
    blacklisted_on = db.Column(db.DateTime, default=func.now(), nullable=False)

    def __init__(self, token):
        self.token = token

    @staticmethod
    def check_blacklist(auth_token):
        """Check whether auth token has been blacklisted"""
        token = BlacklistToken.query.filter_by(token=str(auth_token)).first()
        if token:
            return True

        return False


if os.getenv("FLASK_ENV") == "development":
    from project import admin
    from project.util.admin import UsersAdminView

    admin.add_view(UsersAdminView(User, db.session))
