from random import shuffle
a1 = input('Nome do Aluno 1: ')
a2 = input('Nome do Aluno 2: ')
a3 = input('Nome do Aluno 3: ')
a4 = input('Nome do Aluno 4: ')
lista = [a1, a2, a3, a4]
shuffle(lista)
print('A ordem de apresentação será: ')
print(lista)