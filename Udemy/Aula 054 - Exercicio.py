'''
1. Faça uma lista de compras com listas.
2. O usuário deve ter a possibilidade de inserir, apagar e listar valores da sua lista.
3. Não permita que o programa quebre com erros de índices inexistentes na lista.
'''

# Tela de entrada:
# Selecione uma das opções abaixo:
# [i]nserir [a]pagar [l]istar

# Bruno:

import os                                                                 # importa a biblioteca os

lista_de_compras = []                                                     # cria uma lista vazia

while True:                                                               # enquanto True, faça:
    print('Escolha um dos itens abaixo: ')                                # Exiba 'Escolha um dos itens abaixo: '
    print('[i]nserir    [a]pagar    [l]istar   [s]air')                   # Exiba '[i]nserir [a]pagar [l]istar [s]air'

    opcao = input('Opção: ')                                              # variável opcao recebe a opção digitada pelo usuário

    if opcao == 'i':                                                      # se a opção for 'i', faça:
        os.system('clear')                                                # limpa a tela
        
        item = input('Item: ')                                            # variável item recebe o item digitado pelo usuário
        lista_de_compras.append(item)                                     # adiciona o item digitado na lista de compras
        print(f'O item {item} foi adicionado à lista!')                   # Exibe 'O item {item} foi adicionado à lista!'
    
    elif opcao == 'a' and len(lista_de_compras) > 0:                      # se a opção for 'a' e a lista de compras não estiver vazia, faça:
        os.system('clear')                                                # limpa a tela
        
        try:                                                              # tente:
            item = input('Item: ')                                        # variável item recebe o item digitado pelo usuário
            lista_de_compras.remove(item)                                 # remove o item digitado da lista de compras
            print(f'O item {item} foi removido da lista!')                # Exibe 'O item {item} foi removido da lista!'
    
        except ValueError:                                                # se ocorrer um erro de valor, faça:
            print('A lista já está vazia!')                               # Exibe 'A lista já está vazia!'
            continue                                                      # pule para a próxima iteração do loop
    
    elif opcao == 'l':                                                    # se a opção for 'l', faça:
        os.system('clear')                                                # limpa a tela
        
        if len(lista_de_compras) == 0:                                    # se a lista de compras estiver vazia, faça:
            print('Sua lista está vazia!')                                # Exibe 'Sua lista está vazia!'
            
        else:                                                             # se não, faça:
            print('Ok, aqui está a sua lista de compras!')                # Exibe 'Ok, aqui está a sua lista de compras!'
        
        for indice, item in enumerate(lista_de_compras, start=1):         # para cada índice e item na lista de compras, faça:
            print(indice, item)                                           # Exibe o índice seguido do item.

    elif opcao == 's':                                                    # se a opção for 's', faça:
        break                                                             # pare o loop

    else:                                                                 # se não, faça:
        print('Escolha inválida')                                         # Exibe 'Escolha inválida'
        os.system('clear')                                                # limpa a tela

# Junior:

import os                                                                 # importa a biblioteca os

lista_de_compras = []                                                     # cria uma lista vazia

def inserir_item():                                                       # cria uma função para inserir um item na lista de compras
    os.system('clear')                                                    # limpa a tela
    item = input('Item: ')                                                # variável item recebe o item digitado pelo usuário
    lista_de_compras.append(item)                                         # adiciona o item digitado na lista de compras
    print(f'O item {item} foi adicionado à lista!')                       # Exibe 'O item {item} foi adicionado à lista!'

def apagar_item():                                                        # cria uma função para apagar um item da lista de compras
    os.system('clear')                                                    # limpa a tela
    item = input('Item: ')                                                # variável item recebe o item digitado pelo usuário
    if item in lista_de_compras:                                          # se o item estiver na lista de compras, faça:
        lista_de_compras.remove(item)                                     # remove o item digitado da lista de compras
        print(f'O item {item} foi removido da lista!')                    # Exibe 'O item {item} foi removido da lista!'
    else:                                                                 # se não, faça:
        print(f'O item {item} não está na lista!')                        # Exibe 'O item {item} não está na lista!'

def listar_itens():                                                       # cria uma função para listar os itens da lista de compras
    os.system('clear')                                                    # limpa a tela
    if len(lista_de_compras) == 0:                                        # se a lista de compras estiver vazia, faça:
        print('Sua lista está vazia!')                                    # Exibe 'Sua lista está vazia!'
    else:                                                                 # se não, faça:
        print('Ok, aqui está a sua lista de compras!')                    # Exibe 'Ok, aqui está a sua lista de compras!'
        for indice, item in enumerate(lista_de_compras, start=1):         # para cada índice e item na lista de compras, faça:
            print(indice, item)                                           # Exibe o índice seguido do item.

while True:                                                               # cria um loop infinito
    print('Escolha um dos itens abaixo: ')                                # Exibe 'Escolha um dos itens abaixo: '
    print('[i]nserir    [a]pagar    [l]istar   [s]air')                   # Exibe '[i]nserir [a]pagar [l]istar [s]air'

    opcao = input('Opção: ')                                              # variável opcao recebe a opção digitada pelo usuário

    if opcao == 'i':                                                      # se a opção for 'i', faça:
        inserir_item()                                                    # chama a função inserir_item()
    elif opcao == 'a':                                                    # se a opção for 'a', faça:
        apagar_item()                                                     # chama a função apagar_item()
    elif opcao == 'l':                                                    # se a opção for 'l', faça:
        listar_itens()                                                    # chama a função listar_itens()
    elif opcao == 's':                                                    # se a opção for 's', faça:
        break                                                             # pare o loop
    else:                                                                 # se não, faça:
        print('Escolha inválida')                                         # Exibe 'Escolha inválida'
        os.system('clear')                                                # limpa a tela