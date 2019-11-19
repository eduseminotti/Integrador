from BancoDB import Banco


class Noticias(object):

    def __init__(self, id=0, Titulo="", Conteudo="", Tipo=2, Status="", UserPostId="", InsertDate=""):
        self.info = {}
        self.id = id
        self.Titulo = Titulo
        self.Conteudo = Conteudo
        self.Tipo = Tipo
        self.Status = Status
        self.UserPostId = UserPostId
        self.InsertDate = InsertDate

    def selectAllnoticiasAdm(self):
        banco = Banco()
        try:
            c = banco.conexao.cursor()
            c.execute("select id, titulo, cast (insertdate as date) from [dbo].[Post] as post where tipo = 2  order "
                      "by insertdate desc")
            result = c.fetchall()
            c.close()
            return result
        except:
            return "erro"

    def selectTop6noticiaspublic(self):
        banco = Banco()
        try:
            c = banco.conexao.cursor()
            c.execute("select  id, cast (titulo as varchar (90)), CAST (Post.Conteudo AS varchar (120)) , "
                      "cast (insertdate as date), "
                      "userpost = (select Nome from Users where id = post.UserPostId ) ,Image = (select Imagens.Image "
                      "from Imagens  where Post_ID = post.id ) from [dbo].[Post] as post where tipo = 2  order by "
                      "Insertdate desc OFFSET 1 ROWS FETCH NEXT 6 ROWS ONLY")
            result = c.fetchall()
            c.close()
            return result
        except:
            return "erro"

    def selectTop1noticiaspublic(self):
        banco = Banco()
        try:
            c = banco.conexao.cursor()
            c.execute("select  top 1 id, cast(titulo as varchar(60)), CAST (Post.Conteudo AS varchar (250)) ,"
                      "cast (insertdate as date) , userpost = (select Nome from Users where id = post.UserPostId) , "
                      "image = (select Image from Imagens where Post_ID = post.id ) from [dbo].[Post] as post where "
                      "tipo = 2 order by Insertdate desc  ")
            result = c.fetchall()
            c.close()
            return result
        except:
            return "erro"

    def noticiasrelacionadas(self):
        banco = Banco()
        try:
            c = banco.conexao.cursor()
            c.execute("select  top 4 id, cast(titulo as varchar(60)), CAST (Post.Conteudo AS varchar (250)) ,"
                      "cast (insertdate as date) , userpost = (select Nome from Users where id = post.UserPostId) , "
                      "image = (select Image from Imagens where Post_ID = post.id ) from [dbo].[Post] as post where "
                      "tipo = 2 and id <> %s order by Insertdate desc  ", (self.id))
            result = c.fetchall()
            c.close()
            return result
        except:
            return "erro"

    def selectnoticiaspublic(self):
        banco = Banco()
        try:
            c = banco.conexao.cursor()
            c.execute("select  id, cast(titulo as varchar(60)), CAST (Post.Conteudo AS varchar (250)) ,"
                      "cast (insertdate as date) , userpost = (select Nome from Users where id = post.UserPostId) , "
                      "image = (select Image from Imagens where Post_ID = post.id ) from [dbo].[Post] as post where "
                      "tipo = 2  order by Insertdate desc  ")
            result = c.fetchall()
            c.close()
            return result
        except:
            return "erro"

    def selectnoticiapublic(self):
        banco = Banco()
        try:
            c = banco.conexao.cursor()
            c.execute(
                "select  id, titulo, conteudo, imagem=(select top 1 img.image from dbo.Imagens as img where img.Post_ID = post.Id)," +
                "cast(insertdate as date) , username = (select nome from users where id = post.userpostid) from [dbo].[Post] as post where id = %s  ", (self.id))
            result = c.fetchall()
            c.close()
            return result
        except:
            return "ERRO"

    def selectnoticiaAdm(self):
        banco = Banco()
        try:
            c = banco.conexao.cursor()
            c.execute(
                "select  id, titulo, conteudo, imagem=(select top 1 img.image from dbo.Imagens as img where img.Post_ID = post.Id)" +
                " from [dbo].[Post] as post where tipo = 2 and id = %s  order by insertdate desc", (self.id))
            result = c.fetchall()
            c.close()
            return result
        except:
            return "ERRO"

    def addnoticia(self):
        banco = Banco()
        try:
            c = banco.conexao.cursor()
            c.execute("insert into Post (Titulo, Conteudo, Tipo,Status, UserPostId) values (%s, %s, %s, 1, %s  )",
                      (self.Titulo, self.Conteudo, self.Tipo, self.UserPostId))
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

    def excluinoticia(self):
        banco = Banco()
        try:
            c = banco.conexao.cursor()
            c.execute("delete from Post where id = %s", (self.id))
            banco.conexao.commit()
            c.close()
            return "Excluida"
        except:
            return "erro"

    def updateNoticia(self):

        banco = Banco()
        try:
            c = banco.conexao.cursor()
            c.execute(
                "update post set Titulo = %s, Conteudo = %s, UserPostId = %s, insertdate = getdate()  where id = %s ",
                (self.Titulo, self.Conteudo, self.UserPostId, self.id))

            banco.conexao.commit()

            c.close()

            return "update ok"
        except:
            return "Ocorreu um erro na edição do Anuncio"
