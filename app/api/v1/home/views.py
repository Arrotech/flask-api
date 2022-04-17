import json
from flask import render_template, request, jsonify
from app.api.v1.home.models import User
from app.extensions import db
from arrotechtools import Serializer, Validate, ErrorHandler
from sqlalchemy import exc

from app.api.v1 import blueprint_v1
# write your views here


@blueprint_v1.route('/home', methods=['GET'])
def index():
    """Home page."""
    return render_template('home/index.html')


@blueprint_v1.route('/users', methods=['GET', 'POST'])
def users():
    """Add user."""
    try:
        errors = Validate.request_body_keys(request, ["username", "email"])
        if errors:
            return ErrorHandler.raise_error(message="Invalid {} key".format(', '.join(errors)),  # noqa
                                            status_code=400)
        if request.method == 'GET':
            users = fetch_all(User)
            return Serializer.serialize(response=User.serialize_records(users),
                                        message="Successfully retrieved.",
                                        status_code=200
                                        )
        record = add_record("username", "email")
        if not Validate.email(record[1]):
            return ErrorHandler.raise_error(message="Invalid email",
                                            status_code=400)
        user = User(record[0], record[1])
        db.session.add(user)
        db.session.commit()
        return Serializer.serialize(response=user.serialize_record(),
                                    message="Account successfully created.",
                                    status_code=201)
    except Exception as e:
        return ErrorHandler.raise_error(message=str(e),
                                        status_code=400)


@blueprint_v1.route('/user/<int:id>', methods=['GET', 'DELETE', 'PUT', 'PATCH'])  # noqa
def get_user(id):
    """Get a specific user by id."""
    try:
        user = fetch_one(User, id)

        if request.method == 'GET':
            return Serializer.serialize(
                response=user.serialize_record(),
                message="Successfully retrieved.",
                status_code=200)
        elif request.method == 'DELETE':
            db.session.delete(user)
            db.session.commit()
            return Serializer.on_success(status_code=204,
                                         message="Account deleted")
        elif request.method == 'PUT':
            record = update_record(User, id, "username", "email")
            return Serializer.serialize(response=record.serialize_record(),
                                        message="Account successfully updated.",  # noqa
                                        status_code=200)
        elif request.method == 'PATCH':
            record = update_record(User, id, "username")
            return Serializer.serialize(response=record.serialize_record(),
                                        message="Account successfully updated.",  # noqa
                                        status_code=200)
    except Exception:
        return ErrorHandler.raise_error(message="Resource not found",
                                        status_code=404)


def add_record(*args):
    """Add a record."""
    data = request.get_json()
    details = []
    for arg in args:
        details.append(data[arg])
    return details


def update_record(model, id, *args):
    """Updates a record."""
    record = fetch_one(model, id)
    data = request.get_json()
    for arg in args:
        setattr(record, arg, data[arg])
    db.session.commit()
    return record


def fetch_all(model):
    """Fetches all records."""
    records = model.query.all()
    return records


def fetch_one(model, id):
    """Fetches one record."""
    record = model.query.filter_by(id=id).first()
    return record
