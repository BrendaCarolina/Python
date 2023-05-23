#faça um programa que leia 3 numeros e mostre qual o maior e qual o menor

n1 = int(input('Digite o primeiro numero: '))
n2 = int(input('Digite o segundo numero: '))
n3 = int(input('Digite o terceiro numero: '))

#possivel solução também é colocar os numeros em uma lista e tirar o min e o max dessa lista

if n1 < n2 and n1 < n3:
    menor = n1
if n2 < n3 and n2 < n1:
    menor = n2
if n3 < n1 and n3 < n2:
    menor = n3
if n1 > n2 and n1 > n3:
    maior = n1
if n2 > n3 and n2 > n1:
    maior = n2
if n3 > n1 and n3 > n2:
    maior = n3


print(f'O menor valor digitado foi {menor}')
print(f'O maior valor digitado foi {maior}')