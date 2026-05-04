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

        self.conexao.commit()

        return resultado
    
    def buscar_livro_id (self, idlivro):
        cursor = self.conexao.cursor()
        comando = 'SELECT IDLIVRO, TITULO FROM LIVROS WHERE IDLIVRO = %s'
        cursor.execute(comando, (idlivro,))
        resultado = cursor.fetchone()

        self.conexao.commit()

        return resultado