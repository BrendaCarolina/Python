#crie um programa que leia o nome de uma cidade e diga se ela começa ou não com o nome "Santo"

cidade = str(input('Digite o nome da sua cidade: ')).strip()

print(cidade[:5].upper() == 'SANTO')
#fatia o limite de 5 caracteres, transforma tudo em uppercase e restrinja a palavra já transformada em maiuscula, assim ele vai converter a palavra em maiuscula antes
#de analisar se está escrito certo ou não. Ex: Santo, SaNto, santo são aceitos porque ele vai ficar em uppercase primeiro e depois será verificado se é santo em maiuscula