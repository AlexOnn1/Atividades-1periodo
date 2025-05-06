'''14 - Faça um algoritmo que receba um valor A e B, e troque o valor de A por B 
e o valor de B por A e imprima na tela os valores'''
a = input('Insira um valor para A: ')
b = input('Insira um valor para B: ')
print('Valor de A: ',a)
print('Valor de B: ',b)
c = a
a = b
b = c
print('Valor de A trocado: ',a)
print('Valor de B trocado: ',b)