import os


def test_development_config(test_app):
    test_app.config.from_object("project.config.DevelopmentConfig")
    assert not test_app.config["DEBUG"]
    assert not test_app.config["TESTING"]
    assert not test_app.config["SQLALCHEMY_TRACK_MODIFICATIONS"]
    assert test_app.config["SQLALCHEMY_DATABASE_URI"] == os.environ.get("DATABASE_URL")
    assert test_app.config["SECRET_KEY"] == os.environ.get("SECRET_KEY")
    assert test_app.config["BCRYPT_LOG_ROUNDS"] == 4
    assert test_app.config["TOKEN_EXPIRATION_DAYS"] == 30
    assert test_app.config["TOKEN_EXPIRATION_SECONDS"] == 0
    assert not test_app.config["ERROR_404_HELP"]


def test_testing_config(test_app):
    test_app.config.from_object("project.config.TestingConfig")
    assert not test_app.config["DEBUG"]
    assert not test_app.config["TESTING"]
    assert not test_app.config["SQLALCHEMY_TRACK_MODIFICATIONS"]
    assert test_app.config["SQLALCHEMY_DATABASE_URI"] == os.environ.get(
        "DATABASE_TEST_URL"
    )
    assert test_app.config["SECRET_KEY"] == os.environ.get("SECRET_KEY")
    assert test_app.config["BCRYPT_LOG_ROUNDS"] == 4
    assert test_app.config["TOKEN_EXPIRATION_DAYS"] == 0
    assert test_app.config["TOKEN_EXPIRATION_SECONDS"] == 1
    assert not test_app.config["ERROR_404_HELP"]


def test_production_config(test_app):
    test_app.config.from_object("project.config.ProductionConfig")
    assert not test_app.config["DEBUG"]
    assert not test_app.config["TESTING"]
    assert not test_app.config["SQLALCHEMY_TRACK_MODIFICATIONS"]
    assert test_app.config["SQLALCHEMY_DATABASE_URI"] == os.environ.get("DATABASE_URL")
    assert test_app.config["SECRET_KEY"] == os.environ.get("SECRET_KEY")
    assert test_app.config["BCRYPT_LOG_ROUNDS"] == 13
    assert test_app.config["TOKEN_EXPIRATION_DAYS"] == 30
    assert test_app.config["TOKEN_EXPIRATION_SECONDS"] == 0
    assert not test_app.config["ERROR_404_HELP"]
