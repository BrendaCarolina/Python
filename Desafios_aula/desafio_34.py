#Escreva um programa que pergunte o salario de um funcionario e calcule o valor do seu aumento
#para salarios superiores a 1250,00 aumente 10%. Abaixo desse valor, 15%

salario = float(input('Qual seu salario? '))

if salario >= 1250.00:
    aumento = salario * 0.10
    print(f'Seu aumento foi de R${aumento:.2f} e agora você receberá R${salario + aumento:.2f}')
else:
    aumento = salario * 0.15
    print(f'Seu aumento foi de R${aumento:.2f} e agora você receberá R${salario + aumento:.2f}')
