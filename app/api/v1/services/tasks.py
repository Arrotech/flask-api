import os
from app.celery import make_celery
from app.__init__ import create_app

app = create_app(os.environ.get('FLASK_ENV', default='development'))
celery = make_celery(app)

@celery.task
def company(name):
    """Define company."""
    return name
