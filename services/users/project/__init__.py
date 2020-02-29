import os
from flask import Flask
from flask_admin import Admin
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS
from flask_migrate import Migrate
from flask_bcrypt import Bcrypt


db = SQLAlchemy()
admin = Admin(template_mode="bootstrap3")
cors = CORS()
migrate = Migrate()
bcrypt = Bcrypt()


def create_app(script_info=None):
    app = Flask(__name__)

    app_settings = os.getenv("APP_SETTINGS")
    app.config.from_object(app_settings)

    db.init_app(app)
    if os.getenv("FLASK_ENV") == "development":
        admin.init_app(app)
    cors.init_app(app)
    migrate.init_app(app, db)
    bcrypt.init_app(app)

    from project.api import blueprint as users_blueprint

    app.register_blueprint(users_blueprint)

    @app.shell_context_processor
    def ctx():
        return {"app": app, "db": db}

    return app
