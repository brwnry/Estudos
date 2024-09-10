# id -> identidade de algo que é guardado na memória.

# Exemplo:

v1 = 'a'              # variável v1 recebe 'a'
v2 = 'b'              # variável v2 recebe 'b'
print(id(v1))         # Exibe a id de v1: 140739752912640 
print(id(v2))         # Exibe a id de v2: 140739752912640

# flag -> indica se algo é verdadeiro ou falso.

# Exemplo:

flag = True           # variável flag recebe True
print(flag)           # Exibe True

# is -> verifica se algo é igual a outra coisa.

# Exemplo:

v1 = 'a'              # variável v1 recebe 'a'
v2 = 'b'              # variável v2 recebe 'b'
print(v1 is v2)       # Exibe False
print(v1 is not v2)   # Exibe True

# is not -> verifica se algo é diferente de outra coisa.

# Exemplo:

v1 = 'a'              # variável v1 recebe 'a'
v2 = 'b'              # variável v2 recebe 'b'
print(v1 is not v2)   # Exibe True
print(v1 is v2)       # Exibe False

# None -> indica que algo não tem valor.

# Exemplo:

v1 = None             # variável v1 recebe None
print(v1)             # Exibe None
print(v1 is None)     # Exibe True
print(v1 is not None) # Exibe True