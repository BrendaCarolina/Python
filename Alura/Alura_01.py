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

if (numero_secreto == chute):
    print('Você acertou!')
else:
    print('Você errou, tente novamente! ')

print('Fim de jogo')