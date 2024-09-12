'''
Exercício:

Exiba os nomes da lista:
0 Maria
1 Helena
2 Luiz
'''

# Bruno:

lista = ['Maria', 'Helena', 'Luiz']       # Variável lista recebe uma lista de strings

for indice, nome in enumerate(lista):     # Para cada índice e nome na lista enumerada, 
  print(f'{indice} {nome}')               # Imprima o índice seguido do nome.

# Resultado:
# 0 Maria
# 1 Helena
# 2 Luiz

# Professor:

lista = ['Maria', 'Helena', 'Luiz']       # Variável lista recebe uma lista de strings
indices = range(len(lista))               # Variável indices recebe uma lista de inteiros

for indice in indices:                    # Para cada índice na lista de índices,
  print(f'{indice} {lista[indice]}')      # Imprima o índice seguido do nome.

# Resultado:
# 0 Maria
# 1 Helena
# 2 Luiz

# Livro:

nomes = ['Maria', 'Helena', 'Luiz']       # Variável nomes recebe uma lista de strings

for indice in range(len(nomes)):          # Para cada índice na lista de índices,
  print(f'{indice} {nomes[indice]}')      # Imprima o índice seguido do nome.

# Resultado:
# 0 Maria
# 1 Helena
# 2 Luiz
