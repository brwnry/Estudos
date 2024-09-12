# For in com listas:

# Exemplo:

lista = ['Maria', 'João', 'Pedro', 'Ana']   # Variável lista recebe uma lista de strings [Maria, João, Pedro, Ana]
for nome in lista:                          # Para cada nome na lista,
    print(nome)                             # Imprima o nome.

# Resultado:
# Maria
# João
# Pedro
# Ana

# Exemplo diferente:

lista = ['Maria', 'João', 'Pedro', 'Ana']   # Variável lista recebe uma lista de strings [Maria, João, Pedro, Ana]
for nome in lista:                          # Para cada nome na lista,
    print(f'Olá {nome}')                    # Imprima 'Olá {nome}'.

# Resultado:
# Olá Maria
# Olá João
# Olá Pedro
# Olá Ana