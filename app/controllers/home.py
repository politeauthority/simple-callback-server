"""Home - Controller

"""

from flask import Blueprint, render_template, request

from app.models.web_request import WebRequest

home = Blueprint('Home', __name__, url_prefix='/')


@home.route('', methods=['GET', 'POST'])
def index():
    """
    Index

    """
    wr = WebRequest()
    wr.uri = '/'
    wr.data = request.form
    wr.ip = request.remote_addr
    wr.save()
    return str(request.form)
    d = {}
    return render_template('home/index.html', **d)

# End File: simple-callback-server/app/controllers/home.py
