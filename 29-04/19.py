'''19 - Faça um algoritmo que imprima na tela a tabuada de 1 até 10. '''


for i in range(1, 11):  
    print(f"Tabuada do {i}:")
    for j in range(1, 11): 
        print(f"{i} x {j} = {i * j}")
    print()