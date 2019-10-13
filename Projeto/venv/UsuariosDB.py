from BancoDB import Banco

class Usuarios(object):

    def __init__(self, id=0, Nome="",Username="", Password="",  tipo="" ,  email="" , phone=""):
        self.info = {}
        self.id = id
        self.Nome = Nome
        self.Username = Username 
        self.Password = Password
        self.tipo = tipo
        self.email = email
        self.phone = phone

    def selectUserALL(self):
        banco=Banco()
        try:
            c=banco.conexao.cursor()
            c.execute("SELECT  [id] ,[Nome],[UserName],password,[tipo],[email],[Phone] FROM [dbo].[Users]")
            result = c.fetchall()
            c.close()
            return result
        except:
            return "Ocorreu um erro na busca do usuário"

    def selectUser(self):
        banco=Banco()
        try:
            c=banco.conexao.cursor()
            c.execute("SELECT  [id] ,[Nome],[UserName],password,[tipo],[email],[Phone] FROM [dbo].[Users] where id =  %s" , (self.id))
            result = c.fetchall()
            c.close()
            return result
        except:
            return "Ocorreu um erro na busca do usuário"            

    def insertUser(self):

        banco = Banco()
        try:
            c = banco.conexao.cursor()
            c.execute("INSERT into [dbo].[Users] ( Nome , UserName , Password , tipo , email , phone) VALUES  (%s, %s, %s, %s, %s, %s)" , 
            (self.Nome, self.Username, self.Password, self.tipo , self.email , self.phone ))          
           
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