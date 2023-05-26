print('**********************************')
print('******Escolha seu jogo!******')
print('**********************************')

print('Forca (1) ou Advinhação (2)? ')

jogo = int(input('Digite sua opção: '))

if(jogo == 1):
    print('Jogando forca')
elif (jogo == 2):
    print('Jogando adivinhação')
else:
    print('Valor incorreto. Escolha entre as opções disponíveis')