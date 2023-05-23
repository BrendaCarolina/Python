#faça um programa que leia algo e mostre na tela seu tipo primitivo e todas as informações possíveis sobre ela

n = input("Digite algo: ")

print("O tipo primitivo desse valor é: ", type(n))
print("É um numerico? ", n.isnumeric())
print("é alfabético? ", n.isalpha())
print("Está em letra minúscula? ", n.islower())
print("Está em letra maiúscula? ", n.isupper())
print("Só tem espaço? ", n.isspace())
print("É decimal? ", n.isdecimal())
print("É alfanumerico? ", n.isalnum())
print("Está capitalizada? ", n.istitle()) #começa com letra maiuscula

