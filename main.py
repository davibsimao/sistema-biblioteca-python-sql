from repositories import conexao
from repositories.livro_repository import LivroRepository
from services.livro_service import LivroService
from repositories.leitor_repository import LeitorRepository
from services.leitor_service import LeitorService
from services.emprestimo_service import EmprestimoService
from repositories.emprestimo_repository import EmprestimoRepository


conexao_criada = conexao.criar_conexao()

print('Vou testar a conexao')


# TESTE LIVRO REPOSITORY

#l1 = LivroRepository(conexao_criada)
#buscar_livro = l1.buscar_livro_id(6)
#for livro in buscar_livro:
    #print(livro)


#service = LivroService(l1)
#service.cadastrar_livro('')



# TESTE LEITOR REPOSITORY

#leitor1 = LeitorRepository(conexao_criada)
#buscar_leitor = leitor1.buscar_leitor_id(2)
#for leitor in buscar_leitor:
 #  print(leitor)


#serviceleitor = LeitorService(leitor1)
#serviceleitor.cadastrar_leitor('')


# TESTE EMPRESTIMO REPOSITORY

emprestimo1 = EmprestimoRepository(conexao_criada)
l1 = LivroRepository(conexao_criada)
leitor1 = LeitorRepository(conexao_criada)

emprestimo_service = EmprestimoService(emprestimo1, l1, leitor1)
emprestimo_service.cadastrar_emprestimo(6, 4200)




