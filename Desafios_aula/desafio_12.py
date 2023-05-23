# leia o preço de um produto e mostre seu novo preço com 5% de desconto

valor = float(input('Qual valor do produto? '))
print(f'O novo valor desse produto é de {valor - (valor * 0.05)}')