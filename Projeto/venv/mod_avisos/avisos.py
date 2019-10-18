#coding: utf-8
from flask import Blueprint, render_template , redirect , url_for , request ,session
from mod_login.login import validaSessao
from AvisosDB import Avisos
from ValidaUserDB import ValidaUser

bp_avisos = Blueprint('Avisos', __name__, url_prefix='/avisos', template_folder='templates')

@bp_avisos.route('/')
def Index():
    avisos = Avisos()

    result = avisos.selectAvisosALL()

    return render_template("avisosIndex.html", result=result), 200

@bp_avisos.route('/AvisosAdm')
@validaSessao
def AvisosAdm():
    
    tipo = session['tipo']
    if tipo != 1 and tipo != 3 :  
        return redirect(url_for('home.index', msg="User_sem_Permissão_tipo_", tipo=tipo ))  
    
    avisos = Avisos()

    result = avisos.selectAvisosALLAdm() 
    
    return render_template("avisosAdm.html", result=result, tipo=tipo ), 200


@bp_avisos.route('/avisosNew')
@validaSessao
def avisosNew():

    tipo = session['tipo']
    if tipo != 1 and tipo != 3 :  
        return redirect(url_for('home.index', msg="User_sem_Permissão_tipo_", tipo=tipo ))


    return render_template('avisosNew.html')    
  
@bp_avisos.route('/AddAviso', methods=['POST'])
@validaSessao
def AddAviso():

    tipo = session['tipo']
    if tipo != 1 and tipo != 3 :  
        return redirect(url_for('home.index', msg="User_sem_Permissão_tipo_", tipo=tipo ,))

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

    tipo = session['tipo']
    if tipo != 1 and tipo != 3 :  
        return redirect(url_for('home.index', msg="User_sem_Permissão_tipo_", tipo=tipo ,))

    avisos = Avisos()

    avisos.id = request.form['Id']

    res = avisos.selectAvisoAdm()

    return render_template('avisosEdit.html', result=res )   

@bp_avisos.route('/UpdateAviso', methods=['POST'])   
@validaSessao
def UpdateAviso():

    tipo = session['tipo']
    if tipo != 1 and tipo != 3 :  
        return redirect(url_for('home.index', msg="User_sem_Permissão_tipo_", tipo=tipo ,))    

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

    tipo = session['tipo']
    if tipo != 1 and tipo != 3 :  
        return redirect(url_for('home.index', msg="User_sem_Permissão_tipo_", tipo=tipo ))  

    avisos = Avisos()

    avisos.id = request.form['Id']

    exec = avisos.DeleteAviso() 

    return redirect(url_for('Avisos.AvisosAdm', resultInsert=exec ))


