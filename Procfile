web: gunicorn run:app
worker: celery -A app.api.v1.services.tasks.celery worker --loglevel=info --pool=solo