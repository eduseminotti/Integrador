from BancoDB import Banco

class Imagens(object):

    def __init__(self, id=0, imagem="", Post_ID=0):
        self.info = {}
        self.id = id #0
        self.imagem = imagem 
        self.Post_ID = Post_ID

    def SelectImagensPost(self):
        banco=Banco()
        try:
            c=banco.conexao.cursor() 
            c.execute("SELECT Id,Image ,Insertdate,Post_ID FROM Imagens where Post_ID =  %s", (self.Post_ID ))
            result = c.fetchall()
            c.close()
            return result
        except:
            return "Ocorreu um erro na busca da Imagen" 

    def InsertImagem(self):
        banco=Banco()
        try:
            c=banco.conexao.cursor() 
            c.execute("insert into Imagens ( Image, Post_ID) values ( %s, %s )", (self.imagem, self.Post_ID ))

            banco.conexao.commit()     

            c.close()
            return "Imagem salva com sucesso"
        except:
            return "Ocorreu um erro na inserção da imagem"     

    def InsertImagem(self):
        banco=Banco()
        try:
            c=banco.conexao.cursor() 
            c.execute("insert into Imagens ( Image, Post_ID) values ( %s, %s )" , (self.imagem, self.Post_ID ))

            banco.conexao.commit()     

            c.close()
            return "Imagem salva com sucesso"
        except:
            return "Ocorreu um erro na inserção da imagem"        

    def UpdateImagem(self):
        banco=Banco()
        try:
            c=banco.conexao.cursor() 
            c.execute("update Imagens set Image= %s where post_id = %s" , (self.imagem, self.Post_ID ))

            banco.conexao.commit()     

            c.close()
            return "Imagem salva com sucesso"
        except:
            return "Ocorreu um erro na inserção da imagem" 

    def DeleteImagem(self):
        banco=Banco()
        try:
            c=banco.conexao.cursor() 
            c.execute("delete from Imagens where post_id = %s" , ( self.Post_ID ))

            banco.conexao.commit()     

            c.close()
            return "Imagem Removida com sucesso"
        except:
            return "Ocorreu um erro na remoção da imagem"                                  
                                   
            
  