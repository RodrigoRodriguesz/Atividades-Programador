import psycopg2
try:
    connecting = psycopg2.connect(dbname= "Supermercado", host = "Localhost", port = "5432", user = "postgres", password = "postgres")

    cursor = connecting.cursor()

    print("Conected!!")
except(Exception,psycopg2.Error) as error:
    print("ERROR 404", error)
# ----------------------------------------------------------

class Conexao:
    def __init__(self,dbname,host,port,user,password) -> None:
        self._dbname =dbname
        self._host = host
        self._port=port
        self._user=user
        self._password=password

    def ConsultarBanco(self,sql):
        self._sql = psycopg2.connect(dbname= self._dbname, port=self._port, user=self._user, password=self._password)
   

# -------------------------------------------------------------
def CadastrarCliente():
    print("Voce esta cadastrando um novo cliente")
        
    nome = input("Digite o Nome: ")
        
    cursor.execute(f'''
    Insert into "Cliente"
     VALUES(Default,'{nome}')

        ''')

    print(f'Você cadastrou o cliente {nome} no sistema !')
    connecting.commit()
    # -------------------------------------------------------------
def CadastrarProduto():
    print("Voce esta cadastrando um novo Produto")
        
    Name = input("Digite o Nome: ")
        
    cursor.execute(f'''
    Insert into "Produto"
     VALUES(Default,'{Name}')

        ''')

    print(f'Você cadastrou o Produto {Name} no sistema !')
    connecting.commit()
        # -------------------------------------------------------------
# def CadastrarCompra():
#     print("Voce esta cadastrando um novo Produto")
        
#     Name = input("Digite o Nome: ")
        
#     cursor.execute(f'''
#     Insert into "Produto"
#      VALUES(Default,'{Name}')

#         ''')

#     print(f'Você cadastrou o Produto {Name} no sistema !')
#     connecting.commit()



while True:
    try:
        print('''
    BEM VINDO AO WALLMART !!!


    Escolha uma opção:

    1 - Cadastrar Cliente
    2 - Cadastrar Produtos
    3 - Cadastrar Compra
    4 - Ver Clientes
    5 - Ver Produtos
    6 - Historico de Vendas
    0 - Sair 
            
        ''')
        op = input("Escolha uma opção:")
        match op :
            case "1":
                CadastrarCliente()
            case "2":
               CadastrarProduto()
            case "3":
                CadastrarCompra()
            case "4":
                VerClientes()
            case "5":
                VerProdutos()
            case "6":
                HistoricoVendas()
            case "0":
                print('Saindo do programa')
                break
        
        cursor.close()
        connecting.close()
    except (Exception , psycopg2.Error) as error:
        print('error', error)


# criarnovocliente
# criarnovoproduto


