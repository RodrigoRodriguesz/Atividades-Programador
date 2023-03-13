
nome = input("Digite seu nome:")
nota1 = float(input("Digite a nota 1:"))
nota2 = float(input("Digite a nota 2:"))
nota3 = float(input("Digite a nota 3:"))

soma = nota1 + nota2 + nota3

media = soma/3

if media>=7:
    print(f"{nome} Você foi aprovado :) com a média {media}")

elif  media <=5:
        print(f"{nome} Você foi reprovado :/ com a média {media}")
elif  media <7 and media>5 :
              print(f"{nome} Você está de recuperação com a média {media} :/ ")
else:
        print("Inválido")


