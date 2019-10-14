#coding: utf-8
from flask import Blueprint, render_template , redirect , url_for , request
from mod_login.login import validaSessao
from AvisosDB import Avisos

bp_avisos = Blueprint('Avisos', __name__, url_prefix='/avisos', template_folder='templates')

@bp_avisos.route('/')
def Index():
    return render_template("avisosIndex.html"), 200

@bp_avisos.route('/AvisosAdm')
@validaSessao
def AvisosAdm():

    avisos = Avisos()

    result = avisos.selectAvisosALLAdm() 

    return render_template("avisosAdm.html", result=result), 200

@bp_avisos.route('/avisosNew')
@validaSessao
def avisosNew():
    return render_template('avisosNew.html')    

    
@bp_avisos.route('/AddAviso', methods=['POST'])
@validaSessao
def AddAviso():

    avisos = Avisos()

    avisos.Titulo = request.form['Titulo']
    avisos.Conteudo = request.form['Conteudo']
    avisos.DataInicial = request.form['DataIncial']
    avisos.DataFinal = request.form['DataFinal']
    avisos.Tipo = 4
    avisos.Status = request.form['Status']
    avisos.UserPostId = request.form['UserId']
    

    exec = avisos.insertAviso()

    return redirect(url_for('usuarios.index', resultInsert=exec))