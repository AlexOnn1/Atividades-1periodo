'''11 - Faça um algoritmo que leia quatro notas obtidas por um aluno, calcule a 
média das nota obtidas, imprima na tela o nome do aluno e se o aluno foi 
aprovado ou reprovado. Para o aluno ser considerado aprovado sua média final 
deve ser maior ou igual a 7.'''
aluno = str(input('Insira o nome do aluno: '))
n1 = float(input('Insira a primeira nota: '))
n2 = float(input('Insira a segunda nota: '))
n3 = float(input('Insira a terceira nota: '))
n4 = float(input('Insira a quarta nota: '))
media = float("{:.2f}".format((n1+n2+n3+n4)/4))
print('A média das notas do aluno', aluno,' é:', media)

if media >= 7:
    print(aluno, 'está aprovado!')
else:
    print(aluno, 'está reprovado!')