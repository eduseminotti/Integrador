from flask import Blueprint, render_template , redirect , url_for , request ,session
from BancoDB import Banco

class ValidaUser(object):

    def __init__(self, id=0, username="", password="", tipo=""):
        self.info = {}
        self.id = id
        self.username = username
        self.password = password
        self.tipo = tipo

    def validaUsuario(self, username, password):
        banco=Banco()
        try:
            c=banco.conexao.cursor()
            c.execute("SELECT [id],[username] ,[password] , [tipo]  FROM [dbo].[users] where username = %s and password = %s", (username , password))
            result = c.fetchall()
            c.close()
            return result 
        except:
            return None       

    def validaPermissao(self, entidade, tipo):
        
        #tipo = session['tipo']
        
        if entidade == "avisos":
            if tipo != 1 and tipo != 3 : 
                return False
            else:
                return True 
        return False                



