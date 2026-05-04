from repositories.leitor_repository import LeitorRepository

class LeitorService:
    def __init__(self, leitor_repository):
        self.leitor_repository = leitor_repository

    def cadastrar_leitor(self, nome):
        if nome == '':
            print('ERRO: digite um nome válido.')
            return
        else:
            self.leitor_repository.inserir_leitor(nome)
        
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
        
