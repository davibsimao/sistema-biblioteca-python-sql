from repositories.emprestimo_repository import EmprestimoRepository

class EmprestimoService:
    def __init__(self, emprestimo_repository, livro_repository, leitor_repository):
        self.emprestimo_repository = emprestimo_repository
        self.livro_repository = livro_repository
        self.leitor_repository = leitor_repository
    
    def cadastrar_emprestimo(self,id_livro, id_leitor):
        livro_encontrado = self.livro_repository.buscar_livro_id(id_livro)
        leitor_encontrado = self.leitor_repository.buscar_leitor_id(id_leitor)

        if leitor_encontrado and livro_encontrado:
            self.emprestimo_repository.inserir_emprestimo(id_livro, id_leitor)
            return
        else:
            print('ERRO: Dados não encontrados no banco de dados.')
            return
    
    def listar_emprestimos(self):
        emprestimos = self.emprestimo_repository.listar_emprestimos()
        if not emprestimos:
            print('Não há emprestimos para mostrar')
            return
        else:
            print('-'*40)
            print(f'{"LISTA DE EMPRESTIMOS".center(40)}')
            print('-'*40)
            for emprestimo in emprestimos:
                print(f'ID emprestimo: {emprestimo[0]} | Livro: {emprestimo[1]} | Leitor: {emprestimo[2]} |  STATUS: {emprestimo[5]}')

    def devolver_livro(self, idemprestimo):
        emprestimo = self.emprestimo_repository.buscar_emprestimo_id(idemprestimo)
    
        if not emprestimo:
            print('ERRO: ID inválido.')
            return
        
        if emprestimo[3] == 'DEVOLVIDO':  
            print('Livro já foi devolvido.')
            return

        self.emprestimo_repository.atualizar_status(idemprestimo)
        print('Status atualizado com sucesso.')