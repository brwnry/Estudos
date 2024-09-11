# Next, iter, iterável e iterador

# Iterável -> o que pode ser iterado - str, ramge, list, tuple, dict, set 
# Iterador -> quem sabe entregar um valor por vez
# next() -> retorna o próximo item do iterador
# iter() -> retorna um iterador

texto = 'Python'            # variável texto recebe 'Python'
iterador = iter(texto)      # variável iterador recebe um iterador

while True:                 # enquanto True, faça:
  try:                      # tente:
    letra = next(iterador)  # variável letra recebe o próximo item do iterador 
    print(letra)            # imprima letra
  except StopIteration:     # se houver um erro de StopIteration, faça:
    break                   # pare o loop

# Resultado:
# P
# y
# t
# h
# o
# n

# Que é exatamente a mesma coisa que:

for letra in texto:         # para cada letra na variável texto, faça:
  print(letra)              # imprima letra

# Resultado:
# P
# y
# t
# h
# o
# n