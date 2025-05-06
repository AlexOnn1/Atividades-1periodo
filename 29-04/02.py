'''2 - Faça um algoritmo para receber um número qualquer e imprimir na tela se o 
número é par ou ímpar, positivo ou negativo.'''
num = int(input('Insira um número: '))
if num > 0:
    print('O número é positivo')
elif num == 0:
    print('O número é zero')
else:
    print('O número é negativo')
    
if num % 2 == 0:
    print('O número é par')
else:
    print('O número é ímpar')