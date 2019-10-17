#coding: utf-8
from flask import Blueprint, render_template, request, session, redirect , url_for
from AdminDB import Admin

bp_home = Blueprint('home', __name__, url_prefix='/', template_folder='templates')


@bp_home.route("/")
def index():

    admin = Admin()

    result = admin.selectConfig()

    return render_template('home_index.html' , result=result)
    
