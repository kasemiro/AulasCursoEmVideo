from math import hypot
co = float(input('Digite o Cateto Oposto: '))
ca = float(input('Digite o Cateto Adjacente: '))
hip = hypot(co, ca)
print('Hipotenusa igual a {:.2f}'.format(hip))