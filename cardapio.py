Codigo = input("Digite o codigo do produto:")
Quantidade = int (input("Digite quantos voce quer comprar:"))
preco = 0
nome =  ""
if Codigo =="1":
    nome ="Cachorro quente"
    preco= 22.0
    
elif Codigo =="2":
    nome = "Hambuguer"
    preco= 6.50
  

elif Codigo == "3":
    nome= "X-burguer"
    preco= 8.0
    
elif Codigo =="4":
    nome = "Bauru"
    preco= 12.0
   
else :
    print('nenhum item escolhido!')

valorhamburguer= preco*Quantidade
print(f"Voce escolheu o {nome} e gastou {valorhamburguer}")
Bebidas = input("Você deseja qual bebida:")
Quantidade = int (input("Quantos deseja comprar: "))
if Bebidas =="1":
    nome = "Coca-Cola-Lata"
    preco = 5.0 
    
elif Bebidas =="2":
    nome="Suco Natural 1L "
    preco= 6.0
   
else :
    print("Voce nao escolheu nenhuma bebida!")
valorsuco= preco*Quantidade
print(f"Voce escolheu o {nome} e gastou {valorsuco}")

print(f"O valor total :{valorhamburguer+valorsuco} " )
 



