from repositories.livro_repository import LivroRepository

class LivroService:
    def __init__(self, livro_repository):
        self.livro_repository = livro_repository

    def cadastrar_livro(self, titulo):
        if titulo == '':
            print('ERRO: Campo "titulo" inválido.')
            return
        else:
            self.livro_repository.inserir_livro(titulo)
    
    def listar_livros(self):
        livros = self.livro_repository.listar_livros()
        if not livros:
            print('Não há livros para mostrar')
            return
        else:
            print('-'*40)
            print(f'{"LISTA DE LIVROS".center(40)}')
            print('-'*40)
            for livro in livros:
                print(f'id {livro[0]} | titulo: {livro[1]}')
            print('-'*40)