class Funcionario:
    def __init__(self,nome,salario,luvas):
        self.nome = nome
        self.salario = salario

    def aumentarSalario(self,aumentodesalario) :
        BonusMArketing = self.salario * aumentodesalario/100
        self.salario+= BonusMArketing
    print()
    #adicionais
    def Luvas(self,Luvas):
            Adicionais= self.salario * Adicionais
            self.salario+=Adicionais
    print()

cerrisete =  Funcionario("Cr7",100000000.00,1000.000)
print('Salario antes:   R$', cerrisete.salario)

cerrisete.aumentarSalario(15)
print('Salario depois:  R$', cerrisete.salario)

cerrisete.Luvas(75)
print('O adicionais de transporte e luvas é: R$' , cerrisete.Luvas)
        
    