#coding: utf-8
from flask import Blueprint, render_template, request, url_for, session, redirect 

bp_erro = Blueprint('bp_erro', __name__, url_prefix='/erro', template_folder='templates')

@bp_erro.route('/404')
def nao_encontrado():
    return render_template("form404.html"), 404

@bp_erro.route('/500')
def problema_servidor():
    return render_template("form500.html"), 500
