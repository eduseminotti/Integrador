from BancoDB import Banco

class Anuncios(object):

    def __init__(self, id=0, Titulo="", Conteudo="", DataInicial="",DataFinal="", Status="", UserNamePost="",        InsertDate="", imagem=""):
        self.info = {}
        self.id = id #0
        self.Titulo = Titulo #1
        self.Conteudo = Conteudo #2
        self.DataInicial = DataInicial #3 
        self.DataFinal = DataFinal #4
        self.Status = Status #5
        self.UserNamePost = UserNamePost #6
        self.InsertDate = InsertDate    #7
        self.imagem = imagem #8

    def selectAllAnunciosPublic(self):
        banco=Banco()
        try:
            c=banco.conexao.cursor() 
            c.execute("select id, post.titulo, post.insertdate ,"+
            "imagem = ( select top 1 img.image from dbo.Imagens as img where img.Post_ID = post.Id) "+
            "from dbo.post as post where post.tipo = 3 and post.Status = 1 order by post.insertdate desc") 
            result = c.fetchall()
            c.close()
            return result
        except:
            return "Ocorreu um erro na busca do Anuncio"    
            
    def selectAnunciosAdm(self):
        banco=Banco()
        try:
            c=banco.conexao.cursor()
            c.execute("SELECT [Id],[Titulo],[Conteudo],[DataInicial],[DataFinal],[Status]," + 
            "UserNamePost=(select usr.Nome from dbo.Users as usr where id = post.UserPostId) ,[insertdate] " +  
            "FROM [dbo].[Post] as post where tipo = 3"  )
            result = c.fetchall()
            c.close()
            return result
        except:
            return "Ocorreu um erro na busca do Anuncio"  

    