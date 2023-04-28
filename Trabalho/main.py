import psycopg2
try:
    connecting = psycopg2.connect(dbname= "Locadora", host = "Localhost", port = "5432", user = "postgres", password = "postgres")

    cursor = connecting.cursor()

    print("Conected!!")
except(Exception,psycopg2.Error) as error:
    print("ERROR 404", error)
# ------------------------------------------------------------------
#Funcoes

def CadastrarCliente():
    pass
def CadastrarFilmes():
    pass
def VerFilmesAlugados():
    pass
def verClientes():
    pass
def VerFilmes_Comprados():
    pass

# ------------------------------------------------------------------

while True:
    try:
        print('''

  Locadora RA !!!

    Perfil de Admin:

    1 - Cadastrar Cliente
    2 - Cadastrar Filmes
    3 - Ver Filmes Alugados
    4 - Ver Clientes
    5 - Ver Filmes/Comprados
    0 - Sair 
            
        ''')
    op = input("Escolha uma opção:")
    match op :
            case "1":
                if admin:
                    CadastrarCliente()
                else:
                    print("Acesso negado, usuário sem acesso")
            case "2":
               CadastrarFilmes()
            case "3":
                VerFilmesAlugados()
            case "4":
                VerClientes()
            case "5":
                VerFilmes()
            case "6":
                HistoricoVendas()
            case "0":
                print('Saindo do programa')
                break
        
    cursor.close()
    connecting.close()
    except (Exception , psycopg2.Error) as error:
print('error', error)




# from PySimpleGUI import PySimpleGUI as sg
# #Layout
# sg.theme('Reddit')
# Layout = [
#     [sg.Text('Usuário'),sg.Input(key="usuario")],
#     [sg.Text('Senha'), sg.Input(key="senha", password_char='*')],
#     [sg.Checkbox("Salvar login? ")],
#     [sg.Button('Entrar')]
# ]

# nome = 'Rodrigo'

# janela = sg.Window('Tela de Login', Layout)
# while True:
#     eventos , valores = janela.read()
#     if eventos == sg.WINDOW_CLOSED:
#         break
#     if eventos== 'Entrar':
#         if valores['usuario'] == nome and valores ['senha'] == '123':
#             print(f"Bem-vindo"  , nome)
#         else:
#           print("Usuario inválido")
#         break  