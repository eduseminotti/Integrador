from BancoDB import Banco

class AnunciosPublic(object):

    def __init__(self, id=0, Titulo="", InsertDate="", imagem=""):
        self.info = {}
        self.id = id
        self.Titulo = Titulo
        self.imagem = imagem
        self.InsertDate = InsertDate    

    def selectAllAnunciosPublic(self):
        banco=Banco()
        try:
            c=banco.conexao.cursor() 
            c.execute("select id, post.titulo, post.insertdate ,"+
            "imagem = ( select top 1 img.image from dbo.Imagens as img where img.Post_ID = post.Id) "+
            "from dbo.post as post where post.tipo = 3  order by post.insertdate desc") 
            result = c.fetchall()
            c.close()
            return result
        except:
            return "Ocorreu um erro na busca do Anuncio"    
            
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

    