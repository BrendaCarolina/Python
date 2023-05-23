# subst = "Python"
#verbo = "é"
#adjetivo = "fantástico"
# print(subst, verbo, adjetivo, sep="_", end="!\n")

#********************************************************

print('**********************************')
print('Bem vindo ao Jogo de Advinhação')
print('**********************************')

numero_secreto = int(42)

chute = int(input('Digite seu palpite: '))
print('Você digitou: ', chute)

acertou = numero_secreto == chute
maior = chute > numero_secreto
menor = chute < numero_secreto

if (acertou):
    print('Você acertou!')
else:
    if(maior):
        print('Você errou. Seu chute foi maior que o numero secreto ')
    elif (menor):
        print('Você errou. Seu chute foi menor que o número secreto ')

print('Fim de jogo')