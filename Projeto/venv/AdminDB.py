from BancoDB import Banco

class Admin(object):

    def __init__(self, Nome="", Phone="",Email=""):
        self.info = {}
        self.Nome = Nome
        self.Phone = Phone 
        self.Email = Email


    def selectConfig(self):
        banco=Banco()
        try:
            c=banco.conexao.cursor()
            c.execute("SELECT [Nome] ,[Phone] ,[Email] FROM [dbo].[Configuracoes]")
            result = c.fetchall()
            c.close()
            return result
        except:
            return "Ocorreu um erro na busca das configurações"

    def updateConfig(self):

        banco=Banco()
        try:

            c=banco.conexao.cursor()
            c.execute("update [dbo].[Configuracoes] set Nome = %s , phone = %s, Email = %s ",
            (self.Nome, self.Phone,self.Email)) 
            banco.conexao.commit()
            c.close()

            return "configuração atualizado com sucesso!"
        except:
            return "Ocorreu um erro na alteração da configuração"                

  