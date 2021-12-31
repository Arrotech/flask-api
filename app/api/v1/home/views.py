from flask import render_template

from app.api.v1 import blueprint_v1
from app.api.v1.services.tasks import company
# write your views here


@blueprint_v1.route('/home')
def index():
    """Home page endpoint."""
    # company.delay("Arrotech")
    return render_template('home/index.html')
