#Escreva um programa que leia a velocidade de um carro.
#se ele ultrapassar 80km/h mostre a mensagem dizendo que ele foi multado. A multa custará 7 reais por cada km acima do limite

velocidade = int(input('Digite a velocidade do carro: '))

if velocidade > 80:
    multa = (velocidade - 80) * 7
    print(f'Você estava a {velocidade}km/h e foi multado em R$ {multa}')
else:
    print('Parabens, você estava abaixo de 80km/h')