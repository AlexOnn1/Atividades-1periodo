'''13 - Faça algoritmo que leia o nome e a idade de uma peso e imprima na tela o 
nome da pessoa e se ela é maior ou menor de idade'''
nome = str(input('Insira seu nome: '))
idade = int(input('Insira sua idade: '))

if idade>=18:
    print('Uau,', nome,', você é maior de idade! Incrivel!')
else:
    print('Você é menor de idade, ',nome,', vá embora.')    