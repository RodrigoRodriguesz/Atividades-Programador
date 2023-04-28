
import random


class Pokemon:

    def __init__ (self , nome, tipo , ataque , fraqueza ,hp):
        self.nome= nome
        self.tipo=tipo
        self.ataque=ataque
        self.fraqueza=fraqueza
        self.hp=hp

    

        
Pokemon1= Pokemon( 'Pichu','Raio','ThunderShock','Terra',100)
Pokemon2= Pokemon( 'bulbasaur','Planta','Bomba de Semente','Fogo',95)
pokemon3= Pokemon( 'Charmander','Fogo','respiracao de fogo','Agua e Terra',110)
Ataque= ('>')
pokemonescolhido= random.choice([Pokemon1,Pokemon2,pokemon3])
if Pokemon1:
    print ( """ Pichu

      @%,@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
      .????.@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
      .???????S@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
      :?????????#@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
      *?????????????*@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
      @???????#?????###@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@,*.??#
      @?????,##,S???#####@@@@@@@@@@@@@@@@@@@@@@@@@@S##????????????
      @?????*,,,,,,########@@@@@@@@@@@@@@@@@:###????????????????#@
      @##????,,,,,,,,,#####@@@@@@@@@@@@@.######?????#?:#????????@@
      @####?#,,,,,,,,,,,##@@@@@@@@@@@@@@#######*,,,,,*##+?????+@@@
      @######,,,,,,,,,,,S@@@@@@@@@@@@@@#.,,,,,,,,,,,,,,:?####@@@@@
      @######,,,,,,,,,,%@@,S.S.,@@@@@@@,,,,,,,,,,,,,,,######@@@@@@
      @@#####,,,,,,,,.,,,,,,,,,,,,,,,*#,,,,,,,,,,,,,.#####:@@@@@@@
      @@@@@@@@@@.#,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,######@@@@@@@@@
      @@@@@@@@@,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,+######@@@@@@@@@@
      @@@@@@@@%,,,,,++:,,,,,,,,,,,,,,,,,,,,,@@:.######:@@@@@@@@@@@
      @@@@@@@:,,,:##@@@#,,,,,,,,,,,,?@S#,,,,,,@@@@@@@@@@@@@@@@@@@@
      @@@@@@@?,,,#######,,,,,,,,,,,#.@:##,,,:?@@@@@@@@@@@@@@@@@@@@
      @@@@@@@.,,S,??%?*,,,,,,,,,,,,####?%+,::%@@@@@@@@@@@@@@@@@@@@
      @@@@@@@@?..*+,,,,,,*,,,,,,,,,,,+#S,::::*@@@@@@@@@@@@@@@@@@@@
      @@@@@@@@@%..*,,,,,,,,,,,,,,,,,,,:.*...%@@@@@@@@@@@@@@@@@@@@@
      @@@@@@@@@@.**::*::::::,,:::::::+.....@@@@@@@@@@@@@@@@@@@@@@@
      @@@@@@@@.@@@@?:**:::*::::::::::*...@@@@@@@@@@@@@@@@@@@@@@@@@
      @@@@@?,,,,,,,,,:,##S::::**:::S#@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
      @@@@@@@.,,,,,,:S#?##?########:#****#,@@@@@@@@@@@@@@@@@@@@@@@
      @@@@@@@@@@,%:*%,??#,,,,:*S##**:..****:,.*@@@@@@@@@@@@@@@@@@@
      @@@@@@@@@@@@@+,,,,,,,,,,,,,,,,,,*...*:,.,@@@@@@@@@@@@@@@@@@@
      @@@@@@@@@@@@@+,,,,,,,,,,,,,,,,,,?@@@@@*#?@@@@@@@@@@@@@@@@@@@
      @@@@@@@@@@@@@*,,,,,,,,,,,,,,,,,,.@#########?@@@@@@@@@@@@@@@@
      @@@@@@@@@@@@@.*:,,,,,,,,,,,,,,:.##%,?#####????:@@@@@@@@@@@@@
      @@@@@@@@@@@@@@?.....*******....S@@@@@@:##?????@@@@@@@@@@@@@@
      @@@@@@@@@@@@@@S.+..********...#%@@@@@@@@@##,@@@@@@@@@@@@@@@@
      @@@@@@@@@@@#*,,,,*.#@@@@@@@..*:,,*S@@@@@@@@@@@@@@@@@@@@@@@@@
      @@@@@@@@@@+@,%,,,#@@@@@@@@@@,S,,,%,,:@@@@@@@@@@@@@@@@@@@@@@@

      """)

oponente = random.choice([Pokemon1,Pokemon2,pokemon3])

#Condicao
if pokemonescolhido.hp>oponente.hp:
    print("Você ganhou")
elif pokemonescolhido.hp<oponente.hp:
    print('Voce perdeu')
else :
    print("Empate")
    

# Crie duas equipes de Pokemon, uma para cada jogador. Você pode criar as equipes manualmente, 
# definindo os Pokemon e seus atributos, ou pode usar uma biblioteca Python que já possua uma lista de Pokemon e suas características, como o Pykemon.

# Crie uma classe Pokemon que tenha atributos como nome, tipo, pontos de vida, ataque, defesa, velocidade, etc. Em seguida,
#  defina métodos para que os Pokemon possam atacar e serem atacados, perder pontos de vida, verificar se estão nocauteados, etc.

# Crie uma classe Jogador que possua um nome e uma equipe de Pokemon. 
# O jogador deve ser capaz de escolher qual Pokemon irá usar em cada turno, e de fazer um ataque.

# Crie uma função para simular uma batalha entre os dois jogadores. A cada turno, 
# cada jogador escolhe qual Pokemon irá usar e qual ataque irá fazer. O ataque é então comparado com a defesa do Pokemon adversário, e se o ataque for bem sucedido, o Pokemon adversário perde pontos de vida. A batalha continua até que todos os Pokemon de um jogador sejam nocauteados.

# Implemente a lógica da batalha em um loop que repete até que um jogador vença. A cada turno,
#  o jogador atual deve escolher um Pokemon e um ataque, e o Pokemon adversário deve perder pontos de vida se o ataque for bem sucedido. Se um Pokemon for nocauteado, o próximo Pokemon na equipe do jogador deve entrar em campo.

# Exiba o resultado da batalha, mostrando qual jogador venceu e quantos Pokemon cada um ainda tinha em sua equipe.
   
    
