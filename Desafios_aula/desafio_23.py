#Faça um programa que leia um numero de 0 a 9999 e mostre na tela cada um dos numeros separados por unidade, dezena, centena e milhar
#desafio: TENTAR MATEMATICAMENTE E POR STRING

numero = int(input('Digite um número de 0 a 9999: '))
u = numero // 1 % 10
d = numero // 10 % 10
c = numero // 100 % 10
m = numero // 1000 % 10

print(f'Unidade {u}')
print(f'Dezena {d}')
print(f'Centena {c}')
print(f'Milhar  {m}')

# por string fariamos uma lista mas não daria certo pois obrigatoriamente os 4 elementos da lista precisariam estar preenchidos
# ou seja, se digitassemos 123 ou 12 daria erro.