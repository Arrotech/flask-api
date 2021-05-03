from flask import Blueprint

blueprint_v1 = Blueprint('blueprint_v1', __name__)

from app.api.v1.views import views 