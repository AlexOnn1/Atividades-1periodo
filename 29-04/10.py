'''0 - Faça um algoritmo que leia três notas obtidas por um aluno, e imprima na 
tela a média das notas.'''
n1 = float(input('Insira a primeira nota: '))
n2 = float(input('Insira a segunda nota: '))
n3 = float(input('Insira a terceira nota: '))
media = "{:.2f}".format((n1+n2+n3)/3)
print('A média das notas é:', media)