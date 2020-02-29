import os
from datetime import timedelta


def test_development_config(test_app):
    test_app.config.from_object("project.config.DevelopmentConfig")
    assert len(list(test_app.config)) == 47

    assert test_app.config["APPLICATION_ROOT"] == "/"
    assert test_app.config["BCRYPT_LOG_ROUNDS"] == 4
    assert test_app.config["DEBUG"]
    assert test_app.config["ENV"] == "development"
    assert not test_app.config["ERROR_404_HELP"]
    assert not test_app.config["EXPLAIN_TEMPLATE_LOADING"]
    assert test_app.config["JSON_AS_ASCII"]
    assert test_app.config["JSON_SORT_KEYS"]
    assert test_app.config["JSONIFY_MIMETYPE"] == "application/json"
    assert not test_app.config["JSONIFY_PRETTYPRINT_REGULAR"]
    assert test_app.config["MAX_COOKIE_SIZE"] == 4093
    assert test_app.config["MAX_CONTENT_LENGTH"] is None
    assert test_app.config["PERMANENT_SESSION_LIFETIME"] == timedelta(days=31)
    assert test_app.config["PREFERRED_URL_SCHEME"] == "http"
    assert not test_app.config["PRESERVE_CONTEXT_ON_EXCEPTION"]
    assert test_app.config["PROPAGATE_EXCEPTIONS"] is None
    assert test_app.config["RESTX_MASK_HEADER"] == "X-Fields"
    assert test_app.config["RESTX_MASK_SWAGGER"]
    assert test_app.config["SECRET_KEY"] == os.environ.get("SECRET_KEY")
    assert test_app.config["SEND_FILE_MAX_AGE_DEFAULT"] == timedelta(seconds=43200)
    assert test_app.config["SERVER_NAME"] is None
    assert test_app.config["SESSION_COOKIE_DOMAIN"] is None
    assert test_app.config["SESSION_COOKIE_HTTPONLY"]
    assert test_app.config["SESSION_COOKIE_NAME"] == "session"
    assert test_app.config["SESSION_COOKIE_PATH"] is None
    assert test_app.config["SESSION_COOKIE_SAMESITE"] is None
    assert not test_app.config["SESSION_COOKIE_SECURE"]
    assert test_app.config["SESSION_REFRESH_EACH_REQUEST"]
    assert test_app.config["SQLALCHEMY_BINDS"] is None
    assert not test_app.config["SQLALCHEMY_COMMIT_ON_TEARDOWN"]
    assert test_app.config["SQLALCHEMY_DATABASE_URI"] == os.environ.get("DATABASE_URL")
    assert not test_app.config["SQLALCHEMY_ECHO"]
    assert test_app.config["SQLALCHEMY_ENGINE_OPTIONS"] == {}
    assert test_app.config["SQLALCHEMY_MAX_OVERFLOW"] is None
    assert test_app.config["SQLALCHEMY_NATIVE_UNICODE"] is None
    assert test_app.config["SQLALCHEMY_POOL_RECYCLE"] is None
    assert test_app.config["SQLALCHEMY_POOL_SIZE"] is None
    assert test_app.config["SQLALCHEMY_POOL_TIMEOUT"] is None
    assert test_app.config["SQLALCHEMY_RECORD_QUERIES"] is None
    assert not test_app.config["SQLALCHEMY_TRACK_MODIFICATIONS"]
    assert test_app.config["TEMPLATES_AUTO_RELOAD"] is None
    assert not test_app.config["TESTING"]
    assert test_app.config["TOKEN_EXPIRATION_DAYS"] == 30
    assert test_app.config["TOKEN_EXPIRATION_SECONDS"] == 0
    assert test_app.config["TRAP_BAD_REQUEST_ERRORS"] is None
    assert not test_app.config["TRAP_HTTP_EXCEPTIONS"]
    assert not test_app.config["USE_X_SENDFILE"]


