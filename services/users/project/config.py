import os


class BaseConfig:
    """Base configuration"""

    BCRYPT_LOG_ROUNDS = 13
    DEBUG = False
    ERROR_404_HELP = False
    SECRET_KEY = os.environ.get("SECRET_KEY")
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    TESTING = False
    TOKEN_EXPIRATION_DAYS = 30
    TOKEN_EXPIRATION_SECONDS = 0


class DevelopmentConfig(BaseConfig):
    """Development configuration"""

    BCRYPT_LOG_ROUNDS = 4
    DEBUG = True
    ENV = "development"
    SQLALCHEMY_DATABASE_URI = os.environ.get("DATABASE_URL")


class TestingConfig(BaseConfig):
    """Testing configuration"""

    BCRYPT_LOG_ROUNDS = 4
    ENV = "testing"
    SQLALCHEMY_DATABASE_URI = os.environ.get("DATABASE_TEST_URL")
    TESTING = True
    TOKEN_EXPIRATION_DAYS = 0
    TOKEN_EXPIRATION_SECONDS = 1


class ProductionConfig(BaseConfig):
    """Production configuration"""

    ENV = "production"
    SQLALCHEMY_DATABASE_URI = os.environ.get("DATABASE_URL")
