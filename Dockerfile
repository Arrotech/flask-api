FROM tiangolo/uwsgi-nginx-flask:python3.6-alpine3.7

RUN apk --update add bash nano

WORKDIR /flask-api

COPY requirements.txt .

RUN apk add build-base

RUN pip install -r requirements.txt

COPY . .
COPY templates /flask-api/templates

CMD ["flask", "run", "--host", "0.0.0.0"]
