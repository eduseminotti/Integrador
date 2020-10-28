#coding: utf-8
from flask import Blueprint, render_template , redirect , url_for , request ,session
from mod_login.login import validaSessao
from BannersDB import Banners
from ValidaUserDB import ValidaUser
from ImagensDB import Imagens
from Logs import Logs

import base64

bp_Banners = Blueprint('Banners', __name__, url_prefix='/Banners', template_folder='templates')

@bp_Banners.route('/') 
@validaSessao
def BannersList():

    validauser = ValidaUser()

    retorno = validauser.validaPermissao("banners", session['tipo'])

    if retorno != True :
        return redirect(url_for('home.index', msg="User_sem_Permissão"))

    banners = Banners()

    result = banners.selectAllBannersAdm()
    
    return render_template("BannersList.html", result=result), 200

@bp_Banners.route('/BannersEdit', methods=['POST'])
@validaSessao
def BannersEdit():

    validauser = ValidaUser()

    retorno = validauser.validaPermissao("banners", session['tipo'])

    if retorno != True:
        return redirect(url_for('home.index', msg="User_sem_Permissão"))

    banners = Banners()

    banners.id = request.form['Id']
    
    result = banners.selectbannerAdm()


    return render_template('BannersEdit.html',result=result)     


def BannersEditOrUpdate():

    validauser = ValidaUser()

    retorno = validauser.validaPermissao("banners", session['tipo'])

    if retorno != True:
        return redirect(url_for('home.index', msg="User_sem_Permissão"))

    banners = Banners()

    banners.id = request.form['Id']
    
    result = banners.selectbannerAdm()


    return render_template('BannersEdit.html',result=result)     


@bp_Banners.route('/Updatebanner', methods=['POST'])   
@validaSessao
def Updatebanner():

    validauser = ValidaUser()

    retorno = validauser.validaPermissao("banners", session['tipo'])

    if retorno != True:
        return redirect(url_for('home.index', msg="User_sem_Permissão"))

    banners = Banners()
    imagens = Imagens()

    banners.id = request.form['Id']
    banners.Titulo = request.form['Titulo']
    banners.Conteudo = request.form['Conteudo']  
    banners.UserPostId = request.form['UserId']
    banners.Status = request.form['Status']
    
    imagens.imagem =  "data:" + request.files['imagem'].content_type + ";base64," + str(base64.b64encode( request.files['imagem'].read() ) , "utf-8")
    imagens.Post_ID = request.form['Id']

    banners.updatebanner()
    
    if imagens.imagem != "data:" + request.files['imagem'].content_type + ";base64," :
        imagens.UpdateImagem()

    logs = Logs()
    logs.logadorInfo("Banner Editado com sucesso: " + banners.id)

    return redirect(url_for('Banners.BannersList'))
