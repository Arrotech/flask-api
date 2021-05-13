import os
from celery import Celery
from instance.config import app_config


def make_celery(app):
    celery = Celery(
        app.import_name,
        broker=app_config[os.environ.get('FLASK_ENV')].REDISTOGO_URL,
        backend=app_config[os.environ.get('FLASK_ENV')].REDISTOGO_URL
    )
    celery.conf.update(app_config[os.environ.get(
        'FLASK_ENV')].CELERY_CONFIG)

    TaskBase = celery.Task

    class ContextTask(TaskBase):
        def __call__(self, *args, **kwargs):
            with app.app_context():
                return self.run(*args, **kwargs)

    celery.Task = ContextTask
    return celery