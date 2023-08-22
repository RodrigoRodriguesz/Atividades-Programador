def questao4Simples():
    num1 = int(input("Escreva o número 1: "))
    num2 = int(input("Escreva o número 2: "))
    num3 = int(input("Escreva o número 3: "))

    lista = [num1,num2,num3]
    lista.sort(reverse=True)

    print(lista)