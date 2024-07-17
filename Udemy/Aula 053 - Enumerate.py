# Enumerate - enumera iteráveis (índices).

# Exemplo 1:

nomes = ['Maria', 'João', 'José'] # nomes = ['Maria', 'João', 'José']
for i in enumerate(nomes): # Para cada índice e nome na lista de nomes, faça:
    indice, nome = i # Desempacote o índice e o nome
    print(indice, nome) # Imprima o índice seguido do nome

# Exemplo 2: exatamente a mesma coisa do exemplo anterior, mas com uma sintaxe mais simples

nomes = ['Maria', 'João', 'José'] # nomes = ['Maria', 'João', 'José']
for indice, nome in enumerate(nomes): # Para cada índice e nome na lista de nomes, faça:
    print(indice, nome) # 0 Maria 1 Joao 2 José

# Exemplo 3:

lista = ['Maria', 'João', 'José'] # lista = ['Maria', 'João', 'José']
lista_enumerada = enumerate(lista) # lista_enumerada = [(0, 'Maria'), (1, 'João'), (2, 'José')]

for item in lista_enumerada: # Para cada item na lista_enumerada, faça:
    print(item) # (0, 'Maria') (1, 'João') (2, 'José')
