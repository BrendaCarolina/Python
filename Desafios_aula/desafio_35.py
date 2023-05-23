#Leia o comprimento de 3 retas e diga ao usuário se elas podem ou não formar um triangulo

r1 = float(input('Digite o comprimento da primeira reta: '))
r2 = float(input('Digite o comprimento da segunda reta: '))
r3 = float(input('Digite o comprimento da terceira reta: '))
# Em qualquer triângulo, a soma das medidas de dois lados é sempre maior que a medida do terceiro.

if r1 < r2 + r3 and r2 < r1 + r3 and r3 < r1 + r2:
    print('Os valores digitados podem formar um triangulo')
else:
    print('Os valores digitados não podem formar um triangulo')

