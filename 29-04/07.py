# - Faça um algoritmo que leia dois valores booleanos (lógicos) e determine se ambos são VERDADEIRO ou FALSO. 
# Sendo o número 1 Verdadeiro e 0 Falso.

def ler_valor_booleano(mensagem):
    while True:
        try:
            valor = int(input(mensagem))
            if valor in (0, 1):
                return bool(valor)
            else:
                print("Por favor, insira 1 para Verdadeiro ou 0 para Falso.")
        except ValueError:
            print("Entrada inválida. Por favor, insira 1 para Verdadeiro ou 0 para Falso.")

valor1 = ler_valor_booleano("Digite o primeiro valor (1 para Verdadeiro, 0 para Falso): ")
valor2 = ler_valor_booleano("Digite o segundo valor (1 para Verdadeiro, 0 para Falso): ")

if valor1 and valor2:
    print("Ambos os valores são VERDADEIRO.")
elif not valor1 and not valor2:
    print("Ambos os valores são FALSO.")
else:
    print("Os valores são diferentes.")