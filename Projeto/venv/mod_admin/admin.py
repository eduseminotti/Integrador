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

    result = admin.selectConfig()
    
    return render_template('admin_index.html', result=result)

@bp_admin.route("/EditarConfig", methods=['POST'])
@validaSessao
def EditarConfig():

    admin = Admin()
    
    admin.Nome = request.form['Nome']
    admin.Phone = request.form['Phone']
    admin.Email = request.form['Email']

    exec = admin.updateConfig()

    return redirect(url_for('admin.index', resultInsert=exec))