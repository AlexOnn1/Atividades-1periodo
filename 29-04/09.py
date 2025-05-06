#- Faça um algoritmo que calcule o IMC (Índice de Massa Corporal) de uma pessoa, leia o seu peso e sua altura e imprima na tela sua condição de acordo com a tabela abaixo:
altura = float(input('Insira sua altura em metros (exemplo: 1.80): '))
peso =  float(input('Insira seu peso: '))
imc = float("{:.2f}".format(peso/(altura*altura)))

if imc < 18.5:
    print('Seu imc é:', imc,'. Você está abaixo do peso')
elif 18.6<=imc<=24.9:
    print('Seu imc é:', imc,'. Você está no peso ideal, parabéns!')
elif 25<=imc<=29.9:
    print('Seu imc é:', imc,'. Você está levemente acima do peso')
elif 30<=imc<=34.9:
    print('Seu imc é:', imc,'. Você está com Obesidade grau I, cuidado.')
elif 35<=imc<=30.9:
    print('Seu imc é:', imc,'. Você está com Obesidade grau II, essa é severa.')
elif 40<=imc:
    print('Seu imc é:', imc,'. Você está com Obesidade grau III, mórbida. F')                    
