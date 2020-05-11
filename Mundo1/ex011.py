larg = float(input('Insira a Largura em metros: '))
alt = float(input('Insira a Altura em metros: '))
area = larg*alt
tinta = area/2
print('Essa parede de {}X{}, a área é de {}m².'.format(larg, alt, area))
print('Será necessário {}l de tinta.'.format(tinta))