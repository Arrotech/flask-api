import os
from utils.utils import load_env_file

load_env_file()


class Config(object):

    """App default settings."""

    DEBUG = False
    TESTING = False

    SECRET_KEY = os.environ.get('SECRET_KEY', default='dsbsjsbdkjsdskdb')
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URI')

    CELERY_BROKER_URL = os.environ.get('CELERY_BROKER_URL')
    CELERY_RESULT_BACKEND = os.environ.get('CELERY_RESULT_BACKEND')
    SESSION_COOKIE_SECURE = False

    # celery config
    CELERY_CONFIG = {}


class DevelopmentConfig(Config):

    """Development app settings."""

    DEBUG = True


class ProductionConfig(Config):

    """Production app settings."""

    DEBUG = False
    TESTING = False


class TestingConfig(Config):

    """Testing app configurations."""

    TESTING = True
    DEBUG = True

    SQLALCHEMY_DATABASE_URI = os.environ.get('TEST_DATABASE_URI')


class ReleaseConfig(Config):

    """Release app configuration settings."""


class StagingConfig(Config):

    """Staging area configuration settings."""

    DEBUG = True


app_config = dict(
    development=DevelopmentConfig,
    production=ProductionConfig,
    testing=TestingConfig,
    release=ReleaseConfig,
    staging=StagingConfig
)
