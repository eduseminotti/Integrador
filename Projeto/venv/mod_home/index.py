#coding: utf-8
from flask import Blueprint, render_template
bp_index = Blueprint('index', __name__, url_prefix='/', template_folder='templates')

@bp_index.route("/")
def index():
    return render_template('home_index.html')

@bp_index.route("/home")
def index1():
    return render_template('home_index.html')

@bp_index.route("/users")
def users():
    return render_template('home_users.html')