from random import choice
a1 = input('Nome do aluno: ')
a2 = input('Nome do aluno: ')
a3 = input('Nome do aluno: ')
a4 = input('Nome do aluno: ')
lista = [a1, a2, a3, a4]
sorteio = choice(lista)
print('O aluno sorteado foi {}'.format(sorteio))