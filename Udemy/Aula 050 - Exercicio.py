# Exercício:

# Exiba os nomes da lista:
# 0 Maria
# 1 Helena
# 2 Luiz

lista = ['Maria', 'Helena', 'Luiz']  # Lista de nomes

for indice, nome in enumerate(
    lista):  # Para cada índice e nome na lista enumerada, faça:
  print(f'{indice} {nome}')  # Imprima o índice seguido do nome

# Professor:

lista = ['Maria', 'Helena', 'Luiz']  # Lista de nomes
indices = range(len(lista))  # Gera uma lista de índices

for indice in indices:  # Para cada índice na lista de índices, faça:
  print(f'{indice} {lista[indice]}')  # Imprima o índice seguido do nome

# Livro:

nomes = ['Maria', 'Helena', 'Luiz']  # Lista de nomes

for indice in range(len(nomes)):  # Para cada índice na lista de índices, faça:
  print(f'{indice} {nomes[indice]}')  # Imprima o índice seguido do nome
