#nome = ('Castilho' , 'Erick ' , 'Luvalove' , 'Alvaro')

#print(sorted(nome))
#Questao2

#lista = {5,10,15,20}

#soma = 0 

#for i in lista:
   # soma+=i 
#print(soma)

#Questoes3
#numeros = [100,20,30]

#multiplicacao = 1
#for i in numeros:
  #  multiplicacao = multiplicacao * i
#print("O numero é:" , multiplicacao)

#Questoes4

#dic1={1:10, 2:20}
#dic2={3:30, 4:40}
#dic3={5:50,6:60}
#dic4= {}
#for i in [dic1 , dic2 , dic3]:
  #  dic4.update(i)
#print(dic4)

#Questoes5 Escreva um programa Python para obter o menor número de uma lista

#lista = [ 5,20,36]
#menor = lista [0]
#for numero in lista :
    #numero > menor
    #menor < numero
#print("Menor numero é :", menor)


#Questoes6 Escreva um programa Python para remover duplicatas de uma lista.

#listaRemover=(1,1,2,5,5,5,5,3,6,8,7,8,9,10)
#resultado = 0

#while resultado < len(listaRemover):
  #  for i in  range (len(listaRemover)):
      #  if resultado != i:
          #  if i < len(listaRemover):
             #   if listaRemover[resultado] == listaRemover[i]:
                 #   print(listaRemover)
                    
    

#Questao7
#Escreva um programa Python para criar uma tupla

#TimesSp= ('Santos' , 'Sao paulo' , 'Palmeiras')
#print((TimesSp[2]))

#Questao8

#palavras = "lets go my team"
#for letra in palavras:
    #print(letra)

#Questao9

#Escreva um programa em Python para somar todos os itens de uma lista
#numeros = [100,20,30]

#soma = 0
#for i in numeros:
  #  soma = soma + i
#print("O numero é:" , soma)

#Questao 10 

 #Escreva um programa Python para obter o menor número de uma lista
#lista = (5,40,58)
         
#diminuir = 0
#for i in lista:
  #  diminuir = diminuir - i
#print("O numero é:" , diminuir)
#if diminuir > 900 : 
 #   print("O numero passou do exigido!")
#else:
    #print("o numero esta na faixa permitida")

#lista=([[(2, 5), (1, 2), (4, 4), (2, 3), (2, 1)]])
#novalista=[]
#for tuple in lista:
 # novalista.append(tuple[::-1])
#novalista.sort
#
#lista = []


#for turple in novalista :
#  lista.append(tuple[::-1])
#  print(lista)

#lista=([[(2, 5), (1, 2), (4, 4), (2, 3), (2, 1)]])
#novalista=[]
#for tuple in lista:
 # novalista.append(tuple[::-1])
#novalista.sort

#lista = []


#for turple in novalista :
  #lista.append(tuple[::-1])
  #print(lista)


#def hello (Nome, Sobrenome,idade):
   # print('hello',Nome, Sobrenome,idade) 

#hello ('Fábio', 'Martins' , idade= 20)                  
#def calcular_pagamento(qtd_horas , valor_horas):
    #horas = float(qtd_horas)
    #taxas = float (valor_horas)
    
    #if horas <= 40 :
        #salario = horas*taxas
    #else: 
        #h_excd = horas -40
        #salario = 40*taxas+(h_excd*(1.5*taxas))
        #return salario
    
#str_horas=input('Digite as horas:')
#str_taxas=input('diite as taxas:')
#str_salario=calcular_pagamento(str_horas,str_taxas)
#print("O valor do seu salario e R$: " , str_salario)

Codigo = input("Digite o codigo do produto:")
Quantidade = int (input("Digite quantos voce quer comprar:"))
preco = 0
nome =  ""
if Codigo =="1":
    nome ="Cachorro quente"
    preco= 20.5
    
elif Codigo =="2":
    nome = "Hambuguer"
    preco= 7.5
  

elif Codigo == "3":
    nome= "X-burguer"
    preco= 8.0
    
elif Codigo =="4":
    nome = "Bauru"
    preco= 12.0
   
else :
    Codigo = "0"
    print('nenhum item escolhido!')

valorhamburguer = preco*Quantidade
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
    Bebidas = "0"
    print("Voce nao escolheu nenhuma bebida!")
valorsuco = preco*Quantidade
print(f"Voce escolheu o {nome} e gastou {valorsuco}")

print(f"O valor total :{valorhamburguer+valorsuco} " )

valortotal = valorhamburguer+valorsuco
if valorhamburguer + valorsuco:

    valorgorjeta = valortotal *0.10
    print(f"A gorjeta foi R$ :{valorgorjeta:.2f}")

if Codigo == "0" and Bebidas == "0": 
    print("Nenhum item selecionado")



    


    







