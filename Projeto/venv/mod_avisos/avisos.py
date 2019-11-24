#coding: utf-8
from flask import Blueprint, render_template , redirect , url_for , request ,session
from mod_login.login import validaSessao
from AvisosDB import Avisos
from ValidaUserDB import ValidaUser
from Logs import Logs

bp_avisos = Blueprint('Avisos', __name__, url_prefix='/avisos', template_folder='templates')

@bp_avisos.route('/') 
def Index():
    avisos = Avisos()

    result = avisos.selectAvisosALL()

    return render_template("avisosIndex.html", result=result), 200

@bp_avisos.route('/AvisosAdm')
@validaSessao
def AvisosAdm():
    
    valida = ValidaUser()

    retorno = valida.validaPermissao("avisos", session['tipo'])
        
    if retorno != True :  
        return redirect(url_for('home.index', msg="User_sem_Permissão"))  
    
    avisos = Avisos()

    result = avisos.selectAvisosALLAdm() 
    
    return render_template("avisosAdm.html", result=result), 200


@bp_avisos.route('/avisosNew')
@validaSessao
def avisosNew():

    valida = ValidaUser()

    retorno = valida.validaPermissao("avisos", session['tipo'])
        
    if retorno != True :  
        return redirect(url_for('home.index', msg="User_sem_Permissão"))   


    return render_template('avisosNew.html')
  
@bp_avisos.route('/AddAviso', methods=['POST'])
@validaSessao
def AddAviso():

    valida = ValidaUser()

    retorno = valida.validaPermissao("avisos", session['tipo'])
        
    if retorno != True :  
        return redirect(url_for('home.index', msg="User_sem_Permissão"))  

    avisos = Avisos()

    avisos.Titulo = request.form['Titulo']
    avisos.Conteudo = request.form['Conteudo']
    avisos.DataInicial = request.form['DataInicial']
    avisos.DataFinal = request.form['DataFinal']
    avisos.Tipo = 4

    avisos.UserPostId = request.form['UserId']

    avisos.Status = request.form['Status']

    exec = avisos.insertAviso()

    logs = Logs()
    logs.logadorInfo("novo Aviso Cadastrado.")

    return redirect(url_for('Avisos.AvisosAdm', resultInsert=exec))

@bp_avisos.route('/EditAviso', methods=['POST'])   
@validaSessao
def EditAviso():

    valida = ValidaUser()

    retorno = valida.validaPermissao("avisos", session['tipo'])
        
    if retorno != True :  
        return redirect(url_for('home.index', msg="User_sem_Permissão"))  

    avisos = Avisos()

    avisos.id = request.form['Id']

    res = avisos.selectAvisoAdm()

    return render_template('avisosEdit.html', result=res )   

@bp_avisos.route('/UpdateAviso', methods=['POST'])   
@validaSessao
def UpdateAviso():

    valida = ValidaUser()

    retorno = valida.validaPermissao("avisos", session['tipo'])
        
    if retorno != True :  
        return redirect(url_for('home.index', msg="User_sem_Permissão"))  

    avisos = Avisos()

    avisos.id = request.form['Id']
    avisos.Titulo = request.form['Titulo']
    avisos.Conteudo = request.form['Conteudo']
    avisos.DataInicial = request.form['DataInicial']
    avisos.DataFinal = request.form['DataFinal']
    avisos.Tipo = 4
    avisos.UserPostId = request.form['UserId']
    avisos.Status = request.form['Status']

    exec = avisos.updateAviso()

    logs = Logs()
    logs.logadorInfo("Aviso Editado: " + avisos.id)


    return redirect(url_for('Avisos.AvisosAdm', resultInsert=exec ))



@bp_avisos.route('/DeleteAviso', methods=['POST'])
@validaSessao
def DeleteAviso():

    valida = ValidaUser()
    retorno = valida.validaPermissao("avisos", session['tipo'])
        
    if retorno != True :  
        return redirect(url_for('home.index', msg="User_sem_Permissão"))  

    avisos = Avisos()

    avisos.id = request.form['Id']

    exec = avisos.DeleteAviso()

    logs = Logs()
    logs.logadorInfo("Aviso Excluido: " + avisos.id)

    return redirect(url_for('Avisos.AvisosAdm', resultInsert=exec ))


