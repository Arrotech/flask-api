from flask import Blueprint

blueprint_v1 = Blueprint('blueprint_v1', __name__, template_folder='../../../templates', static_folder='../../../static')

from app.api.v1.home import views 