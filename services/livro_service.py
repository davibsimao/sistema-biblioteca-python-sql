from repositories.livro_repository import LivroRepository
from repositories.emprestimo_repository import EmprestimoRepository

class LivroService:
    def __init__(self, livro_repository,emprestimo_repository):
        self.livro_repository = livro_repository
        self.emprestimo_repository = emprestimo_repository
    

    def cadastrar_livro(self, titulo):
        if not titulo or titulo.strip() == '':
            print('ERRO: Campo "titulo" inválido.')
            return
        else:
            self.livro_repository.inserir_livro(titulo.strip())
    
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

    def listar_livros_disponiveis(self):
        livros = self.livro_repository.listar_livros_disponiveis()

        if not livros:
            print('Não há livros para mostrar')
            return
        else:
            print('-'*40)
            print(f'{"LISTA DE LIVROS DISPONIVEIS".center(40)}')
            print('-'*40)
            for livro in livros:
                print(f'id {livro[0]} | titulo: {livro[1]}')
            print('-'*40)
    
    def deletar_livro(self, idlivro):
        if idlivro <= 0:
            print('ERRO: ID inválido')
            return

        tem_emprestimo = self.emprestimo_repository.verificar_livro_com_emprestimo(idlivro)

        if tem_emprestimo:
            print('Não é possível deletar. Livro possui histórico de empréstimos.')
            return

        try:
            deletou = self.livro_repository.deletar_livro(idlivro)

            if deletou:
                print('Livro deletado com sucesso.')
            else:
                print('Livro não encontrado.')
        except Exception as e:
            print('Erro ao deletar livro:', e)