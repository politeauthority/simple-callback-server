"""Home - Controller
from flask import Blueprint, request, render_template, flash, g, session, redirect

"""

from flask import Blueprint, render_template

home = Blueprint('Home', __name__, url_prefix='/')


@home.route('')
def index():
    """
    Index

    """
    d = {}
    return render_template('home/index.html', **d)

# End File: stocky/app/controllers/home.py
