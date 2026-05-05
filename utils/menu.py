def menu(livro_service, leitor_service, emprestimo_service):
    while True:
        print('''1 - Cadastrar livro
2 - Cadastrar leitor
3 - Cadastrar empréstimo
4 - Listar livros
5 - Listar leitores
6 - Listar empréstimos
7 - Devolver empréstimo
8 - Remover Livro
9 - Remover Leitor
0 - Sair

''')    
        try:
            opc = int(input('Digite sua opção: '))

        except ValueError:
            print('Digite um numero válido.')
            continue

        if opc == 1:
            
            livro = input('Qual livro você deseja cadastrar? ')
            
            livro_service.cadastrar_livro(livro)
            print('Cadastrado com sucesso.')

        elif opc == 2:

            leitor = input('Qual leitor você quer cadastrar? ')

            leitor_service.cadastrar_leitor(leitor)
            print('Cadastrado com sucesso.')
        
        elif opc == 3:

            try:
                id_livro = int(input('ID livro para cadastrar: '))
                id_leitor = int(input('ID leitor para cadastrar: '))
                
            except ValueError:
                print('ERRO: IDs devem ser números.')
                continue

            emprestimo_service.cadastrar_emprestimo(id_livro, id_leitor)
            print('Cadastrado com sucesso.')

        elif opc == 4:

            try:
                sub = int(input('1 - Todos | 2 - Disponíveis: '))

            except ValueError:
                print('Digite um número válido.')
                continue

            if sub == 1:
                livro_service.listar_livros()

            elif sub == 2:
                livro_service.listar_livros_disponiveis()
        
        elif opc == 5:
            leitor_service.listar_leitores()
        
        elif opc == 6:
            emprestimo_service.listar_emprestimos()
        
        elif opc == 7:

            try:
                id_emprestimo = int(input('ID EMPRESTIMO PARA DEVOLVER: '))
            except ValueError:
                print('Digite um ID emprestimo válido.')
                continue

            emprestimo_service.devolver_livro(id_emprestimo)

        elif opc == 8:

            try:
                idlivro = int(input('ID livro que deseja remover: '))

            except ValueError:
                print('Digite um ID Livro válido.')
                continue

            livro_service.deletar_livro(idlivro)
        
        elif opc == 9:
            try:
                idleitor = int(input('ID Leitor que deseja remover: '))

            except ValueError:
                print('Digite um ID Leitor válido.')
                continue

            leitor_service.deletar_leitor(idleitor)

        elif opc == 0:
            print('Encerrando... Volte Sempre! ')
            break

        else:
            print('ERRO: Digite uma opção válida.')
            continue



