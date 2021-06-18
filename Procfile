web: gunicorn run:app
worker: celery -A app.api.v1.tasks.celery worker --loglevel=info --pool=solo