FROM tiangolo/uwsgi-nginx-flask:python3.6-alpine3.7

WORKDIR /app

ENV FLASK_APP=run.py
ENV FLASK_ENV=development

COPY requirements.txt .

RUN apk add build-base

RUN pip3 install -r requirements.txt

CMD ["flask", "run"]
