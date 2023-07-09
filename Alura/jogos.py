#trazendo os códigos dos jogos pra esse código

import forca
import advinhacao

def escolhe_jogo():

    print('**********************************')
    print('******Escolha seu jogo!******')
    print('**********************************')

    print('Forca (1) ou Advinhação (2)? ')

    jogo = int(input('Digite sua opção: '))

    if(jogo == 1):
        print('Jogando forca')
        forca.jogar()   #chamando o jogo forca
    elif (jogo == 2):
        print('Jogando adivinhação')
        advinhacao.jogar()  #chamando o jogo advinhação
    else:
        print('Valor incorreto. Escolha entre as opções disponíveis')

if(__name__ == '__main__'):
    escolhe_jogo()