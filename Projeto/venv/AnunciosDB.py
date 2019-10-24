from BancoDB import Banco

class Anuncios(object):

    def __init__(self, id=0, Titulo="", Conteudo="", DataInicial="",DataFinal="", Status="", UserNamePost="", InsertDate="", imagem=""):
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
            c.execute("select id, post.titulo, cast(  post.insertdate as date)  ,"+
            "imagem = ( select top 1 img.image from dbo.Imagens as img where img.Post_ID = post.Id),cast (post.conteudo as varchar(60))"+
            "from dbo.post as post where post.tipo = 3 and post.Status = 1 order by post.insertdate desc") 
            result = c.fetchall()
            c.close()
            return result
        except:
            return "Ocorreu um erro na busca do Anuncio"    

    def selectSingleAnunciosPublic(self):
        banco=Banco()
        try:
            c=banco.conexao.cursor() 
            c.execute("select id, post.titulo, post.conteudo, username = (select Nome from Users where id = post.UserPostId),"+
            "cast(  post.insertdate as date) from dbo.post as post where  post.id = %s", (self.id ))
            result = c.fetchall()
            c.close()
            return result
        except:
            return "Ocorreu um erro na busca do Anuncio" 

    def relatedAnunciosPublic(self):
        banco=Banco()
        try:
            c=banco.conexao.cursor() 
            c.execute("select top 2 id, post.titulo, cast(  post.insertdate as date) "+
            ",imagem = ( select top 1 img.image from dbo.Imagens as img where img.Post_ID = post.Id) ,cast (post.conteudo as varchar(60)) "+
            "from dbo.post as post where post.tipo = 3 and post.Status = 1 and id <> %s order by post.insertdate desc" , (self.id ))
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
            "FROM [dbo].[Post] as post where tipo = 3 order by post.insertdate desc"  )
            result = c.fetchall()
            c.close()
            return result
        except:
            return "Ocorreu um erro na busca do Anuncio"  

    def insertAnuncio(self):

        banco = Banco()
        try:
            c = banco.conexao.cursor()
            c.execute(" insert into [dbo].[Post] ( Titulo , Conteudo , DataInicial , DataFinal , Tipo , Status , UserPostId )  VALUES  (%s, %s, %s, %s, %s, %s, %s)" , 
            (self.Titulo, self.Conteudo, self.DataInicial, self.DataFinal , self.Tipo , self.Status, self.UserPostId ))          
           
            banco.conexao.commit()
            c.close()

            return "Anuncio cadastrado com sucesso!"
        except:
            return "Ocorreu um erro na inserção do Anuncio"            

    