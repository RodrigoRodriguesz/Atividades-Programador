
from classconexao import Conexao
con = Conexao(dbname= "Locadora", host = "Localhost", port = "5432", user = "postgres", password = "postgres")
# ------------------------------------------------------------------

def cadastrarCliente():
    nome = input(f"Digite seu Nome:")
    cpf = input(f"Digite seu CPF :")
    username = input(f"Digite seu Username :")
    senha = input (f"Digite uma senha:")

    con.manipularBanco(f'''Insert into "Login" ("ID_Cliente", "Nome", "CPF","Nome_Usuario","Senha")
    Values(default,'{nome}','{cpf}','{username}','{senha}')

    ''')

def cadastrarFilmes():
    cine = input(f"Digite nome do filme: ")
    tipo = input(f"Digite o tipo do filme:")
    con.manipularBanco(f'''
    Insert Into "Filmes
    Values(defalt , '{cine}', '{tipo}' )

    ''')

    # nome = input(f"Digite seu Nome:")
    # cpf = input(f"Digite seu CPF :")
    # username = input(f"Digite seu Username :")
    # senha = input (f"Digite uma senha:")

    # con.manipularBanco(f'''Insert into "Login" ("ID_Cliente", "Nome", "CPF","Nome_Usuario","Senha")
    # Values(default,'{nome}','{cpf}','{username}','{senha}')

    # ''')

def VerFilmesAlugados():
    pass

def VerClientes():
    ListaClientes = con.consultarBanco('''
    SELECT * FROM "Login"
    ORDER BY "Nome_Usuario" ASC

    ''')
    if ListaClientes:
            print("Seus Dados : ")
            for Dados in ListaClientes:
                print(f'''

            ID - {Dados[0]} 

            Nome - {Dados[1]}

            User - {Dados[2]}

            Sua senha - {Dados[3]}

            CPF - {Dados[4]}

            ''')
    else:
        print("Ocorreu um erro inesperado!!")

def VerFilmes():
    listafilmes=con.consultarBanco('''
    SELECT * FROM public."Filmes"
    ORDER BY "Nome" ASC 
''')
    if listafilmes :
        print("Filmes Disponiveis:")
        for fil in listafilmes:
            print(f'''
            ID - {fil[0]}
            Nome - {fil[1]}
            Tipo - {fil[2]}
            ''')


    else:
        print("Filme não está disponivel.")

def escolherFilmes():
    escolher=con.consultarBanco('''
    SELECT * FROM "Filmes"
    ORDER BY "Nome" ASC 
''')
    if escolher :
        print("Filmes Disponiveis:")
        for i in escolher:
            print(f'''
            ID - {i[0]}
            Nome - {i[1]}
            Tipo - {i[2]}
            ''')
        ip(input("Você quer alugar esse Filme? 1 - Sim ou 2 - Não :"))
        ip = input("escolha uma opção: ")
        if ip == 1 or ip == "Sim":
            print(f"Você alugou o Filme '{i[1]}','{usuario}' !! ")
        elif ip == 2 or ip == "Não":
            print("Você não alugou nenhum filme.")
        else:
            print("Nenhuma opçâo Válida!!")

def verAlugueis():
    alugueis = con.consultarBanco('''

    SELECT * FROM "Alugueis"
    ORDER BY "ID" ASC
    ''')
    if alugueis :
        print(f'ID | Nome | Tipo |')
        for aluguel in alugueis :
            print(f"{aluguel[0]} |{aluguel[1]}")
        


    # cliente = con.consultarBanco(f'''SELECT * FROM "Clientes"
    # WHERE "ID" = {idCliente}
    # ''')

    # if cliente:

    #     cliente = cliente[0]

    #     print("Cliente Escolhido: ")

    #     print(f'''
    #     ID - {cliente[0]}
    #     Nome - {cliente[1]}
    #     CPF - {cliente[2]}
    #     ''')

    #     listaAlugueis = conexaoBanco.consultarBanco(f'''
    #     SELECT * FROM "Alugueis"
    #     WHERE "ID_Cliente" = '{cliente[0]}'
    #     ''')
    #     if listaAlugueis:
    #         print("Lista de alugueis: ")

    #         print("ID | Cliente | Livro | Data de Aluguel")
    #         for aluguel in listaAlugueis:

    #             #Você já tem o id do Cliente e id do Livro, busque nas tabelas e pegue as informações

    #             clienteDoAluguel = conexaoBanco.consultarBanco(f'''
    #             SELECT * FROM "Clientes"
    #             WHERE "ID" = {aluguel[1]}
    #             ''')[0]

    #             livroDoAluguel = conexaoBanco.consultarBanco(f'''
    #             SELECT * FROM "Livros"
    #             WHERE "ID" = {aluguel[2]}
    #             ''')[0]

    #             print(f"{aluguel[0]} | {clienteDoAluguel[1]} | {livroDoAluguel[1]} | {aluguel[3]}")
    #     else:
    #         print("O cliente não possui aluguéis cadastrados")

    # else:
    #     print("O cliente não foi encontrado!")
    

def verinfo():
    pass

            
while True:
    print("Faça o login:")

    nomeUsuario = input("Digite o nome de usuário:")

    consultaUsuario = con.consultarBanco(f'''
    SELECT * FROM "Login"
    WHERE "Nome_Usuario" = '{nomeUsuario}'
    ''')

    if consultaUsuario:
        usuario = consultaUsuario[0]
    else:
        usuario = False

    if usuario:
        
        senhaUsuario = input("Digite a senha:")

        if senhaUsuario == usuario[3]:

            print("Bem vindo", usuario[1])
            break
        else:

            print("Senha inválida!")
    else:
        print("Usuário inválido")



while True:

    if usuario[5] == "admin":
        print('''  

    Locadora RA !!!

        Perfil de Admin:

        1 - Cadastrar Cliente
        2 - Cadastrar Filmes
        3 - Ver Alugueis
        4 - Ver Clientes
        5 - Ver Filmes/Disponiveis
        0 - Sair 
                
            ''')
        op = input("Escolha uma opção:")
        match op :
                case "1":
                    cadastrarCliente()
                case "2":
                    cadastrarFilmes()
                case "3":
                    verAlugueis()
                case "4":
                    VerClientes()
                case "5":
                    VerFilmes()
                case "0":
                    print('Saindo do programa')
                    break
            
    elif usuario[5] == "comum":

        print(''''
        
        
        O que deseja fazer? : 


        1 - Escolher Filmes
        2 - Ver Histórico de Filmes
        3 - Ver Info.
        4 - Sair 
        ''')
        op = input("Escolha uma opção:")
        match op :
            case "1":
                escolherFilmes()
            case "2":
                verinfo()
            case "3":
                verinfo()
            case "4":
                print('Saindo ...... ')
                break
    else:
        print("Usuário comum detectado!")
        break



