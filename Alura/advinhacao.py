#subst = "Python"
#verbo = "é"
#adjetivo = "fantástico"
# print(subst, verbo, adjetivo, sep="_", end="!\n")
#********************************************************

import random

def jogar(): #função que irá permitir que chame esse jogo em outro código
    print('**********************************')
    print('Bem vindo ao Jogo de Advinhação')
    print('**********************************')

    #numero_secreto = int(round(random.random() * 100))
    numero_secreto = int(random.randrange(1, 101))
    total_tentativas = 0
    rodada = 1
    pontos = 1000

    #incluindo nível:
    print('Escolha o nível de dificuldade: ')
    print('Fácil (1), Médio (2) ou Difícil (3)')

    nivel = int(input('Defina o nível: '))

    if(nivel == 1):
        total_tentativas = 20
    elif(nivel == 2):
        total_tentativas = 10
    else:
        total_tentativas = 5



    #while (rodada <= total_tentativas): -- sem o for
    for rodada in range(1, total_tentativas + 1):
        print(f'Tentativa {rodada} de {total_tentativas}')
        chute = int(input('Digite seu palpite entre 1 e 100: '))
        print(f'Você digitou: {chute}')

        if(chute < 1 or chute > 100):
            print('Você deve digitar um valor entre 1 e 100!')
            continue

        acertou = chute == numero_secreto
        maior = chute > numero_secreto
        menor = chute < numero_secreto

        if (acertou):
            print(f'Você acertou e fez {pontos:.0f} pontos!')
            break
        else:
            pontos_perdidos = abs(numero_secreto - chute) / 3  # colocando numero absoluto pois se o chute for maior, também irá tirar pontos pois ignorará o sinal de numero negativo
            pontos = pontos - pontos_perdidos

            if(maior):
                print('Você errou. Seu chute foi maior que o numero secreto ')
                if (rodada == total_tentativas):
                    print(f'O numero secreto era {numero_secreto} e você fez {pontos:.0f} pontos')
            elif (menor):
                print('Você errou. Seu chute foi menor que o número secreto ')
                if (rodada == total_tentativas):
                    print(f'O numero secreto era {numero_secreto} e você fez {pontos:.0f} pontos')


        # rodada = rodada + 1  -- Usado no while

        print('Fim de jogo')

    #diferenciando um arquivo executado de um importado.
    # Se a variavel está preenchida, o python rodou essa variável diretamente. Se não estiver preenchida, é porque ela só foi importada
    #Usamos o if abaixo para saber isso:

if(__name__ == "__main__"):
    jogar()  #para executar após definir ele como um import, pois sem chamar a função, ele não funciona mais