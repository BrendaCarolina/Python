# Leia o comprimento do cateto oposto e do cateto adjacente de um triangulo retangulo, calcule e mostre o comprimento da hipotenusa
# a hipotenusa é = a raiz quadrada da soma dos catetos ao quadrado

import math

catetoOposto = float(input('Qual o comprimento do cateto oposto? '))
catetoAdjacente = float(input('Qual o comprimento do cateto adjacente? '))
#tb poderia usar math.hypot(co,ca)
hipotenusa = math.sqrt(math.pow(catetoOposto, 2) + math.pow(catetoAdjacente, 2))

print(f'A hipotenusa mede {hipotenusa:.2f}')
