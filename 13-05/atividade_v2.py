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
        exit()

  

 
def ver_lista():
    print('=========================================')
    print(nomes)
    menu()    
    
def adicionar():
    print('=========================================')
    print('Qual convidado você quer adicionar à lista? ')
    novo_convidado = str(input('Nome do convidado: '))
    if novo_convidado in nomes:
        print('!!!!!')
        print('Esse convidado já está na lista! Insira outro nome')
        print('!!!!!')
        adicionar()
    else:        
        nomes.append(novo_convidado)    
        print('Convidado adicionado')                                    
    menu()
        
def remover():
    print('=========================================')
    print('Qual convidado você quer remover da lista?')
    convidado_removido = str(input('Nome do convidado: '))
    if convidado_removido in nomes:
        nomes.remove(convidado_removido)
        print('Convidado removido')
    elif convidado_removido.lower() == 'sair':
        menu()                        
    else:
        print('!!!!!')
        print('O convidado não está na lista! Digite outro nome ou digite corretamente!')
        print('Digite "sair" para voltar ao menu')
        print('!!!!!')
        remover()        
    menu()                                         

def sair():
    print('Encerrando aplicação...')  
    return opcao

while opcao != 4:
    opcao = menu()    