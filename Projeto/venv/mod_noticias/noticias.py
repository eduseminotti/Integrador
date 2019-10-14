#coding: utf-8
from flask import Blueprint, render_template, request, url_for, session, redirect 
from mod_login.login import validaSessao 

bp_noticias = Blueprint('noticias', __name__, url_prefix='/noticias', template_folder='templates')

@bp_noticias.route('/')
def Noticias():
    return render_template("noticias.html"), 200

@bp_noticias.route('/nova')
@validaSessao
def usuarios_new():
    return render_template('noticia_new.html')        