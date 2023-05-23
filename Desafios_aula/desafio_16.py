# Crie um programa que leia um numero real e mostre na tela sua porção inteira

import math

real = float(input('Digite um número: '))
print(f'O inteiro do numero {real} é {math.trunc(real)}')
