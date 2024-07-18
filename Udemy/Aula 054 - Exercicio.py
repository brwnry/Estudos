'''
1. Faça uma lista de compras com listas.
2. O usuário deve ter a possibilidade de inserir, apagar e listar valores da sua lista.
3. Não permita que o programa quebre com erros de índices inexistentes na lista.
'''

# Tela de entrada:
# Selecione uma das opções abaixo:
# [i]nserir [a]pagar [l]istar

lista_de_compras = []

while True:
    print('Selecione uma das opções abaixo:')
    print('[i]nserir  [a]pagar  [l]istar')

    opcao = input('Opção: ')

    if opcao == 'i':
        item = input('Item: ')
        lista_de_compras.append(item)

    elif opcao == 'a':
        item = input('item: ')
        lista_de_compras.remove(item)

    elif opcao == 'l':
        for indice, item in enumerate(lista_de_compras, start=1):
            print(indice, item)

    else:
        print('Opção inválida')