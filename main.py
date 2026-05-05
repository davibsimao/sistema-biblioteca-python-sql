from repositories import conexao
from repositories.livro_repository import LivroRepository
from repositories.leitor_repository import LeitorRepository
from repositories.emprestimo_repository import EmprestimoRepository

from services.livro_service import LivroService
from services.leitor_service import LeitorService
from services.emprestimo_service import EmprestimoService

from utils.menu import menu


conexao_criada = conexao.criar_conexao()

print('Sistema iniciado')

livro_repository = LivroRepository(conexao_criada)
leitor_repository = LeitorRepository(conexao_criada)
emprestimo_repository = EmprestimoRepository(conexao_criada)

livro_service = LivroService(livro_repository, emprestimo_repository)
leitor_service = LeitorService(leitor_repository, emprestimo_repository)
emprestimo_service = EmprestimoService(emprestimo_repository, livro_repository, leitor_repository)

menu(livro_service, leitor_service, emprestimo_service)
