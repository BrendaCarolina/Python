# calcule o salario de um funcionario com o aumento de 15%

salario = float(input('Qual seu salário? '))
novoSalario = salario * 0.15

print(f'Seu aumento foi de R${novoSalario} e seu novo salário será R${salario + novoSalario:.2f}')