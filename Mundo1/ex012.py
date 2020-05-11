preço = float(input('Digite o preço R$'))
desconto = preço - (preço*5/100)
print(' Na promoção o produto fica em R${:.2f}'.format(desconto))