from BancoDB import Banco

class Admin(object):

    def __init__(self, Nome="", Phone="",Email=""):
        self.info = {}
        self.Nome = Nome
        self.Phone = Phone 
        self.Email = Email


    def anunciospendentes(self):
        banco=Banco()
        try:
            c=banco.conexao.cursor()
            c.execute("SELECT count(*) FROM [dbo].[Post] where tipo = 3 and Status = 0")
            result = c.fetchall()
            c.close()
            return result
        except:
            return "ERRO"

    def anunciosaprovados(self):
        banco=Banco()
        try:
            c=banco.conexao.cursor()
            c.execute("SELECT count(*) FROM [dbo].[Post] where tipo = 3 and Status = 3")
            result = c.fetchall()
            c.close()
            return result
        except:
            return "ERRO"            


  