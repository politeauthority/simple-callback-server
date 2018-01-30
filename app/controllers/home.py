"""Home - Controller

"""

from flask import Blueprint, request

from app.models.web_request import WebRequest

home = Blueprint('Home', __name__, url_prefix='/')


@home.route('', defaults={'path': ''}, methods=['GET', 'POST'])
@home.route('<path:path>', methods=['GET', 'POST'])
def index(path):
    """
    Index

    :param path: url extensions
    :type path: str
    """
    if request.method == 'POST':
        data = request.form['POST']
    else:
        data = request.args
    wr = WebRequest()
    wr.uri = '/%s' % path
    wr.data = data
    wr.ip = request.remote_addr
    wr.save()
    return ''


@home.route('ip', methods=['GET', 'POST'])
def ip():
    """
    ip
    Fire off the requesting entities IP address

    """
    wr = WebRequest()
    wr.uri = '/ip'
    wr.data = request.form
    wr.ip = request.remote_addr
    wr.save()
    return str(request.remote_addr)

# End File: simple-callback-server/app/controllers/home.py
