class LeitorRepository:
    def __init__(self, conexao):
        self.conexao = conexao
    
    def inserir_leitor(self, leitor):
        cursor = self.conexao.cursor()
        comando = 'INSERT INTO leitores (NOME) VALUES (%s)'
        cursor.execute(comando, (leitor,))

        self.conexao.commit()

    def listar_leitor(self):
        cursor = self.conexao.cursor()
        comando = 'SELECT IDLEITOR, NOME FROM LEITORES '
        cursor.execute(comando)
        resultado = cursor.fetchall()

        return resultado

    def buscar_leitor_id(self, idleitor):
        cursor = self.conexao.cursor()
        comando = 'SELECT IDLEITOR, NOME FROM LEITORES WHERE IDLEITOR = %s'
        cursor.execute(comando, (idleitor,))
        resultado = cursor.fetchone()

        return resultado