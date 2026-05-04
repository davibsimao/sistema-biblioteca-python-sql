class EmprestimoRepository:
    def __init__(self, conexao):
        self.conexao = conexao
    
    def inserir_emprestimo(self, id_livro, id_leitor):
        cursor = self.conexao.cursor()
        comando = 'INSERT INTO emprestimos (ID_LIVRO, ID_LEITOR) VALUES (%s,%s)'
        valores = (id_livro, id_leitor)
        cursor.execute(comando, valores)
        
        self.conexao.commit()

    def listar_emprestimos(self):
        cursor = self.conexao.cursor()
        comando = '''
        SELECT E.IDEMPRESTIMO,LI.TITULO, LE.NOME, E.ID_LIVRO, E.ID_LEITOR , STATUS
        FROM EMPRESTIMOS E
        INNER JOIN LIVROS LI
        ON E.ID_LIVRO = LI.IDLIVRO
        INNER JOIN LEITORES LE 
        ON E.ID_LEITOR = LE.IDLEITOR
        '''
        cursor.execute(comando)
        resultado = cursor.fetchall()

        return resultado
    
    def buscar_emprestimo_id(self, idemprestimo):
        cursor = self.conexao.cursor()
        comando = 'SELECT IDEMPRESTIMO, ID_LIVRO, ID_LEITOR, STATUS FROM EMPRESTIMOS WHERE IDEMPRESTIMO = %s'
        cursor.execute(comando,(idemprestimo,))
        resultado = cursor.fetchone()

        return resultado
    
    def atualizar_status(self, idemprestimo):
        cursor = self.conexao.cursor()
        comando = 'UPDATE EMPRESTIMOS SET STATUS = %s WHERE IDEMPRESTIMO = %s'
        valores = ('DEVOLVIDO',idemprestimo)
        cursor.execute(comando, valores)

        self.conexao.commit()