def menu(livro_service, leitor_service, emprestimo_service):
    while True:
        print('''1 - Cadastrar livro
2 - Cadastrar leitor
3 - Cadastrar empréstimo
4 - Listar livros
5 - Listar leitores
6 - Listar empréstimos
7 - Devolver empréstimo
0 - Sair

''')    
        try:
            opc = int(input('Digite sua opção: '))
        except ValueError:
            print('Digite um numero válido.')
            continue

        if opc == 1:

            livro = str(input('Qual livro você deseja cadastrar? '))
            livro_service.cadastrar_livro(livro)
            print('Cadastrado com sucesso.')

        elif opc == 2:
            leitor = str(input('Qual leitor você quer cadastrar? '))
            leitor_service.cadastrar_leitor(leitor)
            print('Cadastrado com sucesso.')
        
        elif opc == 3:
            id_livro = int(input('ID livro para cadastrar: '))
            id_leitor = int(input('ID leitor para cadastrar: '))
            emprestimo_service.cadastrar_emprestimo(id_livro, id_leitor)
            print('Cadastrado com sucesso.')

        elif opc == 4:
            livro_service.listar_livros()
        
        elif opc == 5:
            leitor_service.listar_leitores()
        
        elif opc == 6:
            emprestimo_service.listar_emprestimos()
        
        elif opc == 7:
            id_emprestimo = int(input('ID EMPRESTIMO PARA DEVOLVER: '))
            emprestimo_service.devolver_livro(id_emprestimo)

        elif opc == 0:
            print('Encerrando... Volte Sempre! ')
            break

        else:
            print('ERRO: Digite uma opção válida.')
            continue



