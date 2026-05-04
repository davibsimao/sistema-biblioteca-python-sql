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


