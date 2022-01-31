import json
from flask import render_template, request, jsonify
from app.api.v1.home.models import User
from app.extensions import db
from arrotechtools import Serializer

from app.api.v1 import blueprint_v1
# write your views here


@blueprint_v1.route('/users', methods=['GET'])
def get_users():
    """Home page endpoint."""
    return Serializer(
        json.loads(fetch_all(User)),
        200,
        "Successfully retrieved.").serialize()


@blueprint_v1.route('/user', methods=['POST'])
def add_user():
    """Add user."""
    record = add_record("username", "email")
    user = User(record[0], record[1])
    db.session.add(user)
    db.session.commit()
    return Serializer(
        dict(user.as_dict()),
        201,
        "Account successfully created.").serialize()


@blueprint_v1.route('/user/<int:id>', methods=['GET', 'DELETE'])
def get_user(id):
    """Get a specific user by id."""
    if request.method == 'GET':
        return Serializer(
            json.loads(fetch_one(User, id)),
            200,
            "Successfully retrieved.").serialize()
    elif request.method == 'DELETE':
        record = User.query.filter_by(id=id).first()
        db.session.delete(record)
        db.session.commit()
        return Serializer(204,
                          "Successfully deleted.").on_success()


def add_record(*args):
    data = request.get_json()
    details = []
    for arg in args:
        details.append(data[arg])
    return details


def fetch_all(model):
    """Fetches all records."""
    records = model.query.all()
    records_list = []
    for record in records:
        records_list.append(record.as_dict())
    return json.dumps(records_list, default=str)


def fetch_one(model, id):
    """Fetches one record."""
    record = model.query.filter_by(id=id).first()
    return json.dumps(dict(record.as_dict()), default=str)
