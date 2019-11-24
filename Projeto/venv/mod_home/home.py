#coding: utf-8
from flask import Blueprint, render_template, request, session, redirect , url_for
from BannersDB import Banners
from NoticiasDB import Noticias
from AvisosDB import Avisos
from Logs import Logs


bp_home = Blueprint('home', __name__, url_prefix='/', template_folder='templates')


@bp_home.route("/")
def index():
    logs = Logs()
    logs.logadorInfo("iniciando carregamento da tela inicial")
    banners = Banners()
    noticias = Noticias()
    avisos = Avisos()

    banners = banners.selectAllBanners()
    principal = noticias.selectTop1noticiaspublic()
    top6 = noticias.selectTop6noticiaspublic()
    avisos = avisos.selecttop6Avisos()

    logs.logadorInfo("tela inicial carregada")


    return render_template('home_index.html', banners=banners, principal=principal, top6=top6, avisos=avisos)






