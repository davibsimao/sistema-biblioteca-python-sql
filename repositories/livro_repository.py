class LivroRepository:
    def __init__(self, conexao):
        self.conexao = conexao

    def inserir_livro(self, titulo):
        cursor = self.conexao.cursor()

        comando = 'INSERT INTO livros (titulo) VALUES (%s)'
        cursor.execute(comando, (titulo,))

        self.conexao.commit()
    
    def listar_livros(self):
        cursor = self.conexao.cursor()
        comando = 'SELECT IDLIVRO, TITULO FROM LIVROS'
        cursor.execute(comando)
        resultado = cursor.fetchall()

        return resultado
    
    def buscar_livro_id (self, idlivro):
        cursor = self.conexao.cursor()
        comando = 'SELECT IDLIVRO, TITULO FROM LIVROS WHERE IDLIVRO = %s'
        cursor.execute(comando, (idlivro,))
        resultado = cursor.fetchone()

        return resultado
    
    def listar_livros_disponiveis(self):
        cursor = self.conexao.cursor()
        comando = "SELECT IDLIVRO, TITULO FROM LIVROS WHERE IDLIVRO NOT IN (SELECT ID_LIVRO FROM EMPRESTIMOS WHERE STATUS = 'ATIVO')"
        cursor.execute(comando)
        resultado = cursor.fetchall()

        return resultado
    
    def deletar_livro(self, idlivro):
        cursor = self.conexao.cursor()
        comando = 'DELETE FROM LIVROS WHERE IDLIVRO = %s'
        cursor.execute(comando,(idlivro,))

        deletou = cursor.rowcount

        self.conexao.commit()

        return deletou > 0
    


        