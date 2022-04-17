from flask import Flask
from instance.config import app_config
from app.extensions import db, cors
from utils.utils import load_env_file
from app.celery import make_celery
from arrotechtools import ErrorHandler


def create_app(config_name='development'):
    """Create and set up the application."""
    app = Flask(__name__, instance_relative_config=True)

    app.config.from_object(app_config[config_name])
    app.config.from_pyfile('config.py')
    cors.init_app(app)
    make_celery(app)

    from app.api.v1.home import models  # noqa

    db.init_app(app)

    from app.api.v1 import blueprint_v1  # noqa

    app.register_blueprint(blueprint_v1, url_prefix='/api/v1/')
    app.register_error_handler(400, ErrorHandler.bad_request)
    app.register_error_handler(404, ErrorHandler.page_not_found)
    app.register_error_handler(405, ErrorHandler.method_not_allowed)
    app.register_error_handler(500, ErrorHandler.internal_server_error)

    load_env_file()

    return app
