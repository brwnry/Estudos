# Listas de listas e seus íncices:

salas = [
    # 0        1         2       3                                             Índices de itens dentro da lista
    ['Maria', 'Helena', 'Luiz', 'João'], # 0                                   Índice da lista
    # 0         1          2         3                                         Índices de itens dentro da lista
    ['Marcos', 'Marcela', 'Miguel', 'Ana'], # 1                                Índice da lista
    # 0          1       2           3          4                              Índices de itens dentro da lista
    ['Joaquim', 'João', 'Joaquina', 'Joaquim', (0, 10, 20, 30, 40)], # 2       Índice da lista
]

print(salas[0][1]) # Helena
print(salas[2][4][2]) # 20

for sala in salas:
    for aluno in sala:
        print(aluno) # Maria, Helena, Luiz, João, Marcos, Marcela, Miguel, Ana, Joaquim, João, Joaquina, Joaquim, Joaquim, Joaquim

for sala, aluno in (salas):
    print(sala, aluno) # Maria, Helena, Luiz, João, Marcos, Marcela, Miguel, Ana, Joaquim, João, Joaquina, Joaquim, Joaquim, Joaquim