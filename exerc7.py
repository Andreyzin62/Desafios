from ssl import ALERT_DESCRIPTION_UNKNOWN_CA


#Desenvolva um programa que leia as duas notas de um aluno, calcule e mostre a sua média.

n1 = float(input('Primeira nota: '))
n2 = float(input('Segunda nota: ' ))

media = (n1 + n2) / 2

print('A média entre {:.2f} e {:.2f} é igual a {:.2f}'.format(n1, n2, media))