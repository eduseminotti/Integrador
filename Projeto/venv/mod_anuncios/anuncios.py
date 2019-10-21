#coding: utf-8
from flask import Blueprint, render_template , redirect , url_for , request ,session
from mod_login.login import validaSessao
from AnunciosDB import AnunciosPublic
from ValidaUserDB import ValidaUser

bp_anuncios = Blueprint('anuncios', __name__, url_prefix='/anuncios', template_folder='templates')

@bp_anuncios.route('/')
def index():
    
    anuncios = AnunciosPublic()

    result = anuncios.selectAllAnunciosPublic()
        
    return render_template("AllAnunciosPublic.html", result=result), 200 