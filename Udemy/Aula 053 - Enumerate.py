# Enumerate - enumera iteráveis (índices).

# Exemplo 1:

nomes = ['Maria', 'João', 'José']         # Variável nomes recebe uma lista de strings [Maria, João, José]
for i in enumerate(nomes):                # Para cada índice e nome na lista enumerada,
    indice, nome = i                      # atribua o índice e o nome a variável indice e nome.
    print(indice, nome)                   # Exibe o índice seguido do nome.

# Resultado:
# 0 Maria
# 1 João
# 2 José

# Exemplo 2: exatamente a mesma coisa do exemplo anterior, mas com uma sintaxe mais simples

nomes = ['Maria', 'João', 'José']         # Variável nomes recebe uma lista de strings [Maria, João, José]
for indice, nome in enumerate(nomes):     # Para cada índice e nome na lista enumerada,
    print(indice, nome)                   # Exibe o índice seguido do nome.

# Resultado:
# 0 Maria
# 1 João
# 2 José

# Exemplo 3:

lista = ['Maria', 'João', 'José']         # Variável lista recebe uma lista de strings [Maria, João, José] 
lista_enumerada = enumerate(lista)        # Variável lista_enumerada recebe uma lista enumerada da lista.

for item in lista_enumerada:              # Para cada item na lista enumerada,
    print(item)                           # Exibe o item.

# Resultado:
# (0, 'Maria')
# (1, 'João')
# (2, 'José')