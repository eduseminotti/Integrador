#coding: utf-8
from flask import Blueprint, render_template

bp_admin = Blueprint('admin', __name__, url_prefix='/admin', template_folder='templates')

@bp_admin.route("/")
def index():
    return render_template('admin_index.html')

@bp_admin.route("/users")
def users():
    return render_template('admin_users.html')