#coding: utf-8
from flask import Blueprint, render_template, request, url_for, session, redirect 

bp_avisos = Blueprint('bp_avisos', __name__, url_prefix='/avisos', template_folder='templates')

@bp_avisos.route('/')
def Avisos():
    return render_template("avisos.html"), 200