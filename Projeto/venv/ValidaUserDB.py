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
        banco=Banco()

        log = Logs()
        log.LogadorInfo("Iniciando validação de usuario: " + username)      


        try:
            c=banco.conexao.cursor()
            c.execute("SELECT [id],[username] ,[password] , [tipo]  FROM [dbo].[users] where username = %s and password = %s", (username , password))
            result = c.fetchall()
            c.close()
            log.LogadorInfo("Usuario Validado." + username)
            return result 
        except:
            log.LogadorErro("Erro na validação do usuario: " + username)
            return None       

    def validaPermissao(self, entidade, tipo):
                
        if entidade == "avisos":
            if tipo != 1 and tipo != 3 : 
                return False
            else:
                return True 
        
        if entidade == "Users":
            if tipo != 1  : 
                return False
            else:
                return True 
        return False             



                    



