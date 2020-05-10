carteira = float(input('Quanto dinheiro você tem em carteira? R$ '))
dolar = 5.25
euro = 5.75
print('Você tem R${}.  Pode comprar US${:.2f} ou €{:.2f}'.format(carteira, carteira/dolar, carteira/euro))