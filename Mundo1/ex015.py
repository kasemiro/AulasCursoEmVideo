d = int(input ('Quantos dias? '))
km = float(input('Quantos Km? '))
preço = d*60 + km*0.15
print('Para {} dias e {}km o valor a ser pago é de: R${:.2f}'.format(d, km, preço))