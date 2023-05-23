#Faça um programa que leia uma frase via input e mostre:
# quantas vezes aparece a letra "a', em que posição ela aparece pela primeira vez e pela ultima vez

frase = str(input('Digite uma frase qualquer: ')).upper().strip()

print(frase.count('A'))
print(frase.find('A')) #colocar +1 (frase.find('A')+1) para na hora que mostrar no console, começar do 1 e mostrar a posição certa se fossemos contar na mão
# (Ex: Brenda no normal: letra e posição 2. Com o +1: letra e posição 3)
print(frase.rfind('A'))


