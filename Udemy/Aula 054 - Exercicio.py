'''
1. Faça uma lista de compras com listas.
2. O usuário deve ter a possibilidade de inserir, apagar e listar valores da sua lista.
3. Não permita que o programa quebre com erros de índices inexistentes na lista.
'''

# Tela de entrada:
# Selecione uma das opções abaixo:
# [i]nserir [a]pagar [l]istar

# Lista Bruno

import os                                                         # Importa a biblioteca os

lista_de_compras = []                                             # Cria uma lista vazia

while True:                                                       # Loop infinito
    print('Escolha um dos itens abaixo: ')                        # Imprime na tela
    print('[i]nserir    [a]pagar    [l]istar   [s]air')           # Imprime na tela

    opcao = input('Opção: ')                                      # Recebe a opção do usuário

    if opcao == 'i':                                              # Se a opção for 'i'
        os.system('clear')                                        # Limpa a tela
        
        item = input('Item: ')                                    # Recebe o item    
        lista_de_compras.append(item)                             # Adiciona o item na lista de compras    
        print(f'O item {item} foi adicionado à lista!')           # Imprime na tela
    
    elif opcao == 'a' and len(lista_de_compras) > 0:              # Se a opção for 'a' e a lista não estiver vazia
        os.system('clear')                                        # Limpa a tela
        
        try:                                                      # Tenta executar o código abaixo
            item = input('Item: ')                                # Recebe o item
            lista_de_compras.remove(item)                         # Remove o item da lista de compras    
            print(f'O item {item} foi removido da lista!')        # Imprime na tela
    
        except ValueError:                                        # Se ocorrer um erro de valor
            print('A lista já está vazia!')                       # Imprime na tela
            continue                                              # Continua o loop
    
    elif opcao == 'l':                                            # Se a opção for 'l'
        os.system('clear')                                        # Limpa a tela
        
        if len(lista_de_compras) == 0:                            # Se a lista estiver vazia
            print('Sua lista está vazia!')                        # Imprime na tela
            
        else:                                                     # Se a lista não estiver vazia
            print('Ok, aqui está a sua lista de compras!')        # Imprime na tela
        for indice, item in enumerate(lista_de_compras, start=1): # Para cada índice e item na lista de compras
            print(indice, item)                                   # Imprime na tela

    elif opcao == 's':                                            # Se a opção for 's'
        break                                                     # Sai do loop

    else:                                                         # Se a opção não for nenhuma das opções acima
        print('Escolha inválida')                                 # Imprime na tela
        os.system('clear')                                        # Limpa a tela

# Lista AI

import os                                                         # Importa a biblioteca os

lista_de_compras = []                                             # Cria uma lista vazia

def inserir_item():                                               # Função para inserir um item
    os.system('clear')                                            # Limpa a tela
    item = input('Item: ')                                        # Recebe o item
    lista_de_compras.append(item)                                 # Adiciona o item na lista de compras
    print(f'O item {item} foi adicionado à lista!')               # Imprime na tela

def apagar_item():                                                # Função para apagar um item
    os.system('clear')                                            # Limpa a tela
    item = input('Item: ')                                        # Recebe o item
    if item in lista_de_compras:                                  # Se o item estiver na lista de compras
        lista_de_compras.remove(item)                             # Remove o item da lista de compras
        print(f'O item {item} foi removido da lista!')            # Imprime na tela
    else:                                                         # Se o item não estiver na lista de compras
        print(f'O item {item} não está na lista!')                # Imprime na tela

def listar_itens():                                               # Função para listar os itens
    os.system('clear')                                            # Limpa a tela
    if len(lista_de_compras) == 0:                                # Se a lista estiver vazia
        print('Sua lista está vazia!')                            # Imprime na tela
    else:                                                         # Se a lista não estiver vazia
        print('Ok, aqui está a sua lista de compras!')            # Imprime na tela
        for indice, item in enumerate(lista_de_compras, start=1): # Para cada índice e item na lista de compras
            print(indice, item)                                   # Imprime na tela o índice e o item

while True:                                                       # Loop infinito
    print('Escolha um dos itens abaixo: ')                        # Imprime na tela
    print('[i]nserir    [a]pagar    [l]istar   [s]air')           # Imprime na tela

    opcao = input('Opção: ')                                      # Recebe a opção do usuário

    if opcao == 'i':                                              # Se a opção for 'i'
        inserir_item()                                            # Chama a função inserir_item
    elif opcao == 'a':                                            # Se a opção for 'a'
        apagar_item()                                             # Chama a função apagar_item
    elif opcao == 'l':                                            # Se a opção for 'l'
        listar_itens()                                            # Chama a função listar_itens
    elif opcao == 's':                                            # Se a opção for 's'
        break                                                     # Sai do loop
    else:                                                         # Se a opção não for nenhuma das opções acima
        print('Escolha inválida')                                 # Imprime na tela
        os.system('clear')                                        # Limpa a tela