class Funcionario:
    def __init__(self,nome,salario):
        self.nome = nome
        self.salario = salario
    def aumentarSalario(self,aumentodesalario) :
        Bonus= self.salario * aumentodesalario/100
        self.salario+= Bonus
        print()


cerrisete =  Funcionario("Cr7",10000000.00)
print('Salario antes:',cerrisete.salario)
cerrisete.aumentarSalario(10)
print('Salario depois:',cerrisete.salario)
        
    