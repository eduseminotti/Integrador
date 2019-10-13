#coding: utf-8
from flask import Flask ,request , session, redirect , url_for
from datetime import timedelta

from mod_home.home import bp_home
from mod_login.login import bp_login
from mod_admin.admin import bp_admin
from mod_erro.erro import bp_erro
from mod_avisos.avisos import bp_avisos
from mod_anuncios.anuncios import bp_anuncios
from mod_noticias.noticias import bp_noticias
from mod_usuarios.usuarios import bp_usuarios

import os , sys
import pymssql

app = Flask(__name__)

app.register_blueprint(bp_home)
app.register_blueprint(bp_login)
app.register_blueprint(bp_admin)
app.register_blueprint(bp_erro)
app.register_blueprint(bp_avisos)
app.register_blueprint(bp_anuncios)
app.register_blueprint(bp_noticias)
app.register_blueprint(bp_usuarios)

app.secret_key = os.urandom(12).hex()


@app.before_request
def before_request():
    session.permanent = True
    app.permanent_session_lifetime = timedelta(minutes=30)


@app.errorhandler(404)
def nao_encontrado(error):
    return redirect(url_for('bp_erro.nao_encontrado'))

@app.errorhandler(500)
def problema_servidor(error):
    return redirect(url_for('bp_erro.problema_servidor'))


if __name__ == '__main__':
    app.run()