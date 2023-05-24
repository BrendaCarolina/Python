#subst = "Python"
#verbo = "é"
#adjetivo = "fantástico"
# print(subst, verbo, adjetivo, sep="_", end="!\n")

#********************************************************

import random
print('**********************************')
print('Bem vindo ao Jogo de Advinhação')
print('**********************************')

#numero_secreto = int(round(random.random() * 100))
numero_secreto = int(random.randrange(1, 101))
total_tentativas = 3
rodada = 1

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
        print('Você acertou!')
        break
    else:
        if(maior):
            print('Você errou. Seu chute foi maior que o numero secreto ')
        elif (menor):
            print('Você errou. Seu chute foi menor que o número secreto ')

    # rodada = rodada + 1  -- Usado no while

print('Fim de jogo')