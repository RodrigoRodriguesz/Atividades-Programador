# class Name:
#     def __init__(self,nome,idade):
#         self.nome = nome
#         self.idade= idade

    
#     def get_nome(self):
#         print("nome: ",self.nome)

        
    
#     def get_Idade(self):
#         print("idade: ", self.idade)

     
# Nome = (input("Digite o seu nome "))
# idade = (input("Informe sua idade:  "))

# pessoa1 = Name(Nome,idade)

# print(f"Nome: {Nome}, Idade: {idade}")







class Circulo:
     def __init__(self,Raio):
         self.raio=Raio
    
     def Calcular_Area(self,area):
         area = self.raio * self.raio * 3.14
         return area    
     def calcularCircunferencia(self):
         circunferencia = 2*3.14*self.raio 
         return  (f'{circunferencia:.2f}')


circulo1 = Circulo(5)
print (circulo1.calcularCircunferencia())



# class Banco:
#     def __init__(self,saldo,titular):
#         self.saldo= saldo
#         self.titular=titular
#     def Depositar(self,deposito):
#         self.saldo += deposito
#     def sacar(self,saque):
#         if self.saldo >=saque:
#             self.saldo-=saque
#         else:
#             print("saldo insuficiente")
#     def consultarsaldo(self):
#         return self.saldo
    
# titular= input("Digite seu nome: ")
# saldo=float (input("Digite seu saldo: "))
# deposito=float(input("Valor do deposito: "))
# Pessoa= Banco (saldo,titular)
# print(f"Nome: {Pessoa.titular}, saldo: {Pessoa.saldo}")
# Pessoa.Depositar(deposito)
# print('Seu novo saldo é' , deposito + saldo)


    



