'''5 - Faça um algoritmo que leia o valor do salário mínimo e o valor do salário de 
um usuário, calcule quantos salários mínimos esse usuário ganha e imprima na 
tela o resultado. (Base para o Salário mínimo R$ 1.518,00).'''
sal_min = 1518
sal_user = int(input('Insira seu salário: '))
div = "{:.2f}".format(sal_user/sal_min)

print('Seu salário é equivalente a', div, 'salários mínimos')