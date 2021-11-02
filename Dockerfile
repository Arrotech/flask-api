# pull image
FROM tiangolo/uwsgi-nginx-flask:python3.6-alpine3.7

RUN apk --update add bash nano

# set the working directory
WORKDIR /flask-api

# copy the requirements
COPY requirements.txt .

# install the dependencies
RUN apk add build-base
RUN pip install -r requirements.txt

# copy the project
COPY . .
COPY templates /flask-api/templates

CMD ["flask", "run", "--host", "0.0.0.0"]
