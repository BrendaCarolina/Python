# faça um programa que leia a largura e a altura de uma parede em metros, calcule sua area e a quantidade de tinta necessaria
# para pinta-la sabendo que cada litro de tinta pinta uma area de 2m²

largura = float(input('Qual a largura da parede? '))
altura = float(input('Qual a altura da parede? '))

area = float(largura * altura)

print(f'Para pintar uma área de {area} será necessario {area * 2} litros de tinta')