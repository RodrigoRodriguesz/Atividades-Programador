numero=input("Digite o primeiro número:")
numero2= input("Digite o segundo número:")
numero3= input("Digite o terceiro número:")

if numero > numero2 and numero > numero3 :
    print("Maior numero é :"+numero)
elif numero < numero2 and numero < numero3:
    print("Menor número é:"+numero)

if numero2 > numero and numero2 > numero3:
    print('Menor número é:'+numero2)
elif numero2 < numero and numero2 < numero3:
    print("O menor número é:"+numero2)

if numero3 > numero2 and numero3 > numero :
    print("Maior numero é :"+numero3)
elif numero3 < numero2 and numero3 < numero:
    print("Menor número é:"+numero3)
