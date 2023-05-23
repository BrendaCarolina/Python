#faça um programa que leia um ano qualquer e diga se ele é bissexto ou não

ano = int(input('Digite o ano desejado: '))
bissexto = ano % 4

if bissexto == 0:
    print(f'O ano {ano} é bissexto')
else:
    print(f'O ano {ano} não é bissexto')
