altura=int(input("Digite a altura:"))
largura=int(input("Digite a largura: "))

linha = ""
for i in range(largura):
     linha = linha + "#"

retangulo = ""
for i in range(altura):
    retangulo = retangulo + "\n" + linha 
print(retangulo)