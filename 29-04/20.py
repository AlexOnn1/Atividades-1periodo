'''20 - Faça um algoritmo que receba um valor inteiro e imprima na tela a sua 
tabuada. '''

numero = int(input("Digite um número inteiro para ver sua tabuada: "))

print(f"Tabuada do {numero}:")
for i in range(1, 11):
    print(f"{numero} x {i} = {numero * i}")