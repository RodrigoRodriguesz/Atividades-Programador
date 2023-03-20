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




