salário = float(input('Qual é o sálario do funcionário? R$'))
novo = salário + (salário * 15 / 100)

print('O funcionário que ganhava {:.2f} , com 15% de aumento , passa a receber {:.2f}'.format(salário , novo))