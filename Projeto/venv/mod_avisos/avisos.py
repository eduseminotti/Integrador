#coding: utf-8
from flask import Blueprint, render_template , redirect , url_for , request
from mod_login.login import validaSessao
from AvisosDB import Avisos

bp_avisos = Blueprint('Avisos', __name__, url_prefix='/avisos', template_folder='templates')

@bp_avisos.route('/')
def Index():
    avisos = Avisos()

    result = avisos.selectAvisosALL()

    return render_template("avisosIndex.html", result=result), 200

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
    avisos.DataInicial = request.form['DataInicial']
    avisos.DataFinal = request.form['DataFinal']
    avisos.Tipo = 4

    avisos.UserPostId = request.form['UserId']

    Status = 'Status'  in  request.form

    if Status == "on" or Status == True:
        avisos.Status = 1
    else:    
        avisos.Status = 0

    exec = avisos.updateAviso()

    exec = avisos.insertAviso()

    return redirect(url_for('Avisos.AvisosAdm', resultInsert=exec))

@bp_avisos.route('/EditAviso', methods=['POST'])   
@validaSessao
def EditAviso():

    avisos = Avisos()

    avisos.id = request.form['Id']

    res = avisos.selectAvisoAdm()

    return render_template('avisosEdit.html', result=res )   

@bp_avisos.route('/UpdateAviso', methods=['POST'])   
@validaSessao
def UpdateAviso():

    avisos = Avisos()

    avisos.id = request.form['Id']
    avisos.Titulo = request.form['Titulo']
    avisos.Conteudo = request.form['Conteudo']
    avisos.DataInicial = request.form['DataInicial']
    avisos.DataFinal = request.form['DataFinal']
    avisos.Tipo = 4
    avisos.UserPostId = request.form['UserId']

    Status = 'Status'  in  request.form


    if Status == "on" or Status == True:
        avisos.Status = 1
    else:    
        avisos.Status = 0

    exec = avisos.updateAviso()

    return redirect(url_for('Avisos.AvisosAdm', resultInsert=exec , Status=Status))

@bp_avisos.route('/DeleteAviso', methods=['POST'])
@validaSessao
def DeleteAviso():

    avisos = Avisos()

    avisos.id = request.form['Id']

    exec = avisos.DeleteAviso() 

    return redirect(url_for('Avisos.AvisosAdm', resultInsert=exec ))