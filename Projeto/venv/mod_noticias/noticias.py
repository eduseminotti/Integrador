#coding: utf-8
from flask import Blueprint, render_template, request, url_for, session, redirect 
from mod_login.login import validaSessao
from NoticiasDB import Noticias
from ImagensDB import Imagens
from ValidaUserDB import ValidaUser
from Logs import Logs

import base64


bp_noticias = Blueprint('noticias', __name__, url_prefix='/noticias', template_folder='templates')

@bp_noticias.route('/')
def NoticiasIndex():

    noticia = Noticias()

    news = noticia.selectnoticiaspublic()

    return render_template("listanoticiasPublic.html", noticias=news), 200


@bp_noticias.route('/noticia', methods=['POST'])
def noticia():

    noticia = Noticias()

    noticia.id = request.form['id']

    news = noticia.selectnoticiapublic()

    related = noticia.noticiasrelacionadas()

    return render_template("noticiapublic.html", noticias=news, related=related), 200


@bp_noticias.route('/listanoticias')
@validaSessao
def listanoticias():

    valida = ValidaUser()
    retorno = valida.validaPermissao("noticias", session['tipo'])

    if retorno != True:
        return redirect(url_for('home.index', msg="User_sem_Permissão"))

    noticias = Noticias()

    news = noticias.selectAllnoticiasAdm()

    return render_template("listanoticias.html", news=news), 200


@bp_noticias.route('/novanoticia')
@validaSessao
def novanoticia():
    valida = ValidaUser()
    retorno = valida.validaPermissao("noticias", session['tipo'])

    if retorno != True:
        return redirect(url_for('home.index', msg="User_sem_Permissão"))

    return render_template("novanoticia.html"), 200


@bp_noticias.route('/Addnoticia', methods=['POST'])
@validaSessao
def Addnoticia():

    valida = ValidaUser()
    retorno = valida.validaPermissao("noticias", session['tipo'])

    if retorno != True:
        return redirect(url_for('home.index', msg="User_sem_Permissão"))

    noticias = Noticias()
    imagens = Imagens()

    noticias.Titulo = request.form['Titulo']
    noticias.Conteudo = request.form['Conteudo']
    noticias.UserPostId = session['id']
    noticias.DataInicial = request.form['DataInicial']
    noticias.DataFinal = request.form['DataFinal']

    imagens.Post_ID = noticias.addnoticia()

    imagens.imagem = "data:" + request.files['imagem'].content_type + ";base64," + str(
            base64.b64encode(request.files['imagem'].read()), "utf-8")

    if imagens.imagem == "data:application/octet-stream;base64,":
        imagens.imagem = None

    imagens.InsertImagem()

    logs = Logs()
    logs.logadorInfo("Nova noticia cadastrada.")

    return redirect(url_for('noticias.listanoticias'))


@bp_noticias.route('/editanoticia', methods=['POST'])
@validaSessao
def editanoticia():

    valida = ValidaUser()
    retorno = valida.validaPermissao("noticias", session['tipo'])

    if retorno != True:
        return redirect(url_for('home.index', msg="User_sem_Permissão"))

    noticias = Noticias()

    noticias.id = request.form['Id']

    news = noticias.selectnoticiaAdm()

    return render_template("editanoticia.html", news=news), 200


@bp_noticias.route('/Updatenoticia', methods=['POST'])
@validaSessao
def Updatenoticia():

    valida = ValidaUser()
    retorno = valida.validaPermissao("noticias", session['tipo'])

    if retorno != True:
        return redirect(url_for('home.index', msg="User_sem_Permissão"))

    noticias = Noticias()
    imagens = Imagens()

    noticias.id = request.form['PostId']
    imagens.Post_ID = noticias.id
    noticias.Titulo = request.form['Titulo']
    noticias.Conteudo = request.form['Conteudo']
    noticias.UserPostId = session['id']
    noticias.DataInicial = request.form['DataInicial']
    noticias.DataFinal = request.form['DataFinal']

    if 'imgoptions' in request.form:
        rmvimg = request.form['imgoptions']
    else:
        rmvimg = "nova"

    if rmvimg == "remove":
        imagens.nullImagem()

    elif rmvimg == "nova":
        imagens.imagem = "data:" + request.files['imagem'].content_type + ";base64," + str(
            base64.b64encode(request.files['imagem'].read()), "utf-8")
        imagens.UpdateImagem()

    noticias.updateNoticia()

    logs = Logs()
    logs.logadorInfo("Noticia Editada com sucesso: " + noticias.id)

    return redirect(url_for('noticias.listanoticias'))


@bp_noticias.route('/excluinoticia', methods=['POST'])
@validaSessao
def excluinoticia():

    valida = ValidaUser()
    retorno = valida.validaPermissao("noticias", session['tipo'])

    if retorno != True:
        return redirect(url_for('home.index', msg="User_sem_Permissão"))

    noticias = Noticias()
    imagens = Imagens()

    noticias.id = request.form['Id']
    imagens.Post_ID = noticias.id

    imagens.DeleteImagem()

    noticias.excluinoticia()

    logs = Logs()
    logs.logadorInfo("Noticia excluida com sucesso: " + noticias.id)

    return redirect(url_for('noticias.listanoticias'))



