from flask import render_template

from app.api.v1 import blueprint_v1
# write your views here


@blueprint_v1.route('/home')
def index():
    """Home page endpoint."""
    return render_template('home/index.html')
