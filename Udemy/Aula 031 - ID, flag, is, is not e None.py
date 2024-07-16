# id -> identidade de algo que é guardado na memória.

# Exemplo:

v1 = 'a'
v2 = 'b'
print(id(v1)) # 140739352566272
print(id(v2)) # 140739352566272

# flag -> indica se algo é verdadeiro ou falso.

# Exemplo:

flag = True
print(flag) # True

# is -> verifica se algo é igual a outra coisa.

# Exemplo:

v1 = 'a'
v2 = 'b'
print(v1 is v2) # False
print(v1 is not v2) # True

# is not -> verifica se algo é diferente de outra coisa.

# Exemplo:

v1 = 'a'
v2 = 'b'
print(v1 is not v2) # True
print(v1 is v2) # False

# None -> indica que algo não tem valor.

# Exemplo:

v1 = None
print(v1) # None
print(v1 is None) # True
print(v1 is not None) # False