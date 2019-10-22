import pymssql

class Banco():

    def __init__(self):
        host = "DESKTOP-L112HN3"
        user = "sa"
        password = "123456"
        db = "seminotti"
        self.conexao = pymssql.connect(host, user, password, db) 


        

