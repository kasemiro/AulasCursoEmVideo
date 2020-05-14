nome = str(input('Digite um nome: ')). strip()
print('Nome Em Letras MAIÚSCULAS: {}'.format(nome.upper()))
print('Nome Em Letras minúsculas: {}'.format(nome.lower()))
print('Seu Nome é Formado Por {} Caracteres.'.format(len(nome) - nome.count(' ')))
print('Seu Primeiro Nome tem {} Caracteres.'.format(nome.find(' ')))
# separa = nome.split
# print('Seu primeiro Nome é {} e ele tem {} letras'.format(separa[0], len(separa[0])))
