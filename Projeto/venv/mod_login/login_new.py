# coding: utf-8
from flask import Blueprint, render_template, request, session, redirect, url_for
from functools import wraps
from ValidaUserDB import ValidaUser
from Logs import Logs

bp_login = Blueprint('login', __name__, url_prefix='/login', template_folder='templates')


@bp_login.route("/")
def index():
    return render_template('login.html')


@bp_login.route("/btnlogin", methods=['POST'])
def btnlogin():
    logs = Logs()
    validauser = ValidaUser()

    logs.logadorInfo("iniciando login")

    user = request.form.get('user')
    password = request.form.get('pass')

    userBanco = validauser.validaUsuario(user, password)

    userNameDB = 0
    passwordDB = 0
    tipo = 0

    if userBanco != None and userBanco != "":
        for row in userBanco:
            id = row[0]
            userNameDB = row[1]
            passwordDB = row[2]
            tipo = row[3]
        # Usuario correto
        if user == userNameDB and password == passwordDB:
            session.clear()
            session['user'] = userNameDB
            session['tipo'] = tipo
            session['id'] = id

            logs.logadorInfo("Login realizado para o usuario: " + user)

            return redirect(url_for('admin.index'))
        # user errado
        else:
            logs.logadorInfo("Login nao realizado, Login ou senha incorretos para o usuario: " + user)
            return redirect(url_for('login.index', userIncorrect=1))
    else:
        logs.logadorInfo("Usuario nao encontrado: " + userNameDB )
        return redirect(url_for('login.index', userIncorrect=1, userdb=userNameDB, passwordDB=passwordDB, user=user,
                                password=password))


@bp_login.route("/btnlogout", methods=['GET', 'POST'])
def btnlogout():
    logs = Logs()

    logs.logadorInfo("Logout do usuario: " + session['user'])
    session.pop('user', None)
    session.clear()
    return redirect(url_for('home.index'))


def validaSessao(f):
    @wraps(f)
    def decorated_function(*args, **kwargs):
        if 'user' not in session:
            return redirect(url_for('login.index', falhaSessao=1))
        else:
            return f(*args, **kwargs)

    return decorated_function
