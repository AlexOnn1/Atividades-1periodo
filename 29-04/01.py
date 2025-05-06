'''1 - Faça um algoritmo que leia os valores de A, B, C e em seguida imprima na 
tela a soma entre A e B é mostre se a soma é menor que C.'''
a = int(input('Insira o valor de a:'))
b = int(input('Insira o valor de b:'))
c = int(input('Insira o valor de c:'))
print('A soma de A + B é:', a + b)
if a + b > c:
    print('A soma de A + B é maior que C')
elif a + b == c:
    print('A soma de A + B é igual a C')
else:   
    print('A soma de A + B é menor que C')