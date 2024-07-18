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