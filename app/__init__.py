from flask import Flask
from instance.config import app_config
from app.extensions import db, cors
from utils.utils import load_env_file
from app.celery import make_celery


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

    load_env_file()

    return app
