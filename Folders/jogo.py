import random

while True:
    print('''Agora é sua vez!!!
(Digite o número desejado)

    1 - Pedra
    2 - Tesoura
    3 - Papel
    4 - Se render
    ''')
    jogada = int(input)('> ')

    oponente = random.choice(range(1,3))
    #print jogador
    if jogada == 1:
        print('Você usou Pedra')
    elif jogada == 2:
        print('Você usou Tesoura')
    elif jogada == 3:
        print('Você usou Papel')
    elif jogada == 4:
        print('Você se rendeu')
        break
    else:
        print('Jogada invalida')

    #print oponente
    if oponente == 1:
        print('O oponente usou Pedra')
    if oponente == 2:
        print('O oponente usou Tesoura')
    if oponente == 3:
        print('O oponente usou Papel')
    #condições
    #Pedra
    if jogada==1 and oponente == 3:
        print('Você perdeu')
    if jogada==1 and oponente == 1:
        print('Empate')
    if jogada==1 and oponente == 2:
        print('Você venceu!!!')
    #Tesoura
    if jogada==2 and oponente == 3:
        print('Você ganhou!!!')
    if jogada==2 and oponente == 1:
        print('Você perdeu')
    if jogada==2 and oponente == 2:
        print('Empate')
    #Papel
    if jogada==3 and oponente == 3:
        print('Empate')
    if jogada==3 and oponente == 1:
        print('Você ganhou!!!')
    if jogada==3 and oponente == 2:
        print('Você perdeu')
    input('')

    


          
    






    



