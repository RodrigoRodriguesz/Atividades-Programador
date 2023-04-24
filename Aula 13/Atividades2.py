#class Nome:
#    def __init__(self,nome,idade):
 #       self.nome = nome
  #      self.idade = idade
#
 #   def apresentar(self):
  #      texto = print(f'Meu nome é {self.nome} e tenho {self.idade} anos.')
   #     return texto
    
#pessoa1 = Nome("Maria",30)
#pessoa1.apresentar()

# class Circulo:
#     def __init__(self,raio):
#         self.raio = raio

#     def calcularArea(self):
#         Area = 3.14 * (self.raio ** 2)

#         return Area
    
#     def calculacircunferencia(self):
#         circunferencia=3.14*self.raio
        
#         return circunferencia
    
# circle=Circulo(5)

# print(circle.calcularArea())
# print(f"{circle.calculacircunferencia():.2f}")

# class Livro ():
#     def __init__(self, titulo, autor, ano):
#         self.titulo = titulo
#         self.autor = autor
#         self.ano = ano
    
#     def informações(self):
#         return f"{self.titulo} - {self.autor} ({self.ano})."
    

# book = Livro ("O Senhor dos Aneis", "J. R. R. Tolkien", "1954")
# print(book.informações())
        
#Problema: Crie uma classe "Funcionario" com os atributos "nome", "salario" e "departamento". Crie um método "aumentarSalario" que recebe um valor percentual como parâmetro e aumenta o salário do funcionário de acordo com o valor informado. Crie também um método "informacoes" que retorna uma string com as informações do funcionário no formato "nome - departamento - salario".

# Problema - 4:
# class Funcionario:
#     def __init__(self,nome, salario, departamento):
#         self.nome = nome
#         self.salario = salario
#         self.departamento = departamento
#     def aumentarSalario (self, percentual):
#         aumento = self.salario * (percentual/100)
#         self.salario += aumento
    
#     def informaçoes(self):
#         return f"{self.nome}\ndo departamento: {self.departamento}\nele recebe R$: {self.salario:.2f}"    

# Func1 = Funcionario ("Matheus", 30000.00, "Jurídico")
# Func1.aumentarSalario(70)
# print (Func1.informaçoes()) 


# class Carros:
#     def __init__(self,nome,modelo,ano):
#         self.nome=nome
#         self.modelo=modelo
#         self.ano=ano
#     def informacoes(self):
#         return f"{self.nome} - {self.modelo} ({self.ano})."
       
                    
#     def acelerar(self,acelerar1):
#        print (f"O carro {self.nome}  {self.modelo} Acelerou  {acelerar1}")
     
                
                    
# Carros1 = Carros("Fiat","uno",2000)
# print(Carros1.informacoes())
# Carros1.acelerar(80)

#Crie uma classe chamada "Agenda" que tenha como atributos uma lista de contatos e o número máximo de contatos permitidos. 
#Cada contato deve ser um objeto da classe "Contato", que deve ter como atributos o nome e o telefone.
# A classe "Agenda" deve ter os métodos "adicionar_contato", 
#que deve receber um objeto "Contato" e adicioná-lo à lista de contatos, e "remover_contato", 
#que deve receber um nome e remover da lista de contatos o contato que tiver esse nome.
# Além disso, crie o método "informacoes" que retorna uma string contendo o nome e o telefone de cada contato

# class Agenda:
#     def __init__(self,listaDeContatos, maxContatos):

#         self.listaDeContatos = listaDeContatos
#         self.maxContatos = maxContatos

#     def adicionarContato(self, novoContato):
#         if len(self.listaDeContatos) < self.maxContatos:
#             self.listaDeContatos.append(novoContato)
#         else:
#             print("Contato não foi adicionado. Limite atingido.")
        

#     def removerContato(self,nomeContato):
#         for contato in self.listaDeContatos:
#             if contato.nome == nomeContato:
#                 self.listaDeContatos.remove(contato)


#     def informacoes(self):
        
#         impressaoLista = ""

#         for contato in self.listaDeContatos:
#             impressaoLista = impressaoLista + f"• {contato.nome} - {contato.telefone} \n"
#         return impressaoLista


# class Contato:
#     def __init__(self, nome, telefone):
#         self.nome = nome
#         self.telefone = telefone


# contato1 = Contato("Jorge","1o23-123i9-123")

# contato2 = Contato("Maicou", "1230140819841982")

# contato3 = Contato("Maria", "1231151512")

# minhaAgenda = Agenda([contato1,contato2,contato3], 5)

# print(minhaAgenda.informacoes())

# minhaAgenda.removerContato("Maria")

# print(minhaAgenda.informacoes())

# minhaAgenda.adicionarContato(Contato("Josuel", "1231411"))

# minhaAgenda.adicionarContato(Contato("Milena", "1231412e121"))

# print(minhaAgenda.informacoes())

# minhaAgenda.adicionarContato(Contato("Fabricio","12312d12e1"))

# minhaAgenda.adicionarContato(Contato("Pericles", "1djoi1jd12"))
        



# class Conta:
#     def __init__(self,saldo) :
#        self._saldo = saldo
#     def get_saldo(self):
#        return self.set_saldo
        
#     def set_saldo(self,saldo):
#         self._saldo=saldo
       
# conta1=Conta(200.0)
# conta2=Conta(300.0)
# conta3= Conta(-100.0)

# conta1.get_saldo()
# conta2.get_saldo()
# conta3.set_saldo(conta1.get_saldo() + conta2.get_saldo() +conta3.get_saldo())



    

# class Conta:
#     def __init__(self,saldo,numConta):
#         self.saldo = saldo
#         self._numConta = numConta
#     def getsaldo(self):
#         return self.saldo
#     def setsaldo(self,NovoSaldo):
#         if NovoSaldo <0: 
#             print("Digite um saldo positivo!!")
#         else:
#             self._saldo = NovoSaldo

#     def getNumConta(self):
#         return self._numConta
#     def setNumConta(self,NovoNumero):
#         self._numConta


# conta1 = Conta (200.0)
# conta2 = Conta (100.0)

class Pokemon:
    def __init__(self,nome,tipo,hp,movimento):
      self._nome = nome 
      self._tipo=tipo
      self._hp=hp
      self._movimento=movimento
    def fazerBarulho(self):
        print (f"{self._nome} fez um barulho")

class PokemonFogo(Pokemon):
          def __init__(self, nome, tipo, hp, movimento):
              return  super().__init__(nome, tipo, hp, movimento)
class PokemonAgua(Pokemon):
     def __init__(self, nome, tipo, hp, movimento):
          return super().__init__(nome, tipo, hp, movimento)
class PokemonPlanta(Pokemon):
     def __init__(self, nome, tipo, hp, movimento):
        return  super().__init__(nome, tipo, hp, movimento)

