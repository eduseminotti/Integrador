#coding: utf-8
from flask import Blueprint, render_template, request, url_for, session, redirect 
from mod_login.login import validaSessao
from NoticiasDB import Noticias
from ImagensDB import Imagens
from ValidaUserDB import ValidaUser

import base64


bp_noticias = Blueprint('noticias', __name__, url_prefix='/noticias', template_folder='templates')

@bp_noticias.route('/')
def NoticiasIndex():
    return render_template("noticias.html"), 200


@bp_noticias.route('/listanoticias')
@validaSessao
def listanoticias():

    noticias = Noticias()

    news = noticias.selectAllnoticiasAdm()

    return render_template("listanoticias.html", news=news), 200


@bp_noticias.route('/novanoticia')
@validaSessao
def novanoticia():

    return render_template("novanoticia.html"), 200


@bp_noticias.route('/Addnoticia', methods=['POST'])
@validaSessao
def Addnoticia():

    noticias = Noticias()
    imagens = Imagens()

    noticias.Titulo = request.form['Titulo']
    noticias.Conteudo = request.form['Conteudo']
    noticias.UserPostId = session['id']

    imagens.Post_ID = noticias.addnoticia()

    imagens.imagem = "data:" + request.files['imagem'].content_type + ";base64," + str(
        base64.b64encode(request.files['imagem'].read()), "utf-8")

    imagens.InsertImagem()

    return redirect(url_for('noticias.listanoticias'))


@bp_noticias.route('/editanoticia', methods=['POST'])
@validaSessao
def editanoticia():

    noticias = Noticias()

    noticias.id = request.form['Id']

    news = noticias.selectnoticiaAdm()

    return render_template("editanoticia.html", news=news), 200


@bp_noticias.route('/Updatenoticia', methods=['POST'])
@validaSessao
def Updatenoticia():

    noticias = Noticias()
    imagens = Imagens()

    noticias.Titulo = request.form['Titulo']
    noticias.Conteudo = request.form['Conteudo']
    noticias.UserPostId = session['id']

    imagens.Post_ID = noticias.addnoticia()

    RmvImg = 'RemoveIMG' in request.form

    if RmvImg == "on" or RmvImg == True:
        imagens.DeleteImagem()
    else:
        imagens.imagem = "data:" + request.files['imagem'].content_type + ";base64," + str(
            base64.b64encode(request.files['imagem'].read()), "utf-8")

    imagens.InsertImagem()

    return redirect(url_for('noticias.listanoticias'))


@bp_noticias.route('/excluinoticia', methods=['POST'])
@validaSessao
def excluinoticia():

    return redirect(url_for('noticias.listanoticias'))



