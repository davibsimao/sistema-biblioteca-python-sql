from repositories.leitor_repository import LeitorRepository
from repositories.emprestimo_repository import EmprestimoRepository

class LeitorService:
    def __init__(self, leitor_repository, emprestimo_repository):
        self.leitor_repository = leitor_repository
        self.emprestimo_repository = emprestimo_repository

    def cadastrar_leitor(self, nome):
        if not nome or nome.strip() == '':
            print('ERRO: digite um nome válido.')
            return
        elif len(nome.strip()) < 3:
            print('ERRO: nome muito curto')
            return
        else:
            self.leitor_repository.inserir_leitor(nome.strip())
            print('Leitor cadastrado com sucesso.')
        
    def listar_leitores(self):
        leitores = self.leitor_repository.listar_leitor()
        if not leitores:
            print('Não há leitor para mostrar')
            return
        else:
            print('-'*40)
            print(f'{"LISTA DE LEITORES".center(40)}')
            print('-'*40)
            for leitor in leitores:
                print(f'id {leitor[0]} | titulo: {leitor[1]}')
            print('-'*40)

    def deletar_leitor(self, idleitor):
        resultado = self.leitor_repository.deletar_leitor(idleitor)

        if resultado:
            print('Leitor deletado com sucesso.')
        else:
            print('Não foi possível deletar. Leitor possui histórico ou não existe.')