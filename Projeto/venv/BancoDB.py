import pymssql

class Banco():

    def __init__(self):
        host = "localhost"
        user = "sa"
        password = "123456"
        db = "seminotti"
        self.conexao = pymssql.connect(host, user, password, db)


        

