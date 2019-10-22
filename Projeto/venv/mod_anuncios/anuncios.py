#coding: utf-8
from flask import Blueprint, render_template , redirect , url_for , request ,session
from mod_login.login import validaSessao
from AnunciosDB import Anuncios
from ValidaUserDB import ValidaUser

bp_anuncios = Blueprint('Anuncios', __name__, url_prefix='/anuncios', template_folder='templates')

@bp_anuncios.route('/')
def index():
    
    anuncios = Anuncios()

    result = anuncios.selectAllAnunciosPublic()
        
    return render_template("AllAnunciosPublic.html", result=result), 200 

@bp_anuncios.route('/AllAnunciosAdm')
@validaSessao
def AllAnunciosAdm():
    
    anuncios = Anuncios()

    result = anuncios.selectAnunciosAdm()
        
    return render_template("AllAnunciosAdm.html", result=result), 200 

@bp_anuncios.route('/AnunciosNew')
@validaSessao
def AnunciosNew():


    return render_template('AnunciosNew.html') 