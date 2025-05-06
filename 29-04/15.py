'''15 - Faça um algoritmo que leia o ano em que uma pessoa nasceu, imprima na 
tela quantos anos, meses e dias essa pessoa ja viveu. Leve em
consideração o ano com 365 dias e o mês com 30 dias.
(Ex: 5 anos, 2 meses e 15 dias de vida)'''

ano_atual = 2025


while True:
    try:
        ano_nascimento = int(input("Digite o ano em que você nasceu: "))
        if ano_nascimento > ano_atual or ano_nascimento < 0:
            print("Por favor, insira um ano válido.")
            continue
        break
    except ValueError:
        print("Entrada inválida. Por favor, insira um número inteiro.")

anos = ano_atual - ano_nascimento
meses = anos * 12
dias = anos * 365

print('Você já viveu aproximadamente', anos,' anos, ',meses,' meses e ',dias,' dias.')