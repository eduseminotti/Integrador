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
            c.execute("select titulo, Conteudo, cast( DataInicial as date) as DataInicial  from dbo.post where tipo = 4 "+
            "and Status = 1 and DataInicial <= cast( getdate() as date)  and datafinal  >= cast( getdate() as date) ")
            result = c.fetchall()
            c.close()
            return result
        except:
            return "Ocorreu um erro na busca do Aviso"

    def selectAvisosALLAdm(self):
        banco=Banco()
        try:
            c=banco.conexao.cursor()
            c.execute("SELECT post.[Id],post.[Titulo],post.[Conteudo],post.[DataInicial],post.[DataFinal],post.[Tipo],post.[Status],"+
            "us.Nome,post.[insertdate]FROM [dbo].[Post] as post INNER join dbo.users as us on us.id = post.userpostid "+
            " where post.Tipo = 4 order by post.insertdate desc" )
            result = c.fetchall()
            c.close()
            return result
        except:
            return "Ocorreu um erro na busca dos avisos"     
            
    def selectAvisoAdm(self):
        banco=Banco()
        try:
            c=banco.conexao.cursor()
            c.execute("SELECT [Id],[Titulo],[Conteudo],[DataInicial],[DataFinal],[Status] FROM [dbo].[Post] where tipo = 4 and id = %s"
             , (self.id ))
            result = c.fetchall()
            c.close()
            return result
        except:
            return "Ocorreu um erro na busca do aviso"  

    def insertAviso(self):

        banco = Banco()
        try:
            c = banco.conexao.cursor()
            c.execute(" insert into [dbo].[Post] ( Titulo , Conteudo , DataInicial , DataFinal , Tipo , Status , UserPostId )  VALUES  (%s, %s, %s, %s, %s, %s, %s)" , 
            (self.Titulo, self.Conteudo, self.DataInicial, self.DataFinal , self.Tipo , self.Status, self.UserPostId ))          
           
            banco.conexao.commit()
            c.close()

            return "Aviso cadastrado com sucesso!"
        except:
            return "Ocorreu um erro na inserção do Aviso"

    def updateAviso(self):

        banco=Banco()
        try:

            c=banco.conexao.cursor()
            c.execute("update dbo.Post set Titulo = %s , Conteudo = %s , DataInicial = %s, DataFinal = %s , Status = %s , userpostid = %s where id = %s",
            (self.Titulo, self.Conteudo,self.DataInicial,self.DataFinal , self.Status, self.UserPostId,  self.id)) 
            banco.conexao.commit()
            c.close()

            return "Aviso atualizado com sucesso!"
        except:
            return "Ocorreu um erro na alteração do Aviso"    
    
    def DeleteAviso(self):

        banco=Banco()
        try:

            c=banco.conexao.cursor()
            c.execute("delete from dbo.post where id =  %s", (self.id)) 
            banco.conexao.commit()
            c.close()

            return "Aviso atualizado com sucesso!"
        except:
            return "Ocorreu um erro na alteração do Aviso"