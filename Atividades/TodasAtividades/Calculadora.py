def soma():
    x = float(input("Digite um numero: "))
    y = float (input("Digite segundo numero: "))
    print("Soma: ",x+y)
def subtracao():
    x = float (input("Digite um numero: "))
    y = float( input("Digite segundo numero: "))
    print("Subtracao: ",x-y)
def Multiplicao():
    x = float (input("Digite um numero: "))
    y = float (input("Digite segundo numero: "))
    print("Multiplicacao: ",x*y)
def Divisao():
    x = float (input("Digite um numero: "))
    y = float (input("Digite segundo numero: ")) 
    print("Divisao: ",x/y)




while True: 
    try:

        #Tabela
        print('''
        _____________________
        | 1. Soma           |
        |___________________|                  
        | 2. Subtração      |
        |___________________|                  
        | 3. Multiplicação  |
        |___________________|                   
        | 4. Divisão        |
        |___________________|   
        ''')


        #escolher operação

        Calculadora = input("Escolha a operacão: ")
        if Calculadora in ('A', '1'):
            soma()
            
        elif Calculadora in ('b', '2'):
            subtracao()
            
        elif Calculadora in ('c', '3'):
            Multiplicao()
            
        elif Calculadora in ('d' , '4'):
            Divisao()
            
        else:
            print('Opção Inválida')

    except:
        print('Erro')

    input()
