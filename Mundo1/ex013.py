salario = float(input('Qual é o salário do Funcionário? R$ '))
aumento = salario + (salario * 15/100)
print('O salário aumentou de R$ {} para R$ {} com os 15% de ajuste'.format(salario, aumento))