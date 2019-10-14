from BancoDB import Banco

class Avisos(object):

    def __init__(self, id=0, Titulo="", DataInicial="",  DataFinal="" ,Conteudo="" , Tipo="", Status="" , UserPostId="", InsertDate=""):
        self.info = {}
        self.id = id
        self.Titulo = Titulo
        self.Conteudo = Conteudo
        self.DataInicial = DataInicial 
        self.DataFinal = DataFinal
        self.Tipo = Tipo
        self.Status = Status
        self.UserPostId = UserPostId
        self.InsertDate = InsertDate

    def selectAvisosALL(self):
        banco=Banco()
        try:
            c=banco.conexao.cursor()
            c.execute("SELECT  [id] ,[Nome],[UserName],password,[tipo],[email],[Phone] FROM [dbo].[Users]")
            result = c.fetchall()
            c.close()
            return result
        except:
            return "Ocorreu um erro na busca do usuário"

    def selectAvisosALLAdm(self):
        banco=Banco()
        try:
            c=banco.conexao.cursor()
            c.execute("SELECT [Id],[Titulo],[Conteudo],[DataInicial],[DataFinal],[Tipo],[Status],[UserPostId],[insertdate]FROM [dbo].[Post]" )
            result = c.fetchall()
            c.close()
            return result
        except:
            return "Ocorreu um erro na busca dos avisos"            

    def insertAviso(self):

        banco = Banco()
        try:
            c = banco.conexao.cursor()
            c.execute(" insert into [dbo].[Post] ( Titulo , Conteudo , DataInicial , DataFinal , Tipo , Status , UserPostId )  VALUES  (%s, %s, %s, %s, %s, %s)" , 
            (self.Titulo, self.Conteudo, self.DataInicial, self.DataFinal , self.Tipo , self.Status, self.UserPostId ))          
           
            banco.conexao.commit()
            c.close()

            return "Usuário cadastrado com sucesso!"
        except:
            return "Ocorreu um erro na inserção do usuário"

    def updateUser(self):

        banco=Banco()
        try:

            c=banco.conexao.cursor()
            c.execute("update [dbo].[Users] set Nome=%s,Username=%s,Password = %s, tipo = %s, email = %s , phone = %s where id = %s",(self.Nome, self.Username,self.Password,self.tipo,self.email,self.phone, self.id)) 
            banco.conexao.commit()
            c.close()

            return "Usuário atualizado com sucesso!"
        except:
            return "Ocorreu um erro na alteração do usuário"
    
    
    # def deleteUser(self):

    #     banco=Banco()
    #     try:

    #         c=banco.conexao.cursor()
    #         c.execute("delete from dbo.Users where id =  %s" , (self.id))
    #         banco.conexao.commit()
    #         c.close()

    #         return "Usuário excluído com sucesso!"
    #     except:
    #         return "Ocorreu um erro na exclusão do usuário"   