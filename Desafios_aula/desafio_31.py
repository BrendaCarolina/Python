#Crie um programa que pergunte a distancia de uma viagem em km e calcule o preço da passagem, cobrando 0,50 por km para viagens até 200km
#e 0,45 para viagens mais longas

distancia = float(input('Qual a distancia da viagem? '))

if distancia <= 200:
    print(f'O valor da passagem é de R${distancia * 0.50}')
else:
    print(f'O valor da passagem é de R${distancia * 0.45}')