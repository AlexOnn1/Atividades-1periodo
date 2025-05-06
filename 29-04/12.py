'''12 - Faça um algoritmo que leia o valor de um produto e determine o valor que 
deve ser pago, conforme a escolha da forma de pagamento pelo comprador e 
imprima na tela o valor final do produto a ser pago. Utilize os códigos da tabela 
de condições de pagamento para efetuar o cálculo adequado.
Tabela de Código de Condições de Pagamento
1 - À Vista em Dinheiro ou Pix, recebe 15% de desconto
2 - À Vista no cartão de crédito, recebe 10% de desconto
3 - Parcelado no cartão em duas vezes, preço normal do produto sem juros
4 - Parcelado no cartão em três vezes ou mais, preço normal do produto mais 
juros de 10%'''

valor1 = float(input('Insira o valor do produto: '))
print('Por favor, escolha o método de pagamento: Dinheiro ou pix(1), À vista no cartão(2), Parcelado em 2x(3), Parcelado em 3x+(4)')
while True:
        try:
           pagamento=int(input()) 
           if pagamento < 1 or pagamento > 4:
            print('Por favor, selecione uma opção válida entre 1 e 4.')
            continue
        except ValueError:
            print('Por favor, selecione uma opção válida.')
            continue
        if pagamento == 1:
               valor_final = valor1*0.85
               print('O valor a ser pago no pix é:', valor_final)
        elif pagamento == 2:
               valor_final = valor1*0.9
               print('O valor a ser pago no cartão é:', valor_final)
        elif pagamento == 3:
               print('O valor a ser pago em 2x no cartão é: ',valor1)
        elif pagamento == 4:
               valor_final = valor1*1.1
               print('O valor a ser pago com juros de parcelamento é: ',valor_final)         