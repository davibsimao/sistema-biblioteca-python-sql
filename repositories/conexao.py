import mysql.connector

def criar_conexao():
    conexao = mysql.connector.connect(host= 'localhost',
                                    user='root',
                                    password='mysql123',
                                    database='biblioteca',
                                    )
    return conexao
