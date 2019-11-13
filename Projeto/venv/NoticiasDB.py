from BancoDB import Banco


class Noticias(object):


    def __init__(self, id=0, Titulo="", Conteudo="" , Tipo=2, Status="" , UserPostId="", InsertDate=""):
        self.info = {}
        self.id = id
        self.Titulo = Titulo
        self.Conteudo = Conteudo
        self.Tipo = Tipo
        self.Status = Status
        self.UserPostId = UserPostId
        self.InsertDate = InsertDate    

    def selectAllnoticiasAdm(self):
        banco=Banco()
        try:
            c=banco.conexao.cursor()
            c.execute("select id, titulo, cast (insertdate as date) from [dbo].[Post] as post where tipo = 2  order by insertdate desc")
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
            " from [dbo].[Post] as post where tipo = 2 and id = %s  order by insertdate desc" , (self.id ))
            result = c.fetchall()
            c.close()
            return result
        except:
            return "ERRO"              


    def addnoticia(self):
        banco=Banco()
        try:
            c = banco.conexao.cursor()
            c.execute("insert into Post (Titulo, Conteudo, Tipo,Status, UserPostId) values (%s, %s, %s, 1, %s  )",
                      (self.Titulo, self.Conteudo, self.Tipo ,self.UserPostId))
            banco.conexao.commit()

            result = Noticias.selectMaxIdPost(None)

            c.close()
            return result
        except:
            return "ERRO"

    def selectMaxIdPost(self):
        banco = Banco()
        try:
            c = banco.conexao.cursor()
            c.execute("select max(id) from Post")
            result = c.fetchall()

            c.close()

            for row in result:
                result = row[0]

            return result
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