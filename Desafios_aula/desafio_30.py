#Crie um programa que leia um numero inteiro e diga se ele é par ou impar

n = int(input('Digite um numero: '))
par = n % 2

if par == 0:
    print(f'O numero {n} é par')
else:
    print(f'O numero {n} é impar')