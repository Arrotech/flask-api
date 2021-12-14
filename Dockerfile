FROM tiangolo/uwsgi-nginx-flask:python3.6-alpine3.7

WORKDIR /flask-api

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

ADD https://github.com/ufoscout/docker-compose-wait/releases/download/2.9.0/wait /wait

RUN chmod +x /wait

COPY . /flask-api

RUN apk add --no-cache bash nano
RUN apk add build-base
RUN pip3 install --upgrade setuptools
RUN pip3 install --upgrade pip
RUN apk update \
    && apk add postgresql-dev gcc python3-dev musl-dev
RUN pip install -r requirements.txt
EXPOSE 5000

CMD /wait && gunicorn --bind 0.0.0.0:5000 run:app

