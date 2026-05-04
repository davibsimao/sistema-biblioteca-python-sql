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