from flask import Blueprint, render_template , redirect , url_for , request ,session
from BancoDB import Banco
from Logs import Logs

class ValidaUser(object):

    def __init__(self, id=0, username="", password="", tipo=""):
        self.info = {}
        self.id = id
        self.username = username
        self.password = password
        self.tipo = tipo

    def validaUsuario(self, username, password):
        banco = Banco()
        logs = Logs()
        logs.logadorInfo("Buscando usaurio no base.")
        try:
            c=banco.conexao.cursor()
            c.execute("SELECT [id],[username] ,[password] , [tipo]  FROM [dbo].[users] where username = %s and "
                      "password = %s", (username, password))
            result = c.fetchall()
            c.close()

            return result
        except:
            logs.logadorInfo("Erro ao buscar usuario na base.")
            return None       

    def validaPermissao(self, entidade, tipo):
        
        #tipo = session['tipo']
        
        if entidade == "avisos":
            if tipo != 1 and tipo != 3:
                return False
            else:
                return True 
        
        if entidade == "Users":
            if tipo != 1:
                return False
            else:
                return True

        if entidade == "banners":
            if tipo != 1:
                return False
            else:
                return True

        if entidade == "noticias":
            if tipo != 1 and tipo != 2:
                return False
            else:
                return True





        return False



                    



