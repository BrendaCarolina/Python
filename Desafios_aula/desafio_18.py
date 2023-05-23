# Leia um angulo qualquer e mostre na tela o valor do seno, cosseno e a tangente desse angulo

# seno -> cateto oposto / hipotenusa
# cosseno -> cateto adjacente / hipotenusa  0,87
# tangente -> cateto oposto / cateto adjacente   0,58

import math

angulo = int(input('Qual angulo desejado? '))
seno = math.sin(math.radians(angulo))
cosseno = math.cos(math.radians(angulo))
tangente = math.tan(math.radians(angulo))
print(f'O seno de {angulo} é {seno:.2f}')
print(f'O cosseno de {angulo} é {cosseno:.2f}')
print(f'O tangente de {angulo} é {tangente:.2f}')
