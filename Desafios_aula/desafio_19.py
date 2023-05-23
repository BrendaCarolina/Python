# um professor quer sortear 1 dos seus 4 alunos para apagar o quadro. faça um prog q o ajude nisso


import random

a1 = str(input('Aluno 1: '))
a2 = str(input('Aluno 2: '))
a3 = str(input('Aluno 3: '))
a4 = str(input('Aluno 4: '))
lista = [a1, a2, a3, a4]
sorteio = (random.choice(lista))

print(f' O aluno sorteado foi: {sorteio}')