import os
from app import create_app
from instance.celeryconfig import make_celery

app = create_app(os.environ.get('FLASK_ENV'))
celery = make_celery(app)

# write your tasks here
# create a task and use the @celery decorator 