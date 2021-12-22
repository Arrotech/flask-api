import os
from app.celery import make_celery
from app.__init__ import create_app

app = create_app(os.environ.get('FLASK_ENV'))
celery = make_celery(app)
