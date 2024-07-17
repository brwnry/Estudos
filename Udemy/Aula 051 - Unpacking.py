# Unpacking:

# Exemplo 1:

a, b, c = 1, 2, 3 # a = 1, b = 2, c = 3
print(a) # 1
print(b) # 2
print(c) # 3

# Exemplo 2:

a, b, c = range(3) # a = 0, b = 1, c = 2
print(a) # 0
print(b) # 1
print(c) # 2

# Exemplo 3:

a, b, c = range(3) # a = 0, b = 1, c = 2
print(a, b, c) # 0 1 2

# Exemplo 4:

a, b, c = range(3) # a = 0, b = 1, c = 2
print(a, b, c, sep='-') # 0-1-2

# Exemplo 5:

a, b, c = range(3) # a = 0, b = 1, c = 2
print(a, b, c, sep='-', end='.') # 0-1-2.

# Exemplo 6: Udemy

nome1, nome2, nome3 = ['Maria', 'João', 'José'] # nome1 = 'Maria', nome2 = 'João', nome3 = 'José'
print(nome2) # João

# Exemplo 7: Udemy

nome1, *resto = ['Maria', 'João', 'José'] # nome1 = 'Maria', resto = ['João', 'José']
print(nome1, resto) # Maria ['João', 'José']

# Exemplo 8: Udemy
# asterisco e underline para indicar que não vai ser utilizado, mas ainda é armazenado numa lista

nome1, *_ = ['Maria', 'João', 'José'] # nome1 = 'Maria', _ = ['João', 'José']
print(nome1) # Maria

# Exemplo 9: Udemy
# underline para indicar que não vai ser utilizado
_, nome2, *_ = ['Maria', 'João', 'José'] # _ = 'Maria', nome2 = 'João', _ = ['José']
print(nome2) # João
