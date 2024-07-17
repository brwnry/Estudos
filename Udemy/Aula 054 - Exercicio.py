'''
1. Faça uma lista de compras com listas.
2. O usuário deve ter a possibilidade de inserir, apagar e listar valores da sua lista.
3. Não permita que o programa quebre com erros de índices inexistentes na lista.
'''

# Tela de entrada:
# Selecione uma das opções abaixo:
# [i]nserir [a]pagar [l]istar

def insere():
    item = input('Nome do item a inserir: ')
    lista_compras.append(item)
    lista()

def apaga():
    item = input('Nome do item a ser excluido: ')
    if item not in lista_compras:
        print('*** Item nao existe na lista ***')
    else:
        lista_compras.remove(item)
        if item not in lista_compras:
            print('*** Item removido com sucesso! ***')
            print()

def lista():
    if len(lista_compras) == 0:
        print('*** A lista esta vazia ***\n')
    else:
        print()
        print('*** Lista de produtos cadastrados ate o momento: ***\n')
        for produto in lista_compras:
            print(lista_compras.index(produto)+1, '-', produto + ', ')
    print()


lista_compras = []


while True:
    opcao = input('Selecione uma das opções abaixo:\n[i]nserir  [a]pagar  [l]istar [s]air  ').lower()

    if opcao == 'i':
        insere()
    elif opcao == 'a':
        apaga()
    elif opcao == 'l':
        lista()
    elif opcao == 's':
        break
    else:
        print('Opcao invalida!')