def test_testing_config(test_app):
    test_app.config.from_object("project.config.TestingConfig")
    assert len(list(test_app.config)) == 47

    assert test_app.config["APPLICATION_ROOT"] == "/"
    assert test_app.config["BCRYPT_LOG_ROUNDS"] == 4
    assert not test_app.config["DEBUG"]
    assert test_app.config["ENV"] == "testing"
    assert not test_app.config["ERROR_404_HELP"]
    assert not test_app.config["EXPLAIN_TEMPLATE_LOADING"]
    assert test_app.config["JSON_AS_ASCII"]
    assert test_app.config["JSON_SORT_KEYS"]
    assert test_app.config["JSONIFY_MIMETYPE"] == "application/json"
    assert not test_app.config["JSONIFY_PRETTYPRINT_REGULAR"]
    assert test_app.config["MAX_COOKIE_SIZE"] == 4093
    assert test_app.config["MAX_CONTENT_LENGTH"] is None
    assert test_app.config["PERMANENT_SESSION_LIFETIME"] == timedelta(days=31)
    assert test_app.config["PREFERRED_URL_SCHEME"] == "http"
    assert not test_app.config["PRESERVE_CONTEXT_ON_EXCEPTION"]
    assert test_app.config["PROPAGATE_EXCEPTIONS"] is None
    assert test_app.config["RESTX_MASK_HEADER"] == "X-Fields"
    assert test_app.config["RESTX_MASK_SWAGGER"]
    assert test_app.config["SECRET_KEY"] == os.environ.get("SECRET_KEY")
    assert test_app.config["SEND_FILE_MAX_AGE_DEFAULT"] == timedelta(seconds=43200)
    assert test_app.config["SERVER_NAME"] is None
    assert test_app.config["SESSION_COOKIE_DOMAIN"] is None
    assert test_app.config["SESSION_COOKIE_HTTPONLY"]
    assert test_app.config["SESSION_COOKIE_NAME"] == "session"
    assert test_app.config["SESSION_COOKIE_PATH"] is None
    assert test_app.config["SESSION_COOKIE_SAMESITE"] is None
    assert not test_app.config["SESSION_COOKIE_SECURE"]
    assert test_app.config["SESSION_REFRESH_EACH_REQUEST"]
    assert test_app.config["SQLALCHEMY_BINDS"] is None
    assert not test_app.config["SQLALCHEMY_COMMIT_ON_TEARDOWN"]
    assert test_app.config["SQLALCHEMY_DATABASE_URI"] == os.environ.get(
        "DATABASE_TEST_URL"
    )
    assert not test_app.config["SQLALCHEMY_ECHO"]
    assert test_app.config["SQLALCHEMY_ENGINE_OPTIONS"] == {}
    assert test_app.config["SQLALCHEMY_MAX_OVERFLOW"] is None
    assert test_app.config["SQLALCHEMY_NATIVE_UNICODE"] is None
    assert test_app.config["SQLALCHEMY_POOL_RECYCLE"] is None
    assert test_app.config["SQLALCHEMY_POOL_SIZE"] is None
    assert test_app.config["SQLALCHEMY_POOL_TIMEOUT"] is None
    assert test_app.config["SQLALCHEMY_RECORD_QUERIES"] is None
    assert not test_app.config["SQLALCHEMY_TRACK_MODIFICATIONS"]
    assert test_app.config["TEMPLATES_AUTO_RELOAD"] is None
    assert test_app.config["TESTING"]
    assert test_app.config["TOKEN_EXPIRATION_DAYS"] == 0
    assert test_app.config["TOKEN_EXPIRATION_SECONDS"] == 1
    assert test_app.config["TRAP_BAD_REQUEST_ERRORS"] is None
    assert not test_app.config["TRAP_HTTP_EXCEPTIONS"]
    assert not test_app.config["USE_X_SENDFILE"]


def test_production_config(test_app):
    test_app.config.from_object("project.config.ProductionConfig")
    assert len(list(test_app.config)) == 47

    assert test_app.config["APPLICATION_ROOT"] == "/"
    assert test_app.config["BCRYPT_LOG_ROUNDS"] == 13
    assert not test_app.config["DEBUG"]
    assert test_app.config["ENV"] == "production"
    assert not test_app.config["ERROR_404_HELP"]
    assert not test_app.config["EXPLAIN_TEMPLATE_LOADING"]
    assert test_app.config["JSON_AS_ASCII"]
    assert test_app.config["JSON_SORT_KEYS"]
    assert test_app.config["JSONIFY_MIMETYPE"] == "application/json"
    assert not test_app.config["JSONIFY_PRETTYPRINT_REGULAR"]
    assert test_app.config["MAX_COOKIE_SIZE"] == 4093
    assert test_app.config["MAX_CONTENT_LENGTH"] is None
    assert test_app.config["PERMANENT_SESSION_LIFETIME"] == timedelta(days=31)
    assert test_app.config["PREFERRED_URL_SCHEME"] == "http"
    assert not test_app.config["PRESERVE_CONTEXT_ON_EXCEPTION"]
    assert test_app.config["PROPAGATE_EXCEPTIONS"] is None
    assert test_app.config["RESTX_MASK_HEADER"] == "X-Fields"
    assert test_app.config["RESTX_MASK_SWAGGER"]
    assert test_app.config["SECRET_KEY"] == os.environ.get("SECRET_KEY")
    assert test_app.config["SEND_FILE_MAX_AGE_DEFAULT"] == timedelta(seconds=43200)
    assert test_app.config["SERVER_NAME"] is None
    assert test_app.config["SESSION_COOKIE_DOMAIN"] is None
    assert test_app.config["SESSION_COOKIE_HTTPONLY"]
    assert test_app.config["SESSION_COOKIE_NAME"] == "session"
    assert test_app.config["SESSION_COOKIE_PATH"] is None
    assert test_app.config["SESSION_COOKIE_SAMESITE"] is None
    assert not test_app.config["SESSION_COOKIE_SECURE"]
    assert test_app.config["SESSION_REFRESH_EACH_REQUEST"]
    assert test_app.config["SQLALCHEMY_BINDS"] is None
    assert not test_app.config["SQLALCHEMY_COMMIT_ON_TEARDOWN"]
    assert test_app.config["SQLALCHEMY_DATABASE_URI"] == os.environ.get("DATABASE_URL")
    assert not test_app.config["SQLALCHEMY_ECHO"]
    assert test_app.config["SQLALCHEMY_ENGINE_OPTIONS"] == {}
    assert test_app.config["SQLALCHEMY_MAX_OVERFLOW"] is None
    assert test_app.config["SQLALCHEMY_NATIVE_UNICODE"] is None
    assert test_app.config["SQLALCHEMY_POOL_RECYCLE"] is None
    assert test_app.config["SQLALCHEMY_POOL_SIZE"] is None
    assert test_app.config["SQLALCHEMY_POOL_TIMEOUT"] is None
    assert test_app.config["SQLALCHEMY_RECORD_QUERIES"] is None
    assert not test_app.config["SQLALCHEMY_TRACK_MODIFICATIONS"]
    assert test_app.config["TEMPLATES_AUTO_RELOAD"] is None
    assert not test_app.config["TESTING"]
    assert test_app.config["TOKEN_EXPIRATION_DAYS"] == 30
    assert test_app.config["TOKEN_EXPIRATION_SECONDS"] == 0
    assert test_app.config["TRAP_BAD_REQUEST_ERRORS"] is None
    assert not test_app.config["TRAP_HTTP_EXCEPTIONS"]
    assert not test_app.config["USE_X_SENDFILE"]
