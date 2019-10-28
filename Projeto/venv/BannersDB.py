from BancoDB import Banco

class Banners(object):

    def __init__(self, id=0, Titulo="", Conteudo="" , Tipo="", Status="" , UserPostId="", InsertDate=""):
        self.info = {}
        self.id = id
        self.Titulo = Titulo
        self.Conteudo = Conteudo
        self.Tipo = Tipo
        self.Status = Status
        self.UserPostId = UserPostId
        self.InsertDate = InsertDate    

    def selectAllBannersAdm(self):
        banco=Banco()
        try:
            c=banco.conexao.cursor()
            c.execute("select id, titulo, Status, Username=(select Nome from Users as usr where id = post.UserPostId)"+
            "from [dbo].[Post] as post where tipo = 1  order by insertdate desc")
            result = c.fetchall()
            c.close()
            return result
        except:
            return "erro"

    def selectbannerAdm(self):
        banco=Banco()
        try:
            c=banco.conexao.cursor()
            c.execute("select  id, titulo, Status ,conteudo,   imagem=(select top 1 img.image from dbo.Imagens as img where img.Post_ID = post.Id)"+
            " from [dbo].[Post] as post where tipo = 1 and id = %s  order by insertdate desc" , (self.id ))
            result = c.fetchall()
            c.close()
            return result
        except:
            return "ERRO"              

    def updateBanner(self):

        banco=Banco()
        try:

            c=banco.conexao.cursor()
            c.execute("update dbo.Post set Titulo = %s , Conteudo = %s  , Status = %s , userpostid = %s , insertdate=getdate() where id = %s",
            (self.Titulo, self.Conteudo , self.Status, self.UserPostId,  self.id)) 
            banco.conexao.commit()
            c.close()

            return "Aviso atualizado com sucesso!"
        except:
            return "ERRO" 
             
    def selectAllBanners(self):
        banco=Banco()
        try:
            c=banco.conexao.cursor()
            c.execute("select  titulo, CONTEUDO , cast (insertdate as date) ,imagem=(select top 1 img.image from dbo.Imagens as img where img.Post_ID = post.Id) "+
            "from [dbo].[Post] as post where tipo = 1 and status = 1  order by insertdate desc")
            result = c.fetchall()
            c.close()
            return result
        except:
            return "erro"