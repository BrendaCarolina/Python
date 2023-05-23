#Faça um programa que leia o nome completo de uma pessoa, mostrando em seguida o 1º e o ultimo nome separadamente

nome = str(input('Digite seu nome completo: ')).strip()
primeiro = nome.split()
ultimo = nome.split()
print(f" Seu primeiro nome é: {primeiro [0]}")
print(f"Seu ultimo nome é: {ultimo [len(nome)-1]}") #vai contar o tamanho da lista e mostrar -1 (pq começa no zero)

