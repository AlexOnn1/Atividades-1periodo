opcao = 0

nomes = []

def menu():
    print('=========================================')
    print('Escolha uma das opções para acessar sua lista de convidados:')
    print('1 - Ver lista')
    print('2 - Adicionar Convidado')
    print('3 - Remover Convidado')
    print('4 - Sair')
    
    opcao = int(input('Digite sua opção: '))
    if opcao == 1:
        ver_lista()

    if opcao == 2:
        adicionar()

    if opcao == 3:
        remover()

    if opcao == 4:
        sair()

  

 
def ver_lista():
    print('=========================================')
    print(nomes)
    menu()    
    
def adicionar():
    print('=========================================')
    print('Qual convidado você quer adicionar à lista? ')
    nomes.append(input())                                        
    menu()
        
def remover():
    print('=========================================')
    print('Qual convidado você quer remover da lista? (digite o número correspondente ao convidado) ')
    cont=0
    for i in nomes:
        cont = cont + 1

        print(cont, '-', nomes[cont-1])
    nomes.pop(int(input())-1)   
    menu()                                         

def sair():
    exit  

menu()    