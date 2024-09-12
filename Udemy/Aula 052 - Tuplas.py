# Tuplas sãos listas imutáveis.
# Tuplas são representadas por parênteses.

# - mais rápidas que listas.
# - não podem ser alteradas.
# - podem ser utilizadas como chaves de dicionários

# Exemplo 1:

tupla = (1, 2, 3, 4, 5)                 # Tupla com 5 elementos (1, 2, 3, 4, 5)
print(tupla)                            # (1, 2, 3, 4, 5)

# Exemplo 2:

tupla = (1, 2, 3, 4, 5)                 # Tupla com 5 elementos (1, 2, 3, 4, 5)
print(tupla[2])                         # Mostra o elemento na posição 2 da tupla (3)

# Exemplo 3:

tupla = (1, 2, 3, 4, 5)                 # Tupla com 5 elementos (1, 2, 3, 4, 5)
print(tupla[1:3])                       # Mostra os elementos da posição 1 até a posição 3 da tupla (2, 3)

# Exemplo 4:

tupla = (1, 2, 3, 4, 5)                 # Tupla com 5 elementos (1, 2, 3, 4, 5)
print(tupla[1:3:2])                     # Mostra os elementos da posição 1 até a posição 3 com passo de 2

# Exemplo 5:

tupla = (1, 2, 3, 4, 5)                 # Tupla com 5 elementos (1, 2, 3, 4, 5)
print(tupla[1::2])                      # Mostra os elementos da posição 1 até a posição 5 com passo de 2

# Exemplo 6:

tupla = (1, 2, 3, 4, 5)                 # Tupla com 5 elementos (1, 2, 3, 4, 5)
print(tupla[::-1])                      # Mostra os elementos da tupla invertidos (5, 4, 3, 2, 1)

# Exemplo 7:

tupla = (1, 2, 3, 4, 5)                 # Tupla com 5 elementos (1, 2, 3, 4, 5)
print(tupla[-1])                        # Mostra o último elemento da tupla (5)

# Exemplo 8: Udemy
# Convertendo uma lista em tupla:

nomes = ['Maria', 'João', 'José']       # Variável nomes recebe uma lista de strings [Maria, João, José]
nomes = tuple(nomes)                    # Converte a lista em tupla

# Exemplo 9: Udemy
# Convertendo uma tupla em lista:

nomes = ('Maria', 'João', 'José')       # Variável nomes recebe uma tupla de strings [Maria, João, José]
nomes = list(nomes)                     # Converte a tupla em lista