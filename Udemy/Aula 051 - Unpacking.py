# Unpacking ou desempacotamento é o processo de extrair os valores de uma lista ou de um dicionário e atribuí-los a variáveis separadamente.

# Exemplo 1:

a, b, c = 1, 2, 3         # a recebe 1, b recebe 2 e c recebe 3
print(a)                  # imprime 1
print(b)                  # imprime 2
print(c)                  # imprime 3

# Exemplo 2:

a, b, c = range(3)        # a recebe 0, b recebe 1 e c recebe 2
print(a)                  # imprime 0
print(b)                  # imprime 1
print(c)                  # imprime 2

# Exemplo 3:

a, b, c = range(3)        # a recebe 0, b recebe 1 e c recebe 2
print(a, b, c)            # imprime 0 1 2

# Exemplo 4:

a, b, c = range(3)        # a recebe 0, b recebe 1 e c recebe 2
print(a, b, c, sep='-')   # imprime 0-1-2

# Exemplo 5:

a, b, c = range(3)                  # a recebe 0, b recebe 1 e c recebe 2
print(a, b, c, sep='-', end='.')    # imprime 0-1-2.

# Exemplo 6: Udemy

nome1, nome2, nome3 = ['Maria', 'João', 'José']     # Variáveis nome1, nome2 e nome3 recebem uma lista de strings
print(nome2)                                        # imprime 'João'

# Exemplo 7: Udemy

nome1, *resto = ['Maria', 'João', 'José']           # Variável nome1 recebe 'Maria', variável resto recebe uma lista
print(nome1, resto)                                 # imprime 'Maria' ['João', 'José']

# Exemplo 8: Udemy
# asterisco e underline para indicar que não vai ser utilizado, mas ainda é armazenado numa lista

nome1, *_ = ['Maria', 'João', 'José']               # Variável nome1 recebe 'Maria', variável resto recebe uma lista contendo 'João' e 'José'
print(nome1)                                        # imprime 'Maria'

# Exemplo 9: Udemy
# underline para indicar que não vai ser utilizado

_, nome2, *_ = ['Maria', 'João', 'José']           # Variável nome1 recebe 'Maria', variável nome2 recebe 'João' e variável resto recebe uma lista contendo 'José'
print(nome2)                                       # imprime 'João'
