# Listas de listas e seus índ ices:

salas = [
    # 0        1         2       3                                             Índices de itens dentro da lista
    ['Maria', 'Helena', 'Luiz', 'João'],                             # 0       Índice da lista
    # 0         1          2         3                                         Índices de itens dentro da lista
    ['Marcos', 'Marcela', 'Miguel', 'Ana'],                          # 1       Índice da lista
    # 0          1       2           3          4                              Índices de itens dentro da lista
    ['Joaquim', 'João', 'Joaquina', 'Joaquim', (0, 10, 20, 30, 40)], # 2       Índice da lista
    #                                           0  1   2   3   4               ìndices de itens dentro da lista
]

print(salas[0][1])              # Imprime 'Helena'
print(salas[2][4][2])           # Imprime o elemento na posição (2) da lista de tuplas (4) da lista (2)

for sala in salas:              # Para cada sala na lista de salas, faça:
    for aluno in sala:          # Para cada aluno na sala, faça:
        print(aluno)            # Imprima o aluno

# resultado:

# Maria
# Helena
# Luiz
# João
# Marcos
# Marcela
# Miguel
# Ana
# Joaquim
# João
# Joaquina
# Joaquim
# (0, 10, 20, 30, 40)

for sala, aluno in (salas):     # Para cada sala e aluno na lista de salas, faça:
    print(sala, aluno)          # Imprima a sala e o aluno

# resultado:

# Maria Helena Luiz João
# Marcos Marcela Miguel Ana
# Joaquim João Joaquina Joaquim 
# (0, 10, 20, 30, 40)
