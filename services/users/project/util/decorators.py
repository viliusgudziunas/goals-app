from functools import wraps

from flask import request

from project.models import User


def token_required(api):
    def decorator_function(f):
        @wraps(f)
        def decorated_function(self, *args, **kwargs):
            auth_header = request.headers.get("Authorization")
            if not auth_header:
                api.abort(401, "No auth token provided", status="fail")

            try:
                auth_token = auth_header.split(" ")[1]
            except IndexError:
                api.abort(401, "Invalid token", status="fail")

            resp = User.decode_auth_token(auth_token)
            if isinstance(resp, str):
                api.abort(401, resp, status="fail")

            user = User.query.filter_by(id=resp).first()
            if not user or not user.active:
                api.abort(401, "Invalid token", status="fail")

            return f(self, auth_token, resp, *args, **kwargs)

        return decorated_function

    return decorator_function
