FROM tiangolo/uwsgi-nginx-flask:python3.6-alpine3.7
RUN apk --update add bash nano

ENV STATIC_URL /static
ENV STATIC_PATH /app/static
ENV FLASK_APP=run.py
ENV FLASK_ENV=development

COPY requirements.txt .

RUN apk add build-base

RUN pip install -r requirements.txt

CMD ["flask", "run"]
