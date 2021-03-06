#coding: utf-8
from flask import Blueprint, render_template , redirect , url_for , request ,session
from mod_login.login import validaSessao
from AnunciosDB import Anuncios
from ValidaUserDB import ValidaUser
from ImagensDB import Imagens
from Logs import Logs

import base64

bp_anuncios = Blueprint('Anuncios', __name__, url_prefix='/anuncios', template_folder='templates')

@bp_anuncios.route('/')
def index(): 


    anuncios = Anuncios()

    result = anuncios.selectAllAnunciosPublic()
        
    return render_template("AllAnunciosPublic.html", result=result), 200 

@bp_anuncios.route('/SingleAnuncio',methods=['POST'])
def SingleAnuncio():

    anuncios = Anuncios()
    imagens = Imagens()

    anuncios.id = request.form['Id']
    imagens.Post_ID = request.form['Id']

    related = anuncios.relatedAnunciosPublic()

    anuncio = anuncios.selectSingleAnuncioPublic()
    
    imagens = imagens.SelectImagensPost()

    return render_template("SingleAnuncioPublic.html", anuncio=anuncio, related=related, imagens=imagens), 200 

@bp_anuncios.route('/AllAnunciosAdm')
@validaSessao
def AllAnunciosAdm():
    
    anuncios = Anuncios()

    if session['tipo'] == 4:
        result = anuncios.selectAnunciosAdmTp4(session['id'])
    else:    
        result = anuncios.selectAnunciosAdm()
        
    return render_template("AllAnunciosAdm.html", result=result), 200 

@bp_anuncios.route('/AnunciosNew')
@validaSessao
def AnunciosNew():
    return render_template('AnunciosNew.html') 

@bp_anuncios.route('/AddAnuncio', methods=['POST'])
@validaSessao
def AddAnuncio():

    anuncios = Anuncios()
    imagens = Imagens()
    logs = Logs()

    anuncios.Titulo = request.form['Titulo']
    anuncios.Conteudo = request.form['Conteudo']
    anuncios.DataInicial = request.form['DataInicial']
    anuncios.DataFinal = request.form['DataFinal']
    anuncios.Status = request.form['Status']
    anuncios.Tipo = 3

    anuncios.UserPostId = session['id'] 

    imagens.imagem = "data:" + request.files['imagem'].content_type + ";base64," + str(base64.b64encode( request.files['imagem'].read() ) , "utf-8")

    imagens.Post_ID = anuncios.insertAnuncio()

    if imagens.imagem == "data:application/octet-stream;base64,":
        imagens.imagem = None

    imagens.InsertImagem()
    logs.logadorInfo("Novo anuncio Criado")
    return redirect(url_for('Anuncios.AllAnunciosAdm' ))
    
@bp_anuncios.route('/EditAnuncio', methods=['POST'])
@validaSessao
def EditAnuncio():
    
    anuncios = Anuncios()

    anuncios.id = request.form['Id']

    anuncio = anuncios.selectSingleAnuncioAdm()

    return render_template('AnunciosEdit.html', anuncio=anuncio) 


@bp_anuncios.route('/UpdateAnuncio', methods=['POST'])
@validaSessao
def UpdateAnuncio():

    anuncios = Anuncios()
    imagens = Imagens()
    logs = Logs()

    imagens.Post_ID = request.form['Id']
    anuncios.id = request.form['Id']
    anuncios.Titulo = request.form['Titulo']
    anuncios.Conteudo = request.form['Conteudo']
    anuncios.DataInicial = request.form['DataInicial']
    anuncios.DataFinal = request.form['DataFinal']
    anuncios.Status = request.form['Status']
    anuncios.Tipo = 3

    anuncios.UserPostId = session['id'] 

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
    anc = anuncios.updateAnuncio()



    logs.logadorInfo("anuncio Editado  " + anuncios.id)

    return redirect(url_for('Anuncios.AllAnunciosAdm' ))


@bp_anuncios.route('/ExcluiAnuncio', methods=['POST'])
@validaSessao
def ExcluiAnuncio():
    
    anuncios = Anuncios()
    imagens = Imagens()
    logs = Logs()
    
    anuncios.id = request.form['Id']
    imagens.Post_ID = request.form['Id']

    imagens.DeleteImagem()

    anuncios.DeletePost()

    logs.logadorInfo("anuncio Deletado  " + anuncios.id)

    return redirect(url_for('Anuncios.AllAnunciosAdm'))

