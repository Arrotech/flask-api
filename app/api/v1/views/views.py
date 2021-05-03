from arrotechtools import Serializer

from app.api.v1 import blueprint_v1

# write your views here


@blueprint_v1.route('/')
def index():
    """Home page endpoint."""

    response = {
        "msg": "Welcome to Flask API"
    }

    return Serializer.serialize(response, 200, "OK")
