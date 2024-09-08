# Unpacking em chamada de métodos e funções.
#
string = 'EFGH'
lista = ['Maria', 'Helena', 1, 2, 3, 'Eduarda']
tupla = 'Python', 'é', 'legal'

salas = [
    # 0        1         2       3                                             Índices de itens dentro da lista
    ['Maria', 'Helena', 'Luiz', 'João'], # 0                                   Índice da lista
    # 0         1          2         3                                         Índices de itens dentro da lista
    ['Marcos', 'Marcela', 'Miguel', 'Ana'], # 1                                Índice da lista
    # 0          1       2           3          4                              Índices de itens dentro da lista
    ['Joaquim', 'João', 'Joaquina', 'Joaquim', (0, 10, 20, 30, 40)], # 2       Índice da lista
]

# Exemplo 1:
a, b, *_, y, z = lista                                                         # índice a é o primeiro elemento, b é o segundo elemento, *_ é o restante, y é o penúltimo elemento, z é o último elemento
print(a, z) # Maria Eduarda

# Exemplo 2:
print(*lista) # Maria Helena 1 2 3 Eduarda
print(*tupla) # Python é legal

# Exemplo 3:
print(*string) # E F G H
print(*lista, sep='-') # Maria-Helena-1-2-3-Eduarda
print(*tupla, sep='-') # Python-é-legal

# Exemplo 4:
print(*lista, sep='\n') # Maria
# Helena
# 1
# 2
# 3
# Eduarda

# Exemplo 5:
print(*lista, sep='\n', end='!') # Maria
# Helena
# 1
# 2
# 3
# Eduarda!

# Exemplo 6:
print(*lista, sep='\n', end='!') # Maria
# Helena
# 1
# 2
# 3
# Eduarda!

# Exemplo 7:
print(*lista, sep='\n', end='!') # Maria
# Helena
# 1
# 2
# 3
# Eduarda!

# Exemplo 8:
print(*salas, sep='\n')

# ['Maria', 'Helena', 'Luiz', 'João']
# ['Marcos', 'Marcela', 'Miguel', 'Ana']
# ['Joaquim', 'João', 'Joaquina', 'Joaquim', (0, 10, 20, 30, 40)]