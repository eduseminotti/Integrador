import pymssql

class Banco():

    def __init__(self):
        host = "demotmsql\demonstracao"
        user = "sa"
        password = "P@ssw0rd!"
        db = "Seminotti_Teste"
        self.conexao = pymssql.connect(host, user, password, db)


        

