#coding: utf-8
from flask import Blueprint, render_template, request, url_for, session, redirect 

bp_noticias = Blueprint('bp_noticias', __name__, url_prefix='/noticias', template_folder='templates')

@bp_noticias.route('/')
def Noticias():
    return render_template("noticias.html"), 200