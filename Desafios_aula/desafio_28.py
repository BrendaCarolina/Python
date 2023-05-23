# escreva um programa que faça o computador pensar em um numero inteiro entre 0 e 5 e peça para o usuario tentar descobrir o numero escolhido.
# o programa devera escrever na tela se o usuario venceu ou perdeu

from random import randint
from time import sleep #biblioteca de tempo


print('Vou pensar em um numero entre 0 e 5. Tente adivinhar...')

n = int(input('Em qual numero eu pensei? '))
pc = randint(0, 5)
print('PROCESSANDO...')
sleep(3) #tempo em segundos que demorará pra aparecer a resposta

if n == pc:
    print('Parabens! Você acertou o numero!')
else:
    print('Tente novamente')