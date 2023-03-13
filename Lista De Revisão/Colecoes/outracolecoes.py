# Escreva um programa que leia uma lista de nomes 
# e crie um dicionário onde a chave é o nome e o valor é o número de vezes que o nome aparece na lista

listaNomes=['Rodrigo', 'Daniel A. ' , 'Daniel A. ','Luan', 'Meçi' , 'Cerrisete' ]
cont_nomes = {}
for nome in listaNomes:
    if nome in cont_nomes:
        cont_nomes[nome] += 1
    else:
        cont_nomes[nome] = 1
print(cont_nomes)
