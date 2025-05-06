'''17 - Faça um algoritmo que leia uma temperatura em Fahrenheit e calcule a 
temperatura correspondente em grau Celsius. Imprima na tela as duas 
temperaturas. 
Fórmula: C = (5 * ( F-32) / 9)'''

fahrenheit = float(input("Digite a temperatura em Fahrenheit: "))

celsius = (5 * (fahrenheit - 32)) / 9

print(f"A temperatura em Fahrenheit é: {fahrenheit}°F")
print(f"A temperatura correspondente em Celsius é: {celsius:.2f}°C")