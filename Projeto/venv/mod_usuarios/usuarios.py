#coding: utf-8
from flask import Blueprint, render_template , redirect , url_for , request,session
from mod_login.login import validaSessao
from UsuariosDB import Usuarios
from ValidaUserDB import ValidaUser

bp_usuarios = Blueprint('usuarios', __name__, url_prefix='/usuarios', template_folder='templates')

@bp_usuarios.route("/") 
@validaSessao
def index():

    valida = ValidaUser()

    retorno = valida.validaPermissao("Users", session['tipo'])
        
    if retorno != True :  
        return redirect(url_for('home.index', msg="User_sem_Permissão"))  

    user=Usuarios()
    
    res = user.selectUserALL()
    
    return render_template('usuarios_index.html', result=res ,content_type='application/json')


@bp_usuarios.route('/newuser')
@validaSessao
def usuarios_new():

    valida = ValidaUser()

    retorno = valida.validaPermissao("Users", session['tipo'])
        
    if retorno != True :  
        return redirect(url_for('home.index', msg="User_sem_Permissão"))  

    return render_template('usuarios_new.html')    



@bp_usuarios.route('/addUser', methods=['POST'])
@validaSessao
def addUser():

    valida = ValidaUser()

    retorno = valida.validaPermissao("Users", session['tipo'])
        
    if retorno != True :  
        return redirect(url_for('home.index', msg="User_sem_Permissão"))  

    user=Usuarios()

    user.Nome = request.form['Nome'] 
    user.Username = request.form['Username']
    user.Password = request.form['Password']
    user.tipo = request.form['Tipo']
    user.email = request.form['Email']
    user.phone = request.form['Phone']

    exec = user.insertUser()

    return redirect(url_for('usuarios.index', resultInsert=exec))

@bp_usuarios.route('/edituser', methods=['POST'])   
@validaSessao
def edituser():

    valida = ValidaUser()

    retorno = valida.validaPermissao("Users", session['tipo'])
        
    if retorno != True :  
        return redirect(url_for('home.index', msg="User_sem_Permissão"))      

    user=Usuarios()

    user.id = request.form['id']

    res = user.selectUser()

    return render_template('usuarios_edit.html', result=res )   

@bp_usuarios.route('/UpdateUser', methods=['POST'])
@validaSessao
def UpdateUser():

    valida = ValidaUser()

    retorno = valida.validaPermissao("Users", session['tipo'])
        
    if retorno != True :  
        return redirect(url_for('home.index', msg="User_sem_Permissão"))      

    user=Usuarios()
    
    user.id = request.form['Id']
    user.Nome = request.form['Nome']
    user.Username = request.form['Username']
    user.Password = request.form['Password']
    user.tipo = request.form['tipo']
    user.email = request.form['Email']
    user.phone = request.form['Phone']

    exec = user.updateUser()

    return redirect(url_for('usuarios.index', resultUpdate=exec))

