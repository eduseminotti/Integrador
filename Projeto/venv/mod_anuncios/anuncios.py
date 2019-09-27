#coding: utf-8
from flask import Blueprint, render_template, request, url_for, session, redirect 

bp_anuncios = Blueprint('bp_anuncios', __name__, url_prefix='/anuncios', template_folder='templates')

@bp_anuncios.route('/')
def Anuncios():
    return render_template("anuncios.html"), 200