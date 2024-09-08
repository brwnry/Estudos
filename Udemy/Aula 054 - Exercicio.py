'''
1. Faça uma lista de compras com listas.
2. O usuário deve ter a possibilidade de inserir, apagar e listar valores da sua lista.
3. Não permita que o programa quebre com erros de índices inexistentes na lista.
'''

# Tela de entrada:
# Selecione uma das opções abaixo:
# [i]nserir [a]pagar [l]istar

# Lista versão 1

import os

lista_de_compras = []

while True:
    print('Escolha um dos itens abaixo: ')
    print('[i]nserir    [a]pagar    [l]istar   [s]air')

    opcao = input('Opção: ')

    if opcao == 'i':
        os.system('clear')
        
        item = input('Item: ')
        lista_de_compras.append(item)
        print(f'O item {item} foi adicionado à lista!')
    
    elif opcao == 'a' and len(lista_de_compras) > 0:
        os.system('clear')
        
        try:
            item = input('Item: ')
            lista_de_compras.remove(item)        
            print(f'O item {item} foi removido da lista!')
    
        except ValueError:
            print('A lista já está vazia!')
            continue
    
    elif opcao == 'l':
        os.system('clear')
        
        if len(lista_de_compras) == 0:
            print('Sua lista está vazia!')
            
        else:
            print('Ok, aqui está a sua lista de compras!')
        for indice, item in enumerate(lista_de_compras, start=1):
            print(indice, item)

    elif opcao == 's':
        break

    else:
        print('Escolha inválida')
        os.system('clear')

# Lista versão 2

import os

lista_de_compras = []

def inserir_item():
    os.system('clear')
    item = input('Item: ')
    lista_de_compras.append(item)
    print(f'O item {item} foi adicionado à lista!')

def apagar_item():
    os.system('clear')
    item = input('Item: ')
    if item in lista_de_compras:
        lista_de_compras.remove(item)
        print(f'O item {item} foi removido da lista!')
    else:
        print(f'O item {item} não está na lista!')

def listar_itens():
    os.system('clear')
    if len(lista_de_compras) == 0:
        print('Sua lista está vazia!')
    else:
        print('Ok, aqui está a sua lista de compras!')
        for indice, item in enumerate(lista_de_compras, start=1):
            print(indice, item)

while True:
    print('Escolha um dos itens abaixo: ')
    print('[i]nserir    [a]pagar    [l]istar   [s]air')

    opcao = input('Opção: ')

    if opcao == 'i':
        inserir_item()
    elif opcao == 'a':
        apagar_item()
    elif opcao == 'l':
        listar_itens()
    elif opcao == 's':
        break
    else:
        print('Escolha inválida')
        os.system('clear')