#crie um programa que leia o nome completo de uma pessoa e mostre:
# o nome com todas as letras maiusculas, com todas letras minusculas, quantas letras tem (sem considerar os espaços) e quantas letras tem o primeiro nome

nome = str(input('Qual seu nome completo? ')).strip()  #se o usuário inserir espaços antes e depois da resposta, não irá contabilizar

print(nome.upper())
print(nome.lower())
print(len(nome)-nome.count(' '))  #nome menos espaços
print(nome.find(' ')) #vai parar no primeiro espaço
#também pode ser:
separa = nome.split()
print(separa[0]) #vai mostrar o nome
print(len(separa[0])) #vai mostrar a qnt de caracteres da palavra (0 porque é a primeira palavra)



