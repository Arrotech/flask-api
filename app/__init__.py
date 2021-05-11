from os import path
from dotenv import load_dotenv
from flask import Flask
from instance.config import app_config
from app.extensions import db, bootstrap, cors


def create_app(config_name='development'):
    """Create and set up the application."""

    app = Flask(__name__, instance_relative_config=True)

    app.config.from_object(app_config[config_name])
    app.config.from_pyfile('config.py')
    bootstrap.init_app(app)
    cors.init_app(app)

    from app.api.v1.home import models

    db.init_app(app)

    from app.api.v1 import blueprint_v1

    app.register_blueprint(blueprint_v1, url_prefix='/api/v1/')

    base_dir = path.abspath(path.dirname(__name__))
    load_dotenv(path.join(base_dir, '.env'))

    return app
