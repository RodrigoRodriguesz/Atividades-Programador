
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

def buscarfilmes():
    buscar = con.consultarBanco('''
    SELECT * FROM "Filmes"
    ORDER BY "ID" ASC

    ''')
    if buscar:
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
       

        print("Você quer alugar esse Filme? Sim ou Não :")
    

        ip = input("Escolha uma opção:")

        #  ----------------------------------------------------------
        # var= ip.upper()
        # match var :
        #     case "SIM":
        #         print('Escolha um filme:')
                
        
        #     case "NAO" :
        #         print('Você não escolheu nenhum filme.')

        #     case "Nâo" :
        #         print('Você não escolheu nenhum filme.')
        #     case _:
        #         print('Saindo......')
    
        # ----------------------------------------------------------   


        if ip == '1' or ip == "Sim":
            print("Filmes Disponiveis:")
            for i in escolher:
                print(f'''
            ID - {i[0]}
            Nome - {i[1]}
            Tipo - {i[2]}
            ''')

            idescolhido = input("Escolha um filme:")
            filmeescolhido=con.consultarBanco(f'''
            Select * from "Filmes"
            Where "ID" = {idescolhido}
            
            
            ''')
            if filmeescolhido == [()]:
                print("Filme inválido")
            else:
                
                consultaUsuario = con.consultarBanco(f'''
                SELECT * FROM "Login"
                WHERE "Nome_Usuario" = '{nomeUsuario}'
                ''')
                con.manipularBanco(f'''INSERT INTO "Alugueis"
            values(default,'{consultaUsuario[0][0]}','{idescolhido}',default,default)''')
                
            print(f'Você alugou o Filme.',idescolhido)
            
                  

        elif ip == '2' or ip == "Não":
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





def verinfo():
    info = con.consultarBanco(f'''
    SELECT * FROM "Alugueis" 
    where "ID_Cliente" = '{consultaUsuario[0][0]}'
    ORDER BY "ID" ASC
    ''')
    if info:
        print(f'ID | Filme | Data Pedido |')
        for info in info:
            print(f'{info[0]} | {info[1]} | {info[2]} | {info[3]}|')
            if info[3] :
                print("SEU PEDIDO ESTÁ:",info[4])
            

            
while True:
    print("Faça o Login:")

    nomeUsuario = input("Digite o Nome de Usuário:")

    consultaUsuario = con.consultarBanco(f'''
    SELECT * FROM "Login"
    WHERE "Nome_Usuario" = '{nomeUsuario}'
    ''')

    if consultaUsuario:
        usuario = consultaUsuario[0]
    else:
        usuario = False

    if usuario:
        
        senhaUsuario = input("Digite a Senha:")

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



