# Tuplas sãos listas imutáveis.
# Tuplas são representadas por parênteses.
# - mais rápidas que listas.
# - não podem ser alteradas.
# - podem ser utilizadas como chaves de dicionários

# Exemplo 1:

tupla = (1, 2, 3, 4, 5) 
print(tupla) # (1, 2, 3, 4, 5)

# Exemplo 2:

tupla = (1, 2, 3, 4, 5)
print(tupla[2]) # 3

# Exemplo 3:

tupla = (1, 2, 3, 4, 5)
print(tupla[1:3]) # (2, 3)

# Exemplo 4:

tupla = (1, 2, 3, 4, 5)
print(tupla[1:3:2]) # (2, 4)

# Exemplo 5:

tupla = (1, 2, 3, 4, 5)
print(tupla[1::2]) # (2, 4)

# Exemplo 6:

tupla = (1, 2, 3, 4, 5)
print(tupla[::-1]) # (5, 4, 3, 2, 1)

# Exemplo 7:

tupla = (1, 2, 3, 4, 5)
print(tupla[-1]) # 5

# Exemplo 8: Udemy
# Convertendo uma lista em tupla:

nomes = ['Maria', 'João', 'José'] # nomes = ['Maria', 'João', 'José']
nomes = tuple(nomes) # nomes = ('Maria', 'João', 'José')

# Exemplo 9: Udemy
# Convertendo uma tupla em lista:

nomes = ('Maria', 'João', 'José') # nomes = ('Maria', 'João', 'José')
nomes = list(nomes) # nomes = ['Maria', 'João', 'José']