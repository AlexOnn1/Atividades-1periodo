'''8 - Faça um algoritmo que leia três valores inteiros diferentes e imprima na tela 
os valores em ordem decrescente'''
lista = []
a= lista.append(int(input('insira um valor: ')))
b= lista.append(int(input('insira um valor: ')))
c= lista.append(int(input('insira um valor: ')))

lista_reversa = sorted(lista, reverse=True)
print('lista revertida :', lista_reversa)