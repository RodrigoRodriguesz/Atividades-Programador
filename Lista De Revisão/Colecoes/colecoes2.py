#Escreva um programa que leia uma lista de números inteiros 
# e remova todos os valores duplicados. Em seguida, imprima a lista sem os valores duplicados.

lista = [10,10,20,25,55,55,20,60,110,220]
contador=[]
for numero in lista:
    if numero not in contador:
         contador.append(numero)
print(contador)
        