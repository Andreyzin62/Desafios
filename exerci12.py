preço = float(input('Qual é o preço do produto?R$'))
novo = preço - (preço *5/ 100 )

print('O produto que custava {:.2f}R$ , na promoção com 5% vai custar {:.2f}'.format(preço , novo))

