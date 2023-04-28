
import psycopg2
try:
    connecting = psycopg2.connect(dbname= "Pizzaria", host = "Localhost", port = "5432", user = "postgres", password = "postgres")

    cursor = connecting.cursor()

    print("Conected!!")
except(Exception,psycopg2.Error) as error:
    print("ERROR 404", error)
# --------------------------------------------------------
# cursor.execute('''

#     CREATE TABLE "Pizzas"(

#      "ID" serial,
#      "Nome" varchar(255) Not null,
#      "Tipo" varchar(255) Default('Nao informado'),
#      "Preço" Money Not Null,
#      PRIMARY KEY("ID")
#     );
#      ''')
# connecting.commit()
# print("Criado com sucesso!")
# --------------------------------------------------------
# cursor.execute('''

#     CREATE TABLE "Bebidas"(

#      "ID" serial,
#      "Nome" varchar(255) Not null,
#      "Tipo" varchar(255) Default('Nao informado'),
#      "Preço" Money Not Null,
#      PRIMARY KEY("ID")
#     );
#      ''')
# connecting.commit()
# print("Criado com sucesso!")

# ------------------------------------------------------


# print("Bem vindo!!")

# Codigo = input("Escolha o Sabor de Sua Pizza: ")
# -------------------------------------------------------


def cadastrarpizza():
    Pizza = input("Qual o nome da Pizza: ")
    tipo = input("Qual o tipo da Pizza: ")
    preço = input("PRECO DA PIZZA: ")
    cursor.execute(f'''
    insert into "Pizzas"
    VALUES(default,'{Pizza}', '{tipo}', '{preço}' )
    
    ''')
    connecting.commit()


# -------------------------------------------------------


def EscolherPizzas():
    cursor.execute('''
    SELECT * FROM "Pizzas"
    ORDER BY "ID" ASC
    
    
       
    ''')
def EscolherBebidas():
    cursor.execute('''
    SELECT * FROM "Bebidas"
    ORDER BY "ID" ASC
    
    
       
    ''')
def EscolherOutros():
    cursor.execute('''
    SELECT * FROM "OUTROS"
    ORDER BY "ID" ASC
    
    
       
    ''')



# --------------------------------------------------------




while True:
    try:
        print('''
    BEM VINDO !!!


    Escolha uma opção:
    
    123 - Suporte
    1 - Ver Pizzas
    2 - Ver Bebidas
    3 - Ver Outros
    0 - Sair 
            
        ''')
        op = input("Escolha uma opção:")
        match op :
            case "123":
                cadastrarpizza()
            case "1":
                EscolherPizzas()

            case "2":
                EscolherBebidas()

            case "3":
                EscolherOutros()

            case "0":
                print('Saindo do programa')
                break
                
        cursor.close()
        connecting.close()
    except (Exception , psycopg2.Error) as error:
        print('error', error)

# --------------------------------------------------------