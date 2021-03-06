#coding: utf-8
from flask import Blueprint, render_template, request, session, redirect , url_for
from functools import wraps
from mod_login.login import validaSessao
from AdminDB import Admin

bp_admin = Blueprint('admin', __name__, url_prefix='/admin', template_folder='templates')

@bp_admin.route("/")
@validaSessao
def index():

    admin = Admin()

    result = admin.anunciospendentes()
    pendentes = 0
    for row in result:
        pendentes = row[0]



    return render_template('admin_index.html', pendentes=pendentes)

