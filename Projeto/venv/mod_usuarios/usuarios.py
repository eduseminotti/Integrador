#coding: utf-8
from flask import Blueprint, render_template , redirect , url_for , request
from mod_login.login import validaSessao
from UsuariosDB import Usuarios

bp_usuarios = Blueprint('usuarios', __name__, url_prefix='/usuarios', template_folder='templates')

@bp_usuarios.route("/") 
@validaSessao
def index():

    user=Usuarios()
    
    res = user.selectUserALL()
    
    return render_template('usuarios_index.html', result=res ,content_type='application/json')


@bp_usuarios.route('/newuser')
@validaSessao
def usuarios_new():
    return render_template('usuarios_new.html')    



@bp_usuarios.route('/addUser', methods=['POST'])
@validaSessao
def addUser():

    user=Usuarios()

    user.Nome = request.form['Nome']
    user.Username = request.form['Username']
    user.Password = request.form['Password']
    user.tipo = request.form['tipo']
    user.email = request.form['Email']
    user.phone = request.form['Phone']

    exec = user.insertUser()

    return redirect(url_for('usuarios.index', resultInsert=exec))

@bp_usuarios.route('/edituser', methods=['POST'])   
@validaSessao
def edituser():

    user=Usuarios()

    user.id = request.form['id']

    res = user.selectUser()

    return render_template('usuarios_edit.html', result=res )   

@bp_usuarios.route('/UpdateUser', methods=['POST'])
@validaSessao
def UpdateUser():

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


@bp_usuarios.route('/deleteuser', methods=['POST'])
@validaSessao
def deleteuser():

    user=Usuarios()

    user.id = request.form['id']

    user.deleteUser()

    return redirect(url_for('usuarios.index'))