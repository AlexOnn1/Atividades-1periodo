'''16 - Faça um algoritmo que leia três valores que representam os três lados de 
um triângulo e verifique se são válidos, determine se o triângulo é equilátero, 
isósceles ou escaleno.'''

# Função para verificar se os lados formam um triângulo válido
def eh_triangulo(a, b, c):
    return a + b > c and a + c > b and b + c > a

# Função para determinar o tipo de triângulo
def tipo_triangulo(a, b, c):
    if a == b == c:
        return "Equilátero"
    elif a == b or a == c or b == c:
        return "Isósceles"
    else:
        return "Escaleno"

# Entrada dos lados do triângulo
a = float(input("Digite o valor do lado A: "))
b = float(input("Digite o valor do lado B: "))
c = float(input("Digite o valor do lado C: "))

# Verificação e saída
if eh_triangulo(a, b, c):
    print(f"Os lados formam um triângulo {tipo_triangulo(a, b, c)}.")
else:
    print("Os valores informados não formam um triângulo.")